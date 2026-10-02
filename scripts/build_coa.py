import csv, glob, os, re, subprocess, html
from datetime import date
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
REF = date(2026, 9, 30)
CUTOFF = date(2025, 9, 30)  # 12 months before reference date

def field(txt, label):
    m = re.search(r'^\s*' + re.escape(label) + r'[ \t]*(.*)$', txt, re.M)
    return m.group(1).strip() if m else ''

# ---- 1. extract
coas = []
for f in sorted(glob.glob('coa/*.pdf')):
    t = subprocess.run(['pdftotext', '-layout', f, '-'], capture_output=True, text=True).stdout
    num = lambda s: (re.match(r'([\d.]+)', s).group(1) if re.match(r'[\d.]+', s) else '')
    coas.append(dict(
        pdf_file=os.path.basename(f),
        report_id=field(t, 'Report ID:'),
        report_type=field(t, 'Report type:'),
        product=field(t, 'Product'),
        declared_amount_mg=num(field(t, 'Declared amount')),
        batch=field(t, 'Batch / lot number'),
        test_date=field(t, 'Test date'),
        purity_pct=num(field(t, 'Purity (HPLC)')),
        theoretical_mass_da=num(field(t, 'Identity: theoretical mass')),
        observed_mass_da=num(field(t, 'Identity: observed mass (MS)')),
    ))
