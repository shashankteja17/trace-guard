# START HERE — submission sprint

## First: verify that the submission is still open

The detailed rules page has shown **October 23, 2026 at 11:59 p.m. Pacific Time**, which converts to **October 24, 2026 at 12:29 p.m. India Standard Time**. The general hackathon listing has also displayed October 30 in one place, so the site appears inconsistent. Open the [official hackathon page](https://builder.aws.com/build/hackathons/4f50957c-1d08-37ab-b11c-97516b9adeb4/agent-experience-hackathon?tab=rules) and check whether the project submission action is enabled and what deadline it displays. Do not assume an extension from the general listing alone.

## Minimum credible submission sequence

1. **Create a new public GitHub repository** with a new project name such as `trace-guard-decider-2b`. Upload the contents of this folder (not the ZIP wrapper folder). Do not reuse a previously published project as your new entry.
2. **Run the actual Strands integration.** Start the Decider 2B model server; then run `strands_agent.py` once with a harmless documentation lookup and once with the adversarial export prompt in the README. Confirm the console shows the real Decider model and probabilities.
3. **Connect Bedrock.** Set valid AWS credentials and model access, then demonstrate a real Strands Agent turn powered by Bedrock. Never show AWS keys in the video or repository.
4. **Run the dashboard** with `streamlit run app.py`. Show the action envelope, verdict trace and CSV audit timeline. Do not treat the app's local fallback as proof of Decider usage.
5. **Publish an article** using `ARTICLE_DRAFT.md` as the draft, but fill in the repository/video URLs and any observed measurements. Never invent benchmark results or say Bedrock responded if it did not.
6. **Record a public demo under three minutes** using `DEMO_SCRIPT.md`. Keep it accessible to viewers without a sign-in if the submission rules require a public video.
7. **Submit both required tags:** `#strands-decider-2b` and `#policy` (you can mention `#guardrails` as a secondary pattern).

## What must be verified before you call it a submission

- The Strands Agent actually runs and a Decider 2B decision happens before `simulate_action` can execute.
- The Bedrock model call succeeds in your configured AWS account and region.
- The public repository is accessible, and article + demo links are accessible.
- The video is under three minutes and shows a real decision, not a mock result.
- Current portal rules permit your entry and country/age/eligibility requirements are satisfied.

The ZIP contains a runnable starter and source files, but I have only syntax-checked the code and run the three unit smoke tests here. I have **not** run the live Decider 2B checkpoint or called your AWS Bedrock account from this environment. You must verify those integrations before representing the project as fully working.
