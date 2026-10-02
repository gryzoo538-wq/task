# Verification log

Reference date: 2026-09-30, so a COA passes rule 4d only if it was tested on or after 2025-09-30.
Re-run with: `python3 scripts/build_coa.py && python3 scripts/verify_coa.py`

## How the checks work

`scripts/verify_coa.py` is separate from the build. It does **not** reuse the build's extraction:

- It re-reads all 15 PDFs with a different extractor. The build used `pdftotext`; the verifier uses `pypdf`.
- It applies `rules.md` again from scratch.
- It compares that result to every deliverable.

## Checks run (final run: 116 checks, 0 failed)

| # | Check | Result |
|---|---|---|
| 1 | 15 PDFs in `coa/`; `coa_extracted.csv` has one row per PDF | PASS (15/15) |
| 2 | Each PDF's 7 extracted fields (product, declared amount, batch, test date, purity, theoretical mass, observed mass) match the pypdf re-read | PASS (15/15 PDFs, 105 values) |
| 3 | `woocommerce_import.csv` has exactly 14 rows, the required columns, and the same SKUs as the sheet | PASS |
| 4 | For each SKU, the COA chosen, batch, test date, purity, size, status and URL equal the values recomputed independently from the PDFs, the sheet and the rules | PASS (14/14) |
| 5 | For each SKU, `status_reason` is the first failing reason in rule-4 order, or "all publish conditions met" | PASS (14/14) |
| 6 | Name and price come unchanged from the sheet | PASS (14/14) |
| 7 | Each batch matches `PP-YYMM-NNN` and is kept exactly as printed (rule 8) | PASS (13 batches; P03 has none) |
| 8 | Each URL is `https://example-store.test/coa/<sku>-<batch>/` in lowercase, and blank only when the batch is missing (rule 5) | PASS (13 URLs; only P03 blank) |
| 9 | Library rows = published rows in the import (9 = 9), and only published products appear | PASS |
| 10 | Library order is newest test date first: 2026-08-05 > 07-21 > 07-02 > 06-20 > 06-18 > 04-15 > 03-24 > 03-10 > 02-27 | PASS |
| 11 | Each library row's product, batch, date, purity and PDF link equals its import row, and the linked file exists in `coa/` | PASS (9/9) |
| 12 | Teaser count (9) equals the number of `publish` rows in the import | PASS |
| 13 | Teaser mean purity (99.10) equals the mean of the import's published purities: 891.9 / 9 = 99.1000 | PASS |
| 14 | The exceptions report lists exactly the products that are not clean publishes: P02, P03, P04, P05, P07, P09, P11, P12, P13 | PASS |
| 15 | Each draft's reason appears in the report; P02's test date is marked "from sheet" | PASS |
| 16 | Every sheet/PDF disagreement has its own report row (P04 batch, P05 purity, P07 test date and purity, P09 purity, P13 size) | PASS (6/6), after the fix below |

## Key comparisons (PDF value vs sheet value)

| SKU | COA used | Field checked | PDF | Sheet | Outcome |
|---|---|---|---|---|---|
| P02 | MAL-26-3471 | test date | *(blank)* | 2026-03-10 | Sheet value used (rule 3) → publish |
| P03 | MAL-26-7468 | batch | *(blank)* | *(blank)* | Missing → draft, URL blank |
| P04 | MAL-26-1791 | batch | PP-2604-021 | PP-2604-012 | PDF wins → URL uses `pp-2604-021` |
| P05 | MAL-26-2186 | purity | 98.2 | 99.1 | PDF wins; still ≥ 98.0 → publish |
| P07 | MAL-26-6991 vs MAL-26-2542 | test date | 2026-06-20 vs 2026-01-12 | 2026-01-12 | Newer re-analysis used (rule 2): purity 99.3, mass difference 0.2 Da |
| P09 | MAL-26-9313 | purity | 97.4 | 98.5 | 97.4 < 98.0 → draft |
| P11 | MAL-26-1614 | test date | 2025-08-14 | 2025-08-14 | Before 2025-09-30 → draft |
| P12 | MAL-26-2408 | mass | 851.3 vs theoretical 848.8 | n/a | 2.5 Da > 1.0 Da → draft |
| P13 | MAL-26-8104 | size | 10 mg | 5 mg | Size conflict → draft (price to be confirmed) |
| All other PDFs | n/a | mass | | | Largest difference is 0.6 Da (P10), within 1.0 Da |

## Mismatches found and changes made

1. **Exceptions report: P13 size disagreement had no row of its own.** The first build only mentioned the sheet/PDF size difference (5 mg vs 10 mg) inside P13's "Draft: size conflict" line. Every other disagreement gets a separate "Sheet and PDF disagree" row, so this one was not recorded the same way.
   - **Fix:** changed the reconciliation step to add a disagreement row for size too (rules 1 and 4e). I rebuilt every deliverable and added check 16 to the verifier.
   - **Effect:** `woocommerce_import.csv`, `coa_library.html` and `coa_extracted.csv` came out unchanged (P13 was already a draft with `coa_size_mg` = 10). Only `exceptions_report.md` gained one row.

The first verification run (110 checks) found no value mismatches in the import file or the library.

## Final re-check

116 of 116 checks pass. The four deliverables agree with each other and with the PDFs and `rules.md`:

- **Published (9):** P01, P02, P04, P05, P06, P07, P08, P10, P14
- **Draft (5):** P03, P09, P11, P12, P13
- **Mean purity of published products:** 99.10 %
