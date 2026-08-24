# EXECUTION PLAYBOOK — AI Diplomacy & Governance Portfolio

**Audience:** the Hermes agent (any model) executing Q4 2026 portfolio work for Rex.
**You are an operator, not a strategist.** The strategy is already decided and red-team approved. Do not re-litigate it. Your job: execute the steps below exactly, flag blockers, and never publish anything without Rex's explicit OK.

Source of truth: `C:\Users\raksh\portfolio-site\blueprint-v1.md` (APPROVED 23 Aug 2026). If this playbook and the blueprint ever disagree, the blueprint wins — then tell Rex so he knows to update one of them.

---

## 0. Prime directives (read before any task)

1. **Approval-first.** Nothing leaves Rex's machine without his explicit OK — no publishing, no sending emails, no posting to Substack/LinkedIn/GitHub public repos. Draft → show Rex → wait.
2. **No legal interpretation.** Tracker entries state what a provision *says* ("Art. 70 requires X per source Y"), never what it *means*. Qualify everything; link every claim to a primary source with a date checked.
3. **Budget discipline.** ~10 hrs/wk TOTAL across all four products. If a task balloons past its estimate, stop and report rather than grinding on. Hours: tracker ~15/mo · F-briefs ~5/mo · I-memos ~5/mo · D-scans ~2.5/mo (private).
4. **Tripwires are automatic, not advisory.** Check them monthly (see §4). If one trips, apply its consequence immediately and inform Rex — no negotiation needed; he pre-approved these.
5. **Killed ideas stay dead** unless NEW evidence arrives: G divergence file, K syllabus, global power index. If Rex asks about them, cite blueprint §"Killed by red-team".
6. Rex is a non-coder. Every deliverable you show him must be plain-English summary first, artifact second.

---

## 1. The four products (what "done" looks like)

### A+B — Germany AI Act tracker (ANCHOR)
- **What:** bilingual DE/EN table tracking EU AI Act implementation in Germany + an "Enforcement & Communiqués" section. Data lives in `portfolio-site/tracker-data.csv`; rendered later as static-site table.
- **Cadence:** rolling; batch-update sessions of ~3–4 hrs.
- **Done when:** every row has: provision/article · German authority · status · deadline · source URL · last-checked date. No row may have an empty source or last-checked field.
- **v0 public tripwire:** live on GitHub Pages by **30 Sep 2026** (ugly is fine).

### F — EN curation briefs (Substack)
- **What:** English annotation/curation of German AI-policy sources (ChinAI style). Template: `portfolio-site/template-f-brief.md`.
- **Cadence:** ~2/month starting Oct 2026. Rotation includes tech-actor compliance profiles (counts as brief topics — no separate product).
- **Pipeline:** brief originates here → adapt to LinkedIn post (1/wk) → done. Never write platform-native content from scratch.
- **Done when:** template fully filled, all quotes translated/annotated in EN, links verified, Rex has approved final text.

### I — Capability→Clause memos
- **What:** one frontier capability mapped to one AI Act article, monthly. Template: `portfolio-site/template-i-memo.md`. Quarterly fallback if workload spikes (allowed, not failure).
- **Done when:** memo states capability, cites the exact article text, maps them WITHOUT claiming interpretation beyond what qualified sources say, ≤1,500 words, date-stamped.

### D-private — hiring scans (NEVER PUBLISH)
- **What:** quarterly scan of postings at target orgs: DGAP · Aspen Institute Germany · interface (ex-SNV) · AlgorithmWatch · EDRi · BNetzA/ministries.
- **Output:** private notes only. Feeds applications + cold-email pretexts. **Never write publicly about a target employer while applying there.**

---

## 2. Distribution rails (adapt, don't originate)

| Channel | Status | Rule |
|---|---|---|
| Substack | PRIMARY NOW, free tier | Home of F-briefs. Email list starts day 1. |
| LinkedIn | 1 post/wk, adapted | From existing F/I content only. |
| Static site | NOT LIVE until Impressum address + settled in Eichstätt | Anchor tracker + archive. |
| X | Dormant | Activate only with ≥10-piece backlog. |
| YouTube | 2027+, conditional | Only if income stable AND list ≥500 AND batching possible. |
| Other forums | Reader/commenter | Zero posting obligations. |

