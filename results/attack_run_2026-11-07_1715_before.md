# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 17:15
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `60e16eab-efee-4028-84bc-12c5366ade17` | human | 0.336 | BROKE |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `facd800e-d378-4fb6-aea6-856e101552f5` | unsure | 0.449 | BROKE |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `7922ec6f-b685-41e5-ae34-abae64dee26b` | unsure | 0.533 | BROKE |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `2578b479-e89e-4b6c-9e95-d7024d7b766f` | unsure | 0.545 | BROKE |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `97ee7465-632f-4835-a918-f8f9ba5c84c6` | human | 0.314 | BROKE |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `8dc35893-c6cd-416c-8a0a-6b71aaebbc49` | unsure | 0.450 | BROKE |
| EV07 | evasion | signal two: padding with punctuation | 200 | `dade1284-0ab2-47dc-ab97-cd0a12bab3d6` | unsure | 0.485 | BROKE |
| EV08 | evasion | signal one: text below the token window | 200 | `b25780dc-1cbf-4511-8e7a-8a0f8db1a22f` | unsure | 0.409 | BROKE |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `9bd7901b-c4e7-44c2-8382-6d002d152763` | unsure | 0.548 | BROKE |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d5e61314-fe76-4044-bde8-94c20944ae23` | ai | 0.924 | HELD |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `9b661820-bfe7-49d6-9355-ae6a257e97b1` | unsure | 0.591 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `3c3163b1-f969-4fd8-bba8-06557367dab7` | ai | 0.695 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `3ddfb8ab-77e1-484e-b7ca-dbfc0095253d` | ai | 0.724 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `19c17701-44b1-4a9c-80ff-60f4ed01de41` | ai | 0.686 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `9fcaec51-91be-4db0-a8d8-6dc6c76974f3` | ai | 0.744 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `c60466e9-8a69-4b8a-ac8c-c7eed31132d3` | ai | 0.709 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `994176d4-8ccb-4b7a-aeec-89f3dc912ccc` | ai | 0.745 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `8e668071-ec0e-4990-9478-dc652a6c0692` | unsure | 0.422 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `eec71708-1383-48cc-b05f-9bafc12a0ad6` | unsure | 0.454 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `5d91a19d-3ac2-4f6e-b83a-484733bd13cb` | human | 0.278 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d28d2b43-e100-4f6c-8732-b77923c63dcd` | unsure | 0.553 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `55fb5799-c1a5-41d1-8efa-46b847954624` | unsure | 0.474 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `e9c4cc31-c8b3-4708-9251-bf9fb0985eb3` | unsure | 0.408 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `9f8ddec6-5b44-4de2-b052-e40bb0464752` | unsure | 0.566 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `3f62af93-b29b-4ab2-b1e0-e6b81fe1fef0` | human | 0.333 | BROKE |
| MF04 | malformed | text is only punctuation | 200 | `4cf34123-c256-4540-a97a-236952a4af44` | unsure | 0.506 | BROKE |
| MF05 | malformed | text is a very long single word | 200 | `81408504-28c3-4d38-892d-612e67ee5584` | ai | 0.832 | BROKE |
| MF06 | malformed | text is emoji only | 200 | `6ed4c394-556d-47e4-882c-2e6e12c9d819` | ai | 0.999 | BROKE |
| MF07 | malformed | text is right-to-left script | 200 | `f972c41b-7bd3-46d7-bb63-9e8876152c7f` | ai | 0.953 | BROKE |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 200 | `2925a0f6-4bfd-4c61-8d82-535e4a86aca4` | unsure | 0.453 | BROKE |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `aa133023-04bb-4b79-9ba2-26a981a34e53` | human | 0.348 | HELD |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `62fdad8b-dc8f-4380-9485-8707275ad555` | human | 0.348 | HELD |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `595b737b-7df6-4a41-97af-384b2892563a` | human | 0.348 | HELD |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cd9a1410-da8f-4163-beb6-6d30e6744423` | human | 0.348 | HELD |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e8010fc8-894f-460b-bf6b-9ef2bd0865b8` | human | 0.348 | HELD |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc1569d7-a66b-4800-9867-2939b6bf449b` | human | 0.348 | HELD |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `8a5d83e7-665c-4d91-a2d4-04f6b278cc75` | human | 0.348 | HELD |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `bc586566-2369-4b97-b66a-06aa67af6feb` | human | 0.348 | HELD |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `47895916-e2aa-4909-9cb1-e5694b6e437e` | human | 0.348 | HELD |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1d178be0-d89b-45bb-9c78-78c416a25f35` | human | 0.348 | HELD |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "60e16eab-efee-4028-84bc-12c5366ade17",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.336,
  "model_score": 0.1635,
  "style_score": 0.5085,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "facd800e-d378-4fb6-aea6-856e101552f5",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4487,
  "model_score": 0.5943,
  "style_score": 0.3031,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "7922ec6f-b685-41e5-ae34-abae64dee26b",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5331,
  "model_score": 0.6662,
  "style_score": 0.4,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "2578b479-e89e-4b6c-9e95-d7024d7b766f",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5454,
  "model_score": 0.6114,
  "style_score": 0.4795,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "97ee7465-632f-4835-a918-f8f9ba5c84c6",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3137,
  "model_score": 0.3212,
  "style_score": 0.3063,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "8dc35893-c6cd-416c-8a0a-6b71aaebbc49",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4501,
  "model_score": 0.5727,
  "style_score": 0.3275,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "dade1284-0ab2-47dc-ab97-cd0a12bab3d6",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4854,
  "model_score": 0.5862,
  "style_score": 0.3845,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "b25780dc-1cbf-4511-8e7a-8a0f8db1a22f",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4088,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "9bd7901b-c4e7-44c2-8382-6d002d152763",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5485,
  "model_score": 0.7042,
  "style_score": 0.3928,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "d5e61314-fe76-4044-bde8-94c20944ae23",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.924,
  "model_score": 0.9792,
  "style_score": 0.8687,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "HELD"
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "9b661820-bfe7-49d6-9355-ae6a257e97b1",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5914,
  "model_score": 0.6175,
  "style_score": 0.5652,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "3c3163b1-f969-4fd8-bba8-06557367dab7",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6945,
  "model_score": 0.7387,
  "style_score": 0.6503,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "3ddfb8ab-77e1-484e-b7ca-dbfc0095253d",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7236,
  "model_score": 0.8051,
  "style_score": 0.642,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "19c17701-44b1-4a9c-80ff-60f4ed01de41",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6861,
  "model_score": 0.8329,
  "style_score": 0.5392,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "9fcaec51-91be-4db0-a8d8-6dc6c76974f3",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7438,
  "model_score": 0.8005,
  "style_score": 0.6871,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "c60466e9-8a69-4b8a-ac8c-c7eed31132d3",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7087,
  "model_score": 0.8814,
  "style_score": 0.536,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "994176d4-8ccb-4b7a-aeec-89f3dc912ccc",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7454,
  "model_score": 0.8816,
  "style_score": 0.6093,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "8e668071-ec0e-4990-9478-dc652a6c0692",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4223,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "eec71708-1383-48cc-b05f-9bafc12a0ad6",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4541,
  "model_score": 0.4625,
  "style_score": 0.4458,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "5d91a19d-3ac2-4f6e-b83a-484733bd13cb",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2775,
  "model_score": 0.2044,
  "style_score": 0.3506,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "d28d2b43-e100-4f6c-8732-b77923c63dcd",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5531,
  "model_score": 0.5943,
  "style_score": 0.5119,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "55fb5799-c1a5-41d1-8efa-46b847954624",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4736,
  "model_score": 0.4998,
  "style_score": 0.4473,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "e9c4cc31-c8b3-4708-9251-bf9fb0985eb3",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4082,
  "model_score": 0.6401,
  "style_score": 0.1762,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "9f8ddec6-5b44-4de2-b052-e40bb0464752",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5659,
  "model_score": 0.5583,
  "style_score": 0.5735,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "HELD"
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "3f62af93-b29b-4ab2-b1e0-e6b81fe1fef0",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.3333,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "4cf34123-c256-4540-a97a-236952a4af44",
  "creator_id": "attacker_MF04",
  "guess": "unsure",
  "confidence": 0.5056,
  "model_score": 0.0112,
  "style_score": 1.0,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "81408504-28c3-4d38-892d-612e67ee5584",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.8321,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "6ed4c394-556d-47e4-882c-2e6e12c9d819",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.9985,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "f972c41b-7bd3-46d7-bb63-9e8876152c7f",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9532,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": "BROKE"
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "2925a0f6-4bfd-4c61-8d82-535e4a86aca4",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4531,
  "model_score": 0.2395,
  "style_score": 0.6667,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": "BROKE"
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "aa133023-04bb-4b79-9ba2-26a981a34e53",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "62fdad8b-dc8f-4380-9485-8707275ad555",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "595b737b-7df6-4a41-97af-384b2892563a",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "cd9a1410-da8f-4163-beb6-6d30e6744423",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "e8010fc8-894f-460b-bf6b-9ef2bd0865b8",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "bc1569d7-a66b-4800-9867-2939b6bf449b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "8a5d83e7-665c-4d91-a2d4-04f6b278cc75",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "bc586566-2369-4b97-b66a-06aa67af6feb",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "47895916-e2aa-4909-9cb1-e5694b6e437e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "1d178be0-d89b-45bb-9c78-78c416a25f35",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": "HELD"
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": "HELD"
}
```

