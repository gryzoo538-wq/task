I run WooCommerce builds for clients. This client sells research peptides, and every product must show a verified Certificate of Analysis (COA) before it can go live. I need the full job done: the product data, a small WordPress plugin that displays it, and the client's follow-up changes. Work in the folder that contains products.csv, price_list.csv, rules.md, coa/ (41 COA PDFs from three labs) and inbox/ (three client emails with their attachments).

## Inputs
- products.csv: the shop's product sheet (30 products). It may contain errors.
- price_list.csv: the official price list by product and size.
- coa/*.pdf: lab COAs. Filenames are report IDs, so match each result to its product from the PDF content. 28 of them are scans with no text layer (some rotated, some low resolution). No OCR software is installed, so you must look at each scan yourself. Some PDFs list several lots or products, and the Coastal COAs span two pages. Labs use different names for the same peptide and different date and number formats.
- rules.md: the store's publishing rules. Follow it exactly. Do not invent values that are not in the PDFs, sheet, price list, rules or emails.
- inbox/: three emails from the client, dated after the first delivery, plus their attachments. Do not open inbox/ until Part 3.

## Part 1: First delivery (save everything in output/phase1/)
1. Before deciding anything, write reading_notes.md: one entry per PDF with the lab, page count, whether it is a scan (orientation, legibility), every result line it contains, the product each line matches and why (name, amount, mass), and anything unusual (stamps, revisions, blank fields, ambiguous dates).
2. Extract every result line into coa_extracted.csv: pdf_file, lab, product_as_printed, matched_sku, declared_amount_mg, batch, test_date (YYYY-MM-DD), purity, theoretical_mass, observed_mass, notes. Include lines you later ignore.
3. Reconcile the COAs with products.csv and price_list.csv using the rules. Decide each product's final COA, batch, test date, purity, size, price, status and status reason.
4. Build these deliverables:
   - woocommerce_import.csv: 30 rows, columns SKU, Name, Regular price, Status, coa_batch, coa_test_date, coa_purity, coa_size_mg, coa_pdf, coa_url, status_reason.
   - price_changes.csv: SKU, Name, old_price, new_price, reason.
   - coa_library.html: published products in the order the rules give (product, batch, test date, purity, link to the PDF in coa/), with the homepage teaser at the top.
   - coa_feed.json: the same products, order and values as the library, plus sku, coa_url and the teaser numbers.
   - retest_schedule.csv: SKU, Name, test_date, retest_due, days_remaining, due_soon.
   - featured_products.md: the 3 featured products with SKU, name, purity, test date and one sentence on why each was chosen.
   - supplier_scorecard.csv: one row per lab, with the columns the rules define.
   - exceptions_report.md: every product that is not a clean publish, and every product where a value came from the sheet, the sheet and COA disagree, the price changed, or more than one COA exists or a COA was ignored. Also list every COA result that matched no product. For each: product or file, issue, rule used, action taken.
   - client_email.md: the email to the client as the rules describe.

## Part 2: WordPress plugin (in plugin/peptide-coa/)
Write a WordPress plugin that loads the import file into WooCommerce and displays the COAs:
- peptide-coa.php with a valid plugin header.
- An importer class that reads woocommerce_import.csv, validates every row (batch pattern, date format, URL rule, allowed status and reason values, price format), and stores the COA columns as product meta: _coa_batch, _coa_test_date, _coa_purity, _coa_size_mg, _coa_pdf, _coa_url, _coa_status_reason. Invalid rows are reported, not imported.
- A "Certificate of Analysis" product tab (woocommerce_product_tabs filter). Published products show the COA values and a link to the PDF. Drafts show "COA pending" and no values.
- A [coa_library] shortcode that renders the library from the imported data: published only, in rule order, with the teaser.
- tests/run_tests.php, runnable with `php tests/run_tests.php <output folder>` without WordPress installed (stub only the WordPress functions you use). It must check that all 30 rows import with no validation errors; that the shortcode lists the same SKUs in the same order as coa_library.html; that the teaser matches coa_feed.json; that every draft's tab shows "COA pending"; and that a deliberately broken row (bad batch, bad date, wrong URL) is rejected.
Run the tests against output/phase1/ and fix the plugin or the data until they pass.

## Part 3: Client follow-ups (final state in output/final/)
Now read the inbox/ emails and handle them in date order. Each email changes facts, so after each one, update the affected decisions and every deliverable that depends on them, and write a short reply (reply_01.md, reply_02.md, reply_03.md) telling the client exactly what changed because of that email.
After the last email:
- output/final/ must contain the complete, current version of every Part 1 deliverable.
- Write changes_report.md: every product field that differs between output/phase1/woocommerce_import.csv and output/final/woocommerce_import.csv, with the email that caused it, plus the changes to the library, retest schedule, featured products, scorecard and email totals.
- Run the plugin tests again against output/final/ and make them pass.

## Verification
Before finishing, open every scanned PDF again as an image and confirm the values you recorded. Compare every value in both import files against the PDFs, sheet, price list, rules and emails. Check that the deliverables in each folder agree with each other (counts, mean purity, library and feed order, retest dates, featured choices, scorecard totals, price changes, email totals). If you find a mismatch, fix the upstream decision, rebuild everything that depends on it and check again. Write verification_log.md listing each check, the mismatches found, what you changed, the final re-check result and the test output.

## Acceptance checks (how I will judge the result)
- reading_notes.md covers all 41 PDFs, and every result line in it appears in coa_extracted.csv.
- Both import files have exactly 30 rows, and every status, reason, batch, test date, purity, size, price and URL follows the rules (and, for final, the emails) after unit, decimal and date-format conversion.
- The library and feed in each folder contain only published products, in the same correct order, with teaser numbers that match the import file.
- price_changes.csv, retest_schedule.csv, featured_products.md and supplier_scorecard.csv follow the rules using that folder's data.
- client_email.md covers every draft in SKU order with the correct reason, action and totals.
- exceptions_report.md accounts for every non-clean product and every ignored or unmatched COA result.
- The plugin passes its own tests against both folders, and the tests really exercise the importer, tab and shortcode.
- reply_01–03.md and changes_report.md match the real differences between phase 1 and final.
- verification_log.md shows real comparisons, and no unresolved mismatch remains.
- No value appears that is not supported by a PDF, the sheet, the price list, the rules or an email.

When finished, give me a short summary: published and draft counts and mean purity for phase 1 and final, the featured products, the price changes, the total USD value of final drafts, what each email changed, and the plugin test results.