cols = list(coas[0].keys())
with open('coa_extracted.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, cols); w.writeheader(); w.writerows(coas)

# ---- 2/3. reconcile + status
sheet = list(csv.DictReader(open('products.csv')))
rows, exc = [], []
for p in sheet:
    cands = [c for c in coas if c['product'] == p['Product']]
    assert cands, p['Product']
    # rule 2: newest test date (a blank date sorts last)
    c = sorted(cands, key=lambda c: c['test_date'] or '0000', reverse=True)[0]
    issues = []
    if len(cands) > 1:
        others = ', '.join(f"{x['pdf_file']} ({x['report_type'] or 'n/a'}, tested {x['test_date']})" for x in cands if x is not c)
        issues.append(('More than one COA exists: ' + ', '.join(x['pdf_file'] for x in cands) + '.',
                       'Rule 2 (newest test date wins)',
                       f"Used {c['pdf_file']} ({c['report_type'] or 'n/a'}, tested {c['test_date']}); ignored {others}."))
    final = {}
    for key, pk, sk in [('batch', 'batch', 'Batch_Listed'), ('test_date', 'test_date', 'Test_Date_Listed'),
                        ('purity', 'purity_pct', 'Purity_Listed_pct'), ('size', 'declared_amount_mg', 'Size_mg')]:
        pv, sv = c[pk], p[sk]
        if pv:
            final[key] = pv
            differs = (float(pv) != float(sv)) if key in ('purity', 'size') else (pv != sv)
            if sv and differs and key == 'size':
                issues.append((f"Sheet and PDF disagree on size: sheet {sv} mg, PDF declares {pv} mg.",
                               'Rule 1 (PDF overrides sheet) and Rule 4e (size conflict)',
                               f"Used PDF value {pv} mg for coa_size_mg; product held as draft until the price is confirmed."))
            elif sv and differs:
                issues.append((f"Sheet and PDF disagree on {key.replace('_',' ')}: sheet {sv}, PDF {pv}.",
                               'Rule 1 (PDF overrides sheet)', f"Used PDF value {pv}."))
        elif sv:
            final[key] = sv
            issues.append((f"PDF leaves {key.replace('_',' ')} blank; sheet has {sv}.",
                           'Rule 3 (blank on PDF, use sheet)', f"Used sheet value {sv}, recorded as \"from sheet\"."))
        else:
            final[key] = ''
            issues.append((f"{key.replace('_',' ').capitalize()} is blank on both the PDF and the sheet.",
                           'Rule 3 (both blank, field missing)', 'Field left blank and treated as missing.'))
    # rule 4 checks, in the rule's priority order
    reasons = []
    missing = [k for k in ('batch', 'test_date', 'purity', 'size') if not final[k]]
    if missing: reasons.append('missing field: ' + ', '.join(m.replace('_', ' ') for m in missing))
    if final['size'] and float(final['size']) != float(p['Size_mg']):
        reasons.append(f"size conflict: COA declares {final['size']} mg, sheet lists {p['Size_mg']} mg; held until price is confirmed")
    if final['purity'] and float(final['purity']) < 98.0:
        reasons.append(f"purity below 98.0 % ({final['purity']} %)")
    th, ob = float(c['theoretical_mass_da']), float(c['observed_mass_da'])
    if abs(ob - th) > 1.0 + 1e-9:
        reasons.append(f"identity failed: observed {ob} Da vs theoretical {th} Da (diff {abs(ob-th):.1f} Da > 1.0 Da)")
    if final['test_date'] and date.fromisoformat(final['test_date']) < CUTOFF:
        reasons.append(f"COA older than 12 months (tested {final['test_date']}, reference date 2026-09-30)")
    status = 'draft' if reasons else 'publish'
    reason = reasons[0] if reasons else 'all publish conditions met'
    if status == 'draft':
        extra = f" (other failing checks: {'; '.join(reasons[1:])})" if len(reasons) > 1 else ''
        issues.append((f"Draft: {reason}.{extra}", 'Rule 4' + {'missing':'a','size':'e','purity':'b','identity':'c','COA':'d'}[reason.split(' ')[0].rstrip(':')] + ' (first failing reason in rule-4 order)',
                       'Status set to draft; first failing reason written to status_reason.'))
    url = f"https://example-store.test/coa/{p['SKU'].lower()}-{final['batch'].lower()}/" if final['batch'] else ''
    rows.append({'SKU': p['SKU'], 'Name': p['Product'], 'Regular price': p['Price_USD'], 'Status': status,
                 'coa_batch': final['batch'], 'coa_test_date': final['test_date'], 'coa_purity': final['purity'],
                 'coa_size_mg': final['size'], 'coa_pdf': c['pdf_file'], 'coa_url': url, 'status_reason': reason})
    if issues: exc.append((p, c, status, issues))

with open('woocommerce_import.csv', 'w', newline='') as fh:
    w = csv.DictWriter(fh, list(rows[0].keys())); w.writeheader(); w.writerows(rows)

# ---- library
pub = sorted([r for r in rows if r['Status'] == 'publish'], key=lambda r: r['coa_test_date'], reverse=True)
mean = sum(float(r['coa_purity']) for r in pub) / len(pub)
trs = '\n'.join(f"""      <tr><td>{html.escape(r['Name'])}</td><td>{r['coa_batch']}</td><td>{r['coa_test_date']}</td><td>{float(r['coa_purity']):.1f} %</td><td><a href="coa/{r['coa_pdf']}">{r['coa_pdf']}</a></td></tr>""" for r in pub)
open('coa_library.html', 'w').write(f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>COA Library</title>
<style>
  :root {{ --bg:#fff; --fg:#1d1d1f; --muted:#6b6b70; --line:#e3e3e8; --accent:#1a5fb4; }}
  @media (prefers-color-scheme: dark) {{ :root {{ --bg:#16161a; --fg:#ececf1; --muted:#9a9aa3; --line:#2e2e35; --accent:#78aeed; }} }}
  body {{ margin:0; padding:24px 16px; background:var(--bg); color:var(--fg); font:15px/1.5 system-ui,sans-serif; }}
  main {{ max-width:860px; margin:0 auto; }}
  .teaser {{ font-size:1.05rem; padding:12px 14px; border:1px solid var(--line); border-radius:8px; }}
  .wrap {{ overflow-x:auto; }}
  table {{ width:100%; border-collapse:collapse; margin-top:16px; }}
  th, td {{ text-align:left; padding:8px 10px; border-bottom:1px solid var(--line); white-space:nowrap; }}
  th {{ color:var(--muted); font-weight:600; }}
  a {{ color:var(--accent); }}
</style>
</head>
<body>
<main>
  <p class="teaser" id="teaser"><strong><span id="published-count">{len(pub)}</span> published COAs</strong> &middot; mean purity <strong><span id="mean-purity">{mean:.2f}</span> %</strong></p>
  <h1>Certificate of Analysis library</h1>
  <p>Published products only, newest test date first.</p>
  <div class="wrap">
  <table>
    <thead><tr><th>Product</th><th>Batch</th><th>Test date</th><th>Purity</th><th>COA PDF</th></tr></thead>
    <tbody>
{trs}
    </tbody>
  </table>
  </div>
</main>
</body>
</html>
""")

# ---- exceptions report
L = ['# Exceptions report', '',
     'Reference date: 2026-09-30. Covers every product where a value came from the sheet, the sheet and PDF disagree, more than one COA exists, or the product is a draft.', '',
     f"Clean publishes with no exceptions: {', '.join(r['SKU']+' '+r['Name'] for r in rows if r['SKU'] not in {e[0]['SKU'] for e in exc})}.", '',
     '| SKU | Product | COA used | Final status | Issue | Rule used | Action taken |', '|---|---|---|---|---|---|---|']
for p, c, status, issues in exc:
    for i, (iss, rule, act) in enumerate(issues):
        L.append(f"| {p['SKU']} | {p['Product']} | {c['pdf_file']} | {status} | {iss} | {rule} | {act} |")
open('exceptions_report.md', 'w').write('\n'.join(L) + '\n')
print(f"published={len(pub)} drafts={len(rows)-len(pub)} mean={mean:.4f}")
