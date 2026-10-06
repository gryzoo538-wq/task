I'm a legal operations consultant. A small law firm, Hartwell & Osei LLP, is moving from Outlook to Box, and I need its exported mailbox filed into the new Box structure under the firm's filing rules. The firm reviews my work through its portal: the partner asks questions about the first pass, and the office sends memos one at a time as decisions are made. Work in the folder that contains mailbox/ (64 .eml files exported from Outlook), matters.csv, staff.csv, filing_rules.md, firm_portal/, INPUTS.md and MANIFEST.sha256.

## Inputs
- mailbox/*.eml: the exported emails. File names are Outlook IDs and tell you nothing. Many emails carry PDF attachments, and 15 of those are image-only scans (one is rotated). No OCR software is installed, so you must look at each scan yourself. Several emails can only be identified from their attachment.
- matters.csv: every client and matter, with folder names, responsible attorney, status, closed dates, litigation holds, ethical walls and restricted matters.
- staff.csv: firm staff.
- filing_rules.md: the firm's filing rules. Follow them exactly.
- firm_portal/: the firm's portal (a local mock). Start it with `python3 firm_portal/server.py` and read firm_portal/README.md. Treat it as a black box: use it over HTTP only, and do not read or edit its other files. It releases the partner's questions and the office memos only after your previous submission is accepted, and it rejects submissions that are malformed or internally inconsistent.
- INPUTS.md and MANIFEST.sha256: the list of input files and their checksums.

## Before you start: confirm the inputs
Check that you received the complete file set: run `sha256sum -c MANIFEST.sha256`, compare the folder with INPUTS.md, and confirm that all 64 emails parse and that their 24 PDF attachments open. If anything is missing, empty or unreadable, stop and tell me exactly what. Do not guess or work around missing client files.

## Part 1: First filing pass (output/phase1/)
1. Before filing anything, write triage_notes.md: one entry per email with the sender, recipients, date, Message-ID, a one-line summary of the body, what each attachment shows (for scans, what you saw), the category and matter you chose, and why. Note every judgment call: overlapping names, two-matter emails, walls, holds, closed matters, conflicts, duplicates.
2. Build the Box structure in output/phase1/box/ exactly as the rules describe. Copy each email under its new file name, extract the attachments of matter emails into Documents/, and create the cross-reference stubs. Every email must appear exactly once as a primary copy.
3. Produce these files in output/phase1/:
   - filing_log.csv: one row per email, with columns email_file, received (YYYY-MM-DD HH:MM), sender, subject, category, primary_matter, xref_matters, privilege, flags, box_path, attachments_saved.
   - wall_incidents.csv: email_file, received, screened_person, role (sender/to/cc), matter, action.
   - privilege_log.csv: every email filed in matter 1001-001 (under litigation hold) with privilege AC or WP, with columns date, from, to, cc, subject, privilege, description. The description must not reveal privileged content.
   - needs_review.md: every needs_review email with the reason, what the firm must decide, and who should decide it.
   - attorney_actions.md: for each attorney (and for IT and the ethics partner), the emails that need their action and why.
   - filing_summary.md: counts by category, by matter and by responsible attorney; the number of files in box/; and the open issues.

## Part 2: Checker, then first submission
1. Write tools/check_filing.py, which takes an output folder and validates it against the rules and the inputs. It must check that every mailbox email appears exactly once as a primary copy; that every box_path in filing_log.csv exists; that file names follow the naming rule; that restricted matters sit only under box/Restricted/; that every stub's "Filed at:" path exists and no stub crosses clients; that every extracted attachment exists and is named correctly; that hold duplicates are retained; and that the counts in filing_summary.md match the log. Run it against output/phase1/ and fix the data or the checker until it passes cleanly. Then copy output/phase1/ to a scratch folder, break three things in the copy (move a file, corrupt a stub, rename an attachment), and confirm the checker catches all three.
2. Submit phase 1 to the portal (stage `phase1`). If it is rejected, fix the cause in your data, rebuild, re-run the checker and resubmit. Keep each request and response in output/portal_log.md.

## Part 3: Partner review
The accepted submission releases the partner's questions to the portal inbox. Before answering each question, go back to the emails and attachments involved (open the scans again as images) and confirm your decision against the rules. If you find a mistake, fix it, rebuild output/phase1/, re-run the checker and say so in the answer. Write output/partner_answers.md, then submit the answers (stage `partner_answers`), each with the email files that prove it.

## Part 4: Memos, one at a time (final state in output/final/)
Each accepted submission releases the next memo. Handle each memo before you can see the next:
1. Read the memo from the portal inbox and work out which decisions it changes.
2. Update the filing decisions and rebuild everything that depends on them in output/final/ (the box/ tree, every log and report).
3. Run tools/check_filing.py on output/final/ and fix any failures.
4. Submit the updated filing to the portal (stage `memo_01`, `memo_02`, …). Fix and resubmit if rejected.
5. Write memo_reply_0N.md telling the sender exactly what changed because of that memo (emails moved, flags, incidents, paths).
After the last memo is accepted, write changes_report.md: every email whose category, matter, flags, privilege or path differs between output/phase1/filing_log.csv and output/final/filing_log.csv, with the memo that caused it, plus the changes to the wall incidents, privilege log, needs_review list, attorney actions and counts.

## Verification
Before finishing, open every scanned attachment again as an image and confirm the matter you chose. Re-read every email you flagged or placed in needs_review, and every email involving Heron, Fenwick, Kestrel, Tran or a screened person, and confirm the decision against the rules and memos. Check that the files in each output folder agree with each other and with their box/ tree, and that the last submission accepted by the portal matches output/final/. If you find a mistake, fix the decision, rebuild everything that depends on it, re-run the checker and check again. Write verification_log.md listing each check, the mistakes found, what you changed, the final checker output for both folders, the deliberate-break result and the portal receipts.

## Acceptance checks (how I will judge the result)
- triage_notes.md covers all 64 emails, and every scanned attachment is described from its image.
- Both filing logs have exactly 64 rows, and every category, matter, cross-reference, privilege value, flag and path follows the rules (and, for final, the memos).
- box/ in each folder matches its filing log exactly, with no missing, extra or misnamed files. Restricted items stay under Restricted, and no stub or copy crosses clients.
- wall_incidents.csv, privilege_log.csv, needs_review.md and attorney_actions.md are complete and correct for their phase.
- The checker really validates the rules, passes on both folders and catches the three deliberate breaks.
- The portal accepted every stage in order. partner_answers.md answers each question correctly with evidence. memo_reply_01 to 04 and changes_report.md match the real differences.
- verification_log.md shows real comparisons, and no unresolved mistake remains.
- No decision relies on information that is not in the emails, their attachments, the CSVs, the rules, the partner's questions or the memos.

When finished, give me a short summary: category counts for phase 1 and final, the emails in needs_review at each phase, the wall incidents, the privilege log count, any decision you changed after the partner's questions, what each memo changed, the portal receipts, and the checker results.
