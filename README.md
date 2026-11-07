# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->

1. A writer sends text and a `creator_id` to `POST /submit`.
2. The service validates the JSON request and creates a `content_id`.
3. The text is sent to `detector.py`, which calculates a model-based signal.
4. The text is sent to `stylometry.py`, which calculates a writing-style signal.
5. `scoring.py` combines both signals into one confidence score.
6. The score is converted into a high-confidence human, unsure, or
   high-confidence AI label.
7. The service returns the `content_id`, guess, confidence, label, and signal
   scores to the reader.

### False-positive trace

A real writer submits plain, predictable writing. The model signal may produce
a high AI-likelihood score because predictable language is not proof of AI
authorship. If the combined score crosses the AI threshold, the writer sees a
high-confidence AI label even though the work is theirs. The writer can call
`POST /appeal` with the `content_id` and their reasoning; the service records
the appeal and changes the item status to `under_review`.

### Endpoint contracts

`POST /submit`

- Request JSON: `{"text": "string", "creator_id": "string"}`
- Response JSON: `content_id`, `guess`, `confidence`, `label`,
  `model_score`, `style_score`, and `combined_score`

`POST /appeal`

- Request JSON: `{"content_id": "string", "reasoning": "string"}`
- Response JSON: `content_id`, a confirmation message, and the
  `under_review` status


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:** It measures how predictable the text is to a local
language model using perplexity. Lower perplexity becomes a higher
AI-likelihood score.

**Why that might differ between human and AI writing:** AI-generated writing
often follows likely word choices and predictable sentence patterns. Human
writing may make unusual word choices or abrupt turns, which can be less
predictable.

**What it can't see:** It cannot determine authorship. It may falsely flag a
human who writes plainly with common words, and it may miss AI writing that
uses unusual or complex wording.

### Signal two — the style signal

**What it measures:** It measures the shape of the text: sentence-length
variation, vocabulary variety, and punctuation usage, without interpreting the
meaning.

**Why that might differ between human and AI writing:** AI writing may have
even sentence lengths and narrower vocabulary, while human writing may have
more uneven sentence lengths and varied word choices.

**What it can't see:** It cannot understand meaning or identify the author.
Typos, quotations, or sentence changes can alter the measurements without
changing who wrote the text.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:** I use an equal-weight average of the model signal and the style
signal. Both signals run from 0 to 1, with higher values meaning more
AI-like. When they disagree, the average moves toward the middle and treats
the disagreement as uncertainty.

**The numbers:** `0.5 * model_score + 0.5 * style_score`, rounded to four
decimal places.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:** For the
text “The system follows a clear process. It handles each request carefully,
but human writing can vary,” the model score was `0.1709` and the style score
was `0.4099`. The average was `0.2904`, so the combined result stayed closer
to the human side while preserving the disagreement in the score.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 | We think this was probably written by a person. |
| unsure | 0.35–0.65 | We are not sure who wrote this. Please treat the result as uncertain. |
| high-confidence AI | 0.65–1.00 | We think this was probably written by AI. |

**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->

The unsure label avoids accusing the writer when the signals do not provide
enough evidence for a high-confidence decision.



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
C:\> curl.exe -X POST http://127.0.0.1:5000/submit -H "Content-Type: application/json" -d "{\"text\":\"I walked home in the rain and noticed a blue bird beside the road.\",\"creator_id\":\"writer1\"}"
```

```json
{
  "combined_score": 0.5544,
  "confidence": 0.5544,
  "content_id": "856a98b6-7b06-4aa7-9f03-85063747076e",
  "guess": "unsure",
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "model_score": 0.4421,
  "style_score": 0.6667
}
```

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json

```

**What the log shows afterwards**

```bash
C:\> curl.exe "http://127.0.0.1:5000/log?limit=5"
```

