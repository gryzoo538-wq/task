# Independent re-check: re-extracts PDFs with pypdf, re-applies rules.md from scratch,
# then compares against every deliverable. Prints one line per check.
import csv, glob, os, re, html.parser
from datetime import date
import pypdf
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
results = []
def check(name, ok, detail=''):
    results.append((name, ok, detail)); print(('PASS' if ok else 'FAIL'), '|', name, '|', detail)

LABELS = ['Product', 'Declared amount', 'Batch / lot number', 'Test date', 'Method',
          'Purity (HPLC)', 'Identity: theoretical mass', 'Identity: observed mass (MS)']
def parse(path):
    lines = [l.strip() for l in pypdf.PdfReader(path).pages[0].extract_text().splitlines()]
    out = {}
    for lab in LABELS:
        i = lines.index(lab); nxt = lines[i + 1]
        out[lab] = '' if nxt in LABELS or nxt in ('Appearance',) else nxt
    n = lambda s: re.match(r'[\d.]+', s).group(0) if s else ''
    return dict(product=out['Product'], size=n(out['Declared amount']), batch=out['Batch / lot number'],
                date=out['Test date'], purity=n(out['Purity (HPLC)']),
                th=float(n(out['Identity: theoretical mass'])), ob=float(n(out['Identity: observed mass (MS)'])))
pdfs = {os.path.basename(f): parse(f) for f in sorted(glob.glob('coa/*.pdf'))}
check('15 COA PDFs present in coa/', len(pdfs) == 15, f'{len(pdfs)} found')

# coa_extracted.csv vs independent extraction
ext = {r['pdf_file']: r for r in csv.DictReader(open('coa_extracted.csv'))}
check('coa_extracted.csv has one row per PDF', set(ext) == set(pdfs), f'{len(ext)} rows')
for f, p in pdfs.items():
    e = ext[f]
    diffs = [k for k, a, b in [('product', e['product'], p['product']), ('size', e['declared_amount_mg'], p['size']),
             ('batch', e['batch'], p['batch']), ('date', e['test_date'], p['date']), ('purity', e['purity_pct'], p['purity']),
             ('th', float(e['theoretical_mass_da']), p['th']), ('ob', float(e['observed_mass_da']), p['ob'])] if a != b]
    check(f'extract {f} matches pypdf re-read', not diffs, ','.join(diffs) or 'all 7 fields equal')

# expected values derived from scratch
sheet = {r['SKU']: r for r in csv.DictReader(open('products.csv'))}
imp = list(csv.DictReader(open('woocommerce_import.csv')))
check('import has exactly 14 rows', len(imp) == 14, f'{len(imp)} rows')
check('import columns', list(imp[0].keys()) == ['SKU','Name','Regular price','Status','coa_batch','coa_test_date','coa_purity','coa_size_mg','coa_pdf','coa_url','status_reason'])
check('import SKUs match sheet', [r['SKU'] for r in imp] == list(sheet))
expected = {}
for sku, s in sheet.items():
    cands = sorted([(f, p) for f, p in pdfs.items() if p['product'] == s['Product']], key=lambda x: x[1]['date'], reverse=True)
    f, p = cands[0]
    batch = p['batch'] or s['Batch_Listed']; d = p['date'] or s['Test_Date_Listed']
    pur = p['purity'] or s['Purity_Listed_pct']; size = p['size'] or s['Size_mg']
    fails = []
    if not (batch and d and pur and size): fails.append('missing field')
    if size and float(size) != float(s['Size_mg']): fails.append('size conflict')
    if pur and float(pur) < 98.0: fails.append('purity below 98.0')
    if abs(p['ob'] - p['th']) > 1.0: fails.append('identity failed')
    if d and date.fromisoformat(d) < date(2025, 9, 30): fails.append('COA older than 12 months')
    expected[sku] = dict(pdf=f, n=len(cands), batch=batch, date=d, purity=pur, size=size,
                         status='draft' if fails else 'publish', reason=fails[0] if fails else '',
                         url=f"https://example-store.test/coa/{sku.lower()}-{batch.lower()}/" if batch else '')
for r in imp:
    e, s = expected[r['SKU']], sheet[r['SKU']]
    got = (r['coa_pdf'], r['coa_batch'], r['coa_test_date'], r['coa_purity'], r['coa_size_mg'], r['Status'], r['coa_url'])
    exp = (e['pdf'], e['batch'], e['date'], e['purity'], e['size'], e['status'], e['url'])
    check(f"{r['SKU']} pdf/batch/date/purity/size/status/url", got == exp, f'got {got}' if got != exp else f"{r['Status']}, {r['coa_pdf']}")
    reason_ok = r['status_reason'].startswith(e['reason']) if e['reason'] else r['status_reason'] == 'all publish conditions met'
    check(f"{r['SKU']} status_reason follows rule-4 order", reason_ok, r['status_reason'])
    check(f"{r['SKU']} name & price from sheet", (r['Name'], r['Regular price']) == (s['Product'], s['Price_USD']))
    if r['coa_batch']:
        check(f"{r['SKU']} batch matches PP-YYMM-NNN", bool(re.fullmatch(r'PP-\d{4}-\d{3}', r['coa_batch'])), r['coa_batch'])
    check(f"{r['SKU']} URL blank only when batch missing", (r['coa_url'] == '') == (r['coa_batch'] == ''))

