# Exceptions report

Reference date: 2026-09-30. Covers every product where a value came from the sheet, the sheet and PDF disagree, more than one COA exists, or the product is a draft.

Clean publishes with no exceptions: P01 BPC-157, P06 Epitalon, P08 Semax, P10 Thymosin Alpha-1, P14 AOD-9604.

| SKU | Product | COA used | Final status | Issue | Rule used | Action taken |
|---|---|---|---|---|---|---|
| P02 | TB-500 | MAL-26-3471.pdf | publish | PDF leaves test date blank; sheet has 2026-03-10. | Rule 3 (blank on PDF, use sheet) | Used sheet value 2026-03-10, recorded as "from sheet". |
| P03 | GHK-Cu | MAL-26-7468.pdf | draft | Batch is blank on both the PDF and the sheet. | Rule 3 (both blank, field missing) | Field left blank and treated as missing. |
| P03 | GHK-Cu | MAL-26-7468.pdf | draft | Draft: missing field: batch. | Rule 4a (first failing reason in rule-4 order) | Status set to draft; first failing reason written to status_reason. |
| P04 | Ipamorelin | MAL-26-1791.pdf | publish | Sheet and PDF disagree on batch: sheet PP-2604-012, PDF PP-2604-021. | Rule 1 (PDF overrides sheet) | Used PDF value PP-2604-021. |
| P05 | CJC-1295 (no DAC) | MAL-26-2186.pdf | publish | Sheet and PDF disagree on purity: sheet 99.1, PDF 98.2. | Rule 1 (PDF overrides sheet) | Used PDF value 98.2. |
| P07 | Selank | MAL-26-6991.pdf | publish | More than one COA exists: MAL-26-2542.pdf, MAL-26-6991.pdf. | Rule 2 (newest test date wins) | Used MAL-26-6991.pdf (re-analysis, tested 2026-06-20); ignored MAL-26-2542.pdf (first analysis, tested 2026-01-12). |
| P07 | Selank | MAL-26-6991.pdf | publish | Sheet and PDF disagree on test date: sheet 2026-01-12, PDF 2026-06-20. | Rule 1 (PDF overrides sheet) | Used PDF value 2026-06-20. |
| P07 | Selank | MAL-26-6991.pdf | publish | Sheet and PDF disagree on purity: sheet 98.9, PDF 99.3. | Rule 1 (PDF overrides sheet) | Used PDF value 99.3. |
| P09 | MOTS-c | MAL-26-9313.pdf | draft | Sheet and PDF disagree on purity: sheet 98.5, PDF 97.4. | Rule 1 (PDF overrides sheet) | Used PDF value 97.4. |
| P09 | MOTS-c | MAL-26-9313.pdf | draft | Draft: purity below 98.0 % (97.4 %). | Rule 4b (first failing reason in rule-4 order) | Status set to draft; first failing reason written to status_reason. |
| P11 | PT-141 | MAL-26-1614.pdf | draft | Draft: COA older than 12 months (tested 2025-08-14, reference date 2026-09-30). | Rule 4d (first failing reason in rule-4 order) | Status set to draft; first failing reason written to status_reason. |
| P12 | DSIP | MAL-26-2408.pdf | draft | Draft: identity failed: observed 851.3 Da vs theoretical 848.8 Da (diff 2.5 Da > 1.0 Da). | Rule 4c (first failing reason in rule-4 order) | Status set to draft; first failing reason written to status_reason. |
| P13 | KPV | MAL-26-8104.pdf | draft | Sheet and PDF disagree on size: sheet 5 mg, PDF declares 10 mg. | Rule 1 (PDF overrides sheet) and Rule 4e (size conflict) | Used PDF value 10 mg for coa_size_mg; product held as draft until the price is confirmed. |
| P13 | KPV | MAL-26-8104.pdf | draft | Draft: size conflict: COA declares 10 mg, sheet lists 5 mg; held until price is confirmed. | Rule 4e (first failing reason in rule-4 order) | Status set to draft; first failing reason written to status_reason. |