```json
{
  "count": 1,
  "entries": [
    {
      "combined_score": 0.2904,
      "content_id": "99874186-e0b3-4ba2-ac25-19c84ff2aaef",
      "creator_id": "writer1",
      "guess": "ai",
      "label": null,
      "model_score": 0.1709,
      "status": "decided",
      "style_score": 0.4099
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* I asked for help tracing a submission and identifying
  the blind spots in `detector.py` and `stylometry.py`.
- *What came back:* The explanation identified predictability as the model
  signal, sentence and vocabulary shape as the style signal, and explained
  that neither signal can prove authorship.
- *What I changed:* I added the submission path, signal descriptions, blind
  spots, and false-positive trace to this README.

**Moment 2**

- *What I asked for:* I asked for step-by-step CMD guidance to test the
  service and wire the detector into `/submit`.
- *What came back:* The guidance separated route testing from signal testing,
  then showed how to generate a `content_id`, log the model score, and inspect
  `GET /log`.
- *What I changed:* I implemented `/submit` in `app.py`, then added the
  stylometry signal, combined score, labels, and appeal flow in later
  milestones.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

Ten submissions per minute allows a real writer to submit several pieces
without interruption, while limiting rapid threshold-mapping scripts. The
daily limit of 200 allows continued normal use but prevents unlimited probing.

**What a caller counts as:** A caller is counted by `creator_id` when it is a
valid non-empty string; otherwise the request falls back to the remote address.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

The flood run produced 10 accepted requests and 5 rate-limited requests. The
service reported `"rate_limiting": true` from `GET /health`. Rate-limited
requests were recorded in `logs/audit.jsonl` with
`"event": "rejected"` and `"reason": "rate_limited"`.

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->

The complete 56-attack report is in
`results/attack_run_2026-11-07_1715_before.md`. I marked each result as
`HELD` when the attack did not achieve its stated target and `BROKE` when it
did or when the service failed.

| Family | Attacks | Held | Broke |
|---|---:|---:|---:|
| evasion | 10 | 1 | 9 |
| false positive | 8 | 2 | 6 |
| prompt injection | 6 | 6 | 0 |
| malformed | 20 | 12 | 8 |
| flood_same_creator | 12 | 12 | 0 |
| **Total** | **56** | **33** | **23** |

The flood family was held because the first ten requests were accepted and
the remaining two were rejected with `429`, matching the configured limit.
The malformed one-character input `MF02` returned `500`, so it was marked
`BROKE`.

**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
[
  {
    "creator_id": "flood_tester",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected"
  },
  {
    "creator_id": "flood_tester",
    "event": "rejected",
    "limit": "10 per 1 minute",
    "reason": "rate_limited",
    "status": "rejected"
  },
  {
    "content_id": "60e16eab-efee-4028-84bc-12c5366ade17",
    "creator_id": "attacker_EV01",
    "guess": "human",
    "model_score": 0.1635,
    "style_score": 0.5085,
    "combined_score": 0.336,
    "label": "We think this was probably written by a person.",
    "status": "decided"
  },
  {
    "content_id": "facd800e-d378-4fb6-aea6-856e101552f5",
    "creator_id": "attacker_EV02",
    "guess": "unsure",
    "model_score": 0.5943,
    "style_score": 0.3031,
    "combined_score": 0.4487,
    "label": "We are not sure who wrote this. Please treat the result as uncertain.",
    "status": "decided"
  },
  {
    "content_id": "9b661820-bfe7-49d6-9355-ae6a257e97b1",
    "creator_id": "attacker_FP01",
    "guess": "unsure",
    "model_score": 0.6175,
    "style_score": 0.5652,
    "combined_score": 0.5914,
    "label": "We are not sure who wrote this. Please treat the result as uncertain.",
    "status": "decided"
  },
  {
    "content_id": "3c3163b1-f969-4fd8-bba8-06557367dab7",
    "creator_id": "attacker_FP02",
    "guess": "ai",
    "model_score": 0.7387,
    "style_score": 0.6503,
    "combined_score": 0.6945,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "content_id": "3f62af93-b29b-4ab2-b1e0-e6e6e1fef0",
    "creator_id": "attacker_MF03",
    "guess": "human",
    "model_score": 0.0,
    "style_score": 0.6667,
    "combined_score": 0.3333,
    "label": "We think this was probably written by a person.",
    "status": "decided"
  },
  {
    "content_id": "81408504-28c3-4d38-892d-612e67ee5584",
    "creator_id": "attacker_MF05",
    "guess": "ai",
    "model_score": 0.9976,
    "style_score": 0.6667,
    "combined_score": 0.8321,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "content_id": "f972c41b-7bd3-46d7-bb63-9e8876152c7f",
    "creator_id": "attacker_MF07",
    "guess": "ai",
    "model_score": 0.9064,
    "style_score": 1.0,
    "combined_score": 0.9532,
    "label": "We think this was probably written by AI.",
    "status": "decided"
  },
  {
    "content_id": "2925a0f6-4bfd-4c61-8d82-535e4a86aca4",
    "creator_id": "unknown",
    "guess": "unsure",
    "model_score": 0.2395,
    "style_score": 0.6667,
    "combined_score": 0.4531,
    "label": "We are not sure who wrote this. Please treat the result as uncertain.",
    "status": "decided"
  }
]
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

`MF02` was a one-character submission that caused HTTP 500. The failure
happened before a controlled rejection and therefore produced neither a useful
decision nor a clear audit entry. The route should reject text that is too
short for the detector with HTTP 400 and record the reason.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