# library vs import
class P(html.parser.HTMLParser):
    def __init__(s): super().__init__(); s.rows=[]; s.cur=None; s.cell=None; s.links=[]; s.spans={}; s.sid=None
    def handle_starttag(s, t, a):
        a = dict(a)
        if t == 'tr': s.cur = []
        if t == 'td': s.cell = ''
        if t == 'a' and s.cur is not None: s.links.append(a['href'])
        if t == 'span': s.sid = a.get('id')
    def handle_endtag(s, t):
        if t == 'td': s.cur.append(s.cell); s.cell = None
        if t == 'tr' and s.cur: s.rows.append(s.cur)
        if t == 'tr': s.cur = None
        if t == 'span': s.sid = None
    def handle_data(s, d):
        if s.cell is not None: s.cell += d
        if s.sid: s.spans[s.sid] = d
hp = P(); hp.feed(open('coa_library.html').read())
pub = sorted([r for r in imp if r['Status'] == 'publish'], key=lambda r: r['coa_test_date'], reverse=True)
check('library row count == published count in import', len(hp.rows) == len(pub), f'{len(hp.rows)} vs {len(pub)}')
check('library lists only published products', {r[0] for r in hp.rows} == {r['Name'] for r in pub})
lib_dates = [r[2] for r in hp.rows]
check('library order newest test date first', lib_dates == sorted(lib_dates, reverse=True), ' > '.join(lib_dates))
for row, r, link in zip(hp.rows, pub, hp.links):
    ok = (row[0], row[1], row[2], row[3].replace(' %', ''), link) == (r['Name'], r['coa_batch'], r['coa_test_date'], r['coa_purity'], 'coa/' + r['coa_pdf'])
    check(f"library row {r['Name']} == import row", ok and os.path.exists(link), link)
mean = sum(float(r['coa_purity']) for r in pub) / len(pub)
check('teaser count == import publish count', hp.spans.get('published-count') == str(len(pub)), hp.spans.get('published-count'))
check('teaser mean purity == import mean (2 dp)', hp.spans.get('mean-purity') == f'{mean:.2f}', f"{hp.spans.get('mean-purity')} vs {mean:.4f}")

# exceptions report coverage
rep = open('exceptions_report.md').read()
rep_rows = [l.split(' | ') for l in rep.splitlines() if re.match(r'\| P\d\d ', l)]
in_rep = {x[0].strip('| ') for x in rep_rows}
need = set()
for sku, s in sheet.items():
    e = expected[sku]; p = pdfs[e['pdf']]
    from_sheet = any(not p[k] for k in ('batch', 'date', 'purity', 'size'))
    disagree = any(sv and pv and (float(pv) != float(sv) if k in ('purity','size') else pv != sv)
                   for k, pv, sv in [('batch', p['batch'], s['Batch_Listed']), ('date', p['date'], s['Test_Date_Listed']),
                                     ('purity', p['purity'], s['Purity_Listed_pct']), ('size', p['size'], s['Size_mg'])])
    if from_sheet or disagree or e['n'] > 1 or e['status'] == 'draft': need.add(sku)
check('exceptions report covers exactly the non-clean products', in_rep == need, f'need {sorted(need)}; report {sorted(in_rep)}')
for sku in need:
    if expected[sku]['status'] == 'draft':
        check(f'{sku} draft reason in report', any(x[0].strip('| ') == sku and expected[sku]['reason'] in x[4] for x in rep_rows))
for sku, s in sheet.items():
    p = pdfs[expected[sku]['pdf']]
    for k, pv, sv, word in [('batch', p['batch'], s['Batch_Listed'], 'batch'), ('date', p['date'], s['Test_Date_Listed'], 'test date'),
                            ('purity', p['purity'], s['Purity_Listed_pct'], 'purity'), ('size', p['size'], s['Size_mg'], 'size')]:
        if sv and pv and (float(pv) != float(sv) if k in ('purity','size') else pv != sv):
            check(f'{sku} disagreement on {word} has its own report row', any(x[0].strip('| ') == sku and f'disagree on {word}' in x[4] for x in rep_rows), f'sheet {sv} vs PDF {pv}')
check('P02 test date recorded "from sheet"', any(x[0].strip('| ') == 'P02' and 'from sheet' in x[6] for x in rep_rows))

fails = [r for r in results if not r[1]]
print(f'\nTOTAL {len(results)} checks, {len(fails)} failed')
