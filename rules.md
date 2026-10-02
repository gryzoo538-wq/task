# Store rules for COA publishing

Reference date for all date checks: 2026-09-30.

1. Source of truth. Values printed on a COA PDF override the product sheet (products.csv) for batch, test date, purity and declared amount (size).
2. Several COAs for one product. Use the COA with the newest test date.
3. Blank field on the PDF. If the PDF leaves a field blank and the sheet has a value, use the sheet value and record it as "from sheet" in the exceptions report. If both are blank, the field is missing.
4. Publish conditions. A product gets status "publish" only if ALL are true:
   a. all four fields (batch, test date, purity, size) are known (rule 3 allowed);
   b. purity is 98.0 % or higher;
   c. identity passes: observed mass is within 1.0 Da of theoretical mass (both printed on the PDF);
   d. the test date is no more than 12 months before the reference date;
   e. the declared amount on the PDF equals the size on the sheet. If it differs, the price may be wrong, so the product is held until the price is confirmed.
   Otherwise the status is "draft" and the first failing reason is recorded in status_reason.
   Order of reasons when more than one applies: missing field, size conflict, purity below 98.0, identity failed, COA older than 12 months.
5. COA page URL (published and draft alike, when a batch is known): https://example-store.test/coa/<sku lowercase>-<batch lowercase>/
   If the batch is missing, leave the URL blank.
6. COA library lists published products only, newest test date first.
7. Homepage teaser shows: number of published COAs, and the mean purity of published products rounded to 2 decimals.
8. Batch numbers use the pattern PP-YYMM-NNN. Keep them exactly as printed on the COA.
