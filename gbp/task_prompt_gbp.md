I build review automations for small businesses. My client, Lantern & Loaf Bakery Café, has three locations. I need this month's Google review work done end to end, plus the automation that will run it every month. Work in the folder that contains playbook.md, locations.csv, staff.csv, august_report.json, mock_gbp/, old_town_screenshots/ and owner_update/.

## Inputs
- mock_gbp/: a local mock of the Google Business Profile API with the client's reply gateway. Start it with `python3 mock_gbp/server.py --phase 1` and read mock_gbp/README.md for the endpoints. Treat it as a black box: use it only over HTTP, and do not read or edit its other files. It paginates, rate-limits writes, rejects replies that break house rules, and some listed reviews may already have been removed.
- old_town_screenshots/: the Old Town location is not connected to the API. Its reviews exist only in these 6 phone screenshots (2 reviews each). No OCR software is installed, so you must look at each image yourself.
- playbook.md: the client's rules for routing, replies, flags and the monthly report. Follow it exactly.
- locations.csv, staff.csv: managers, connection status, and who may be named in public.
- august_report.json: last month's report from the previous contractor.
- owner_update/: the owner's response, which arrives after your first delivery. Do not open owner_update/ until Part 4.

## Part 1: Intake (output/phase1/)
1. Fetch every review for every connected location through the API, following pagination. Read every screenshot. Write review_inventory.csv with one row per review: our_id (M01…, R01…, O01…, numbered by location in createTime order), source (api/screenshot), location, review_id (API id, or blank), reviewer, stars, create_date, update_date, text, existing_reply, existing_reply_date.
2. Write triage_notes.md: one entry per review with the category under playbook section 2, the reason, any staff names mentioned and whether each may be named, the language, and anything unusual (edited after reply, wrong business, other location, conflict of interest, star-only, existing reply that breaks the rules).
3. Write decisions.csv: our_id, location, category, flag_priority, issue, reply_needed, notes.

## Part 2: Automation (automation/)
Build a small Python package that the client can run every month:
- gbp_client.py: an API client with auth, full pagination, retry on 429 that honours Retry-After, and clear errors for 400, 404 and 409.
- reply_rules.py: a local validator implementing playbook section 4 (name rule, staff consent from staff.csv, no compensation offers, no contact details, location name and sign-off, length, uniqueness across all replies) so that drafts are checked before they are sent.
- post_replies.py: posts approved replies from a CSV through the client, records every attempt and result in a post log, and never posts for Old Town.
- build_report.py: builds the monthly report from decisions.csv, the inventory and the live API state, under playbook section 5.
- tests/ (unittest, run with `python3 -m unittest discover automation/tests`): validator cases for every rule, a pagination test, a 429-retry test and a report-math test. Make them pass.

## Part 3: First delivery (output/phase1/)
1. Draft every reply needed (replies.csv: our_id, location, reply_text, char_count, language, names_used). Run every draft through reply_rules.py, and fix them until they all pass.
2. Post the replies for Midtown and Riverside with post_replies.py. Handle every API rejection. If the gateway rejects a reply, fix the reply and re-post. If a review returns 404, change its category to deleted. Correct our existing replies where playbook rule 1 requires it. Save post_log.csv.
3. Write old_town_replies.md: the Old Town replies for the owner to post by hand, plus any existing Old Town replies to correct.
4. Write owner_digest.md: urgent items first, with the reason and the call-back deadline; then flags by priority; then removal requests (also as removal_requests.csv with the reason under the playbook); then reply corrections made.
5. Build the September report with build_report.py: report.json, plus report.html containing the per-location table and an inline SVG bar chart of star distribution by location. Include the deleted reviews list, the reply corrections, and the August comparison against august_report.json with an explanation of any difference.
6. Reconcile: fetch the live API state again and confirm that every reply in post_log.csv is actually visible on the right review, and that every number in report.json can be traced to individual rows in decisions.csv.

## Part 4: Owner update (output/final/)
Now open owner_update/. Stop the server and restart it with `--phase 2` (posted replies are kept). Re-fetch everything, and work out exactly what changed in the API since phase 1: new reviews, edited reviews, reviews that disappeared. Apply the owner's decisions and the staff change under the playbook, including section 6. Draft, validate and post the new and corrected replies, and edit any of our posted replies that now break the rules. Then produce the complete final set in output/final/ (inventory, triage notes, decisions, replies, post log, Old Town replies, owner digest, removal requests, report.json, report.html), plus:
- changes_report.md: every review whose category, stars, text, reply or report treatment changed between phase 1 and final, with the cause; and every report number that changed, with old and new values.
- owner_reply.md: a short email to the owner confirming what was done and what still needs her.

## Verification
Before finishing, look at every screenshot again and confirm the values in your inventory. Fetch the live API state and compare every review and reply with your final files. Check that each report number equals the count you get from decisions.csv, both by location and in total, and that the HTML and JSON agree. Run the unit tests again. If you find a mismatch, fix the upstream decision, rebuild everything that depends on it and check again. Write verification_log.md listing each check, the mismatches found, what you changed, and the final results (including the test output).

## Acceptance checks (how I will judge the result)
- The inventory covers every review from the API (all pages) and all 12 screenshot reviews, with correct values.
- Every category follows playbook section 2 (and, for final, sections 1 and 6 with the owner's decisions and the API changes).
- Every reply passes playbook section 4. Staff are named only when allowed, Spanish reviews get Spanish replies, and no compensation or contact details appear.
- The live API shows exactly the replies in the final post log, with no rule-breaking reply left posted.
- report.json and report.html in each folder match decisions.csv exactly, per location and in total, under playbook section 5. The August comparison is correct and explained.
- The automation tests pass and really exercise pagination, the 429 retry, the validator rules and the report math.
- changes_report.md and owner_reply.md match the real differences between phase 1 and final.
- verification_log.md shows real comparisons, and no unresolved mismatch remains.

When finished, give me a short summary: the September numbers for phase 1 and final (new reviews, average rating, replied, urgent, removal requests, by location and in total), the urgent items, which replies the API rejected and how you fixed them, which existing replies you corrected, what changed in phase 2, and the test results.
