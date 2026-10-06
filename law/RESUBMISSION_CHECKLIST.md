# Law-firm email filing task: resubmission checklist

The reviewer's finding: the uploaded attachment was a 0-byte file, so the self-test never saw the inputs. Follow these steps in order.

## A. Check the archive before using it
1. Download **LAW_task_inputs_COMPLETE.zip**. It must be about **1.4 MB**. If your device shows 0 KB, download it again.
2. Open it on your device. You should see: mailbox/ (64 .eml files), matters.csv, staff.csv, filing_rules.md, memos/ (4 files), INPUTS.md and MANIFEST.sha256.
3. Never upload PRIVATE_answer_key_law.md anywhere in the task.

## B. Fresh self-test with the full inputs
1. Create a **new, empty** GitHub repo.
2. Upload the **contents** of the zip to the repo root, keeping the mailbox/ and memos/ folders, plus count_steps.py. Then check on GitHub that mailbox/ shows 64 files and memos/ shows 4.
3. Start a **new** session at claude.ai/code on that repo. Paste the full prompt from task_prompt_law.md and nothing else.
4. Do not step in until it finishes. If it reports a missing file at the input check, stop: the upload is incomplete. Fix the repo and start a new session.

## C. Count the steps and keep the trace (same session, after the task ends)
1. Send:
   > Please run the attached count_steps.py (python3 count_steps.py) to count the execution steps of this session and tell me the result. If the script says no session log was found, count the steps yourself following the rules it prints.
   Take a screenshot of the reply.
2. Send:
   > Copy this session's full log file (the .jsonl the script used) into a folder named trace/ in the repo, then commit and push it.
   That keeps the complete main-model trace the reviewer asked for. Also keep the session link.
3. Run the self-check skill if you use it, and take a screenshot of that too.

## D. Fill in the form
- **Input Attachments:** upload **LAW_task_inputs_COMPLETE.zip** only. After it uploads, check that the form shows its size (about 1.4 MB), not 0 bytes.
- **Full Task Prompt:** the updated task_prompt_law.md (it now starts with the input check).
- **Step-Count:** the exact number from step C1, with its screenshot.
- Do not add anything to the prompt just to raise the step count.