Monetization sequence (fixed): Werkstudent salary → paid tier mid-2027 if list ≥500 → courses/workshops after German credential. No billing setup before then.

---

## 3. Standard operating procedures

### SOP-1: Add/update a tracker row
1. Research: find primary source (official gazette, ministry page, BNetzA communiqué). Secondary sources OK for discovery, NEVER as the cited source.
2. Fill all six columns (see §1 A+B). Record `last-checked` = today.
3. Show Rex the diff (old vs new rows) before writing to `tracker-data.csv`.
4. After approval: append row, update any affected summary counts.

### SOP-2: Produce an F-brief (~2.5 hrs)
1. Pick topic from rotation or current German AI-policy news.
2. Gather 3–6 German-language primary sources.
3. Fill `template-f-brief.md`: context, curated excerpts w/ EN translation, annotation paragraphs, why-it-matters.
4. Self-check: every excerpt attributed; translations marked as yours ("my translation"); no unqualified claims.
5. Draft → Rex approves → save to `briefs/YYYY-MM-slug.md` → prepare LinkedIn adaptation.

### SOP-3: Produce an I-memo (~5 hrs incl. research)
1. Choose ONE frontier capability from current month's notable releases.
2. Locate the single most relevant AI Act article (verify text on EUR-Lex).
3. Fill `template-i-memo.md`.
4. Same approval pipeline as SOP-2. Output to `memos/YYYY-MM-capability-clause.md`.

### SOP-4: Quarterly hiring scan (private, ~2.5 hrs)
1. Check careers pages of all six target orgs.
2. Log: role · requirements · German level required · fit note · posting URL · date.
3. Deliverable: private summary + suggested 2–3 application priorities. File stays OUT of any public repo.

### SOP-5: Weekly wrap (15 min)
Report to Rex: hours spent per product · what shipped · next week's plan · any tripwire risk. Keep it under 10 lines.

---

## 4. Monthly tripwire check (run first week of each month)

| Tripwire | Condition | Action |
|---|---|---|
| ZERO-VISIBILITY | No public tracker v0 by 30 Sep 2026 | Drop static-site premise; distribute via LinkedIn + shared doc only |
| SPRAWL | >2 projects WIP simultaneously at week 6 | Freeze all except anchor tracker |
| COLLISION | <~5 hrs on anchor, 2 consecutive weeks | Pre-publish "paused until Feb" notice; shift hours to applications |
| OUTREACH RATIO | <30% of weekly career-hours on outreach/applications | Rebalance immediately; portfolio serves applications, not replaces them |

---

## 5. Q4 2026 milestones

- **Oct:** tracker v0 public · Substack live · first F-brief out.
- **Nov:** brief cadence established · I-memo #1.
- **Dec:** fact-check pass over everything published · "paused" protocol staged for exam season.

## 6. File map

```
C:\Users\raksh\portfolio-site\
  blueprint-v1.md          <- strategy source of truth
  EXECUTION-PLAYBOOK.md    <- this file
  HANDOFF-ARTIFACTS.md     <- build queue for artifacts
  tracker-data.csv         <- anchor data (created in artifact #2)
  sources.md               <- verified URL pack
  template-f-brief.md      <- F-brief fill-in template
  template-i-memo.md       <- I-memo fill-in template
  briefs\                  <- finished F-briefs
  memos\                   <- finished I-memos
C:\Users\raksh\
  rex_portfolio_landscape_research.md   <- research evidence base
  ai-diplomacy-ideation.md              <- ideation evidence base
```

## 7. When something goes wrong

- Tool/API fails → try alternative path; report fix + plain-English cause. Never fabricate data, sources, or dates.
- Source dead-link discovered in tracker → mark row `SOURCE DEAD`, search for archived version (web archive), flag to Rex same session.
- Rex unavailable >1 week → keep executing research/drafting (approval-gated steps pause, nothing publishes), log status for his return.
