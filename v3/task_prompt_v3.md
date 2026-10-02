You are helping me prepare product data for a WooCommerce store that sells research peptides. Each product must show a verified Certificate of Analysis (COA) before it can go live. Work in the folder that contains products.csv, price_list.csv, rules.md and the coa/ folder (41 COA PDFs from three labs).

## Inputs
- products.csv: the shop's product sheet (30 products). It may contain errors.
- price_list.csv: the official price list by product and size.
- coa/*.pdf: lab COA documents. Filenames are report IDs, so match each result to its product from the content of the PDF. Ten PDFs are scans with no text layer (some rotated, some low resolution). Some PDFs list several lots or several products. Some COAs span two pages. Labs use different names for the same peptide, and their date and number formats differ.
- rules.md: the store's publishing rules. Follow it exactly. Do not invent values that are not in the PDFs, the sheet, the price list or the rules.

## What to do
1. Before you decide anything, write reading_notes.md: one entry per PDF with the lab, number of pages, whether it is a scan (and its orientation and legibility), every result line it contains, the product each line matches and why (name, amount, mass), and anything unusual (stamps, revisions, blank fields, ambiguous dates).
2. Extract every result line into coa_extracted.csv: pdf_file, lab, product_as_printed, matched_sku, declared_amount_mg, batch, test_date (YYYY-MM-DD), purity, theoretical_mass, observed_mass, notes. One row per result line, including lines you will later ignore.
3. Reconcile the COA data with products.csv and price_list.csv using the rules. Decide the final COA, batch, test date, purity, size and price for each product, then its status and status reason.
4. Build these deliverables from your decisions:
   - woocommerce_import.csv: 30 rows, columns SKU, Name, Regular price, Status, coa_batch, coa_test_date, coa_purity, coa_size_mg, coa_pdf, coa_url, status_reason.
   - price_changes.csv: SKU, Name, old_price, new_price, reason.
   - coa_library.html: published products only, in the order the rules give, with columns product, batch, test date, purity and a link to the PDF in coa/. Put the homepage teaser line at the top.
   - coa_feed.json: the same products, order and values as the library, plus sku, coa_url and the teaser numbers.
   - retest_schedule.csv: SKU, Name, test_date, retest_due, days_remaining, due_soon.
   - featured_products.md: the 3 featured products with SKU, name, purity, test date and one sentence on why each was chosen.
   - supplier_scorecard.csv: one row per lab, with the columns defined in the rules.
   - exceptions_report.md: every product that is not a clean publish, and every product where a value came from the sheet, where the sheet and COA disagree, where the price changed, or where more than one COA exists or a COA was ignored. Also list every COA result that matched no product. For each, give the product or file, the issue, the rule used and the action taken.
   - client_email.md: the email to the client as the rules describe.
5. Verify your own work. Open every scanned PDF again as an image and confirm the values you recorded for it. Compare every value in woocommerce_import.csv against the PDFs, the sheet, the price list and the rules. Check that the deliverables agree with each other: counts, mean purity, library and feed order, retest dates, featured choices, scorecard totals, the price changes and the email totals. If you find a mismatch, fix the upstream decision, rebuild every deliverable that depends on it, and check again. Write verification_log.md listing each check, the mismatches you found, what you changed, and the result of the final re-check.

## Acceptance checks (how I will judge the result)
- reading_notes.md covers all 41 PDFs, and every result line in it appears in coa_extracted.csv.
- woocommerce_import.csv has exactly 30 rows, and every status and reason follows rules.md.
- Every batch, test date, purity, size and price matches the rules applied to the PDFs, sheet and price list, after unit, decimal and date-format conversion.
- Every coa_url follows the URL rule and is blank only where the rules say so.
- coa_library.html and coa_feed.json contain only published products, in the same correct order, and their teaser numbers match the import file.
- price_changes.csv lists every price that changed, and only those.
- retest_schedule.csv, featured_products.md and supplier_scorecard.csv follow the rules using the final data.
- client_email.md covers every draft in SKU order with the correct reason and action, and the totals are correct.
- exceptions_report.md accounts for every product that is not a clean publish and every ignored or unmatched COA result.
- verification_log.md shows real comparisons, and the final files contain no unresolved mismatch.
- No value appears that is not supported by a PDF, the sheet, the price list or the rules.

When finished, give me a short summary: how many products are published and how many are drafts, the mean purity of the published ones, the featured products, the price changes, and the total USD value of the draft products.
