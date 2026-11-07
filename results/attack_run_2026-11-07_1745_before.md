# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 17:45
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `8b211dba-6d06-4cd3-89fa-034ecd12e199` | human | 0.336 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `91e1e44f-3528-4081-bad8-e7366d844ba8` | unsure | 0.449 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `9067fc3d-6e5c-42b7-b7b2-45ef53471f1d` | unsure | 0.533 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `b3ee4777-68a6-449a-86fb-d3b5ca676003` | unsure | 0.545 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `779ee458-0a74-464c-9e28-8b445a67e990` | human | 0.314 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `650dd692-4511-4158-9ad5-88647465d273` | unsure | 0.450 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d2939047-1f6b-4f86-91ca-ec7d326ae255` | unsure | 0.485 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `a1ceea18-c591-4b3f-8a51-06f6ce1bb5e3` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `ed5b0764-b5fc-4f52-9e16-13446f2eb2e2` | unsure | 0.548 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `c92d3b0e-241f-4ab7-96a4-8eb2b470466f` | ai | 0.924 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `6a3a29f4-f7c2-4022-836b-780680c973e3` | unsure | 0.591 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `e035c0bb-229e-4de9-838d-a1738fb6e982` | ai | 0.695 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `e3cb8756-3c57-4a39-b7ab-ba09748033c0` | ai | 0.724 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `64e56706-c9f5-4128-863e-c2b09409196f` | ai | 0.686 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `aae82b78-4afc-48f3-86eb-ea029bb3d12d` | ai | 0.744 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `4a74388e-4a7c-495f-b17e-490317ca7d28` | ai | 0.709 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `79590cd2-fd94-4237-842a-fc6f385d589d` | ai | 0.745 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `d4833c8e-509a-49b2-8173-bd401a59129d` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `ebf9f8e3-7d26-4c1e-bfd8-82a0e9439e85` | unsure | 0.454 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `02b21a45-01b7-4006-a1ff-b725e9d16243` | human | 0.278 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `0a6cc434-91d0-4dd2-9831-d7e355a8ba71` | unsure | 0.553 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `3518f9ca-d0ac-4c46-89c0-48f6faaaa4ba` | unsure | 0.474 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `097dc3b8-8ebe-4689-a3c1-669615188531` | unsure | 0.408 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `5f2a14d7-d5b7-4dc2-9d39-66a91fabaed2` | unsure | 0.566 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `c7efae69-8065-428c-b3b3-7ce356ecedf6` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `64a4b39e-18dc-4371-92a4-e563b3cea1f7` | unsure | 0.453 |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2424fd60-f2bd-4e58-9a9f-be1e1331ee32` | human | 0.348 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f53eaffd-11a4-4787-bacc-5db9bb899e77` | human | 0.348 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `3b81ef70-489e-4453-b321-e7d70020c8db` | human | 0.348 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `45602345-0e02-41a9-8ddd-c6ec0b79c6b5` | human | 0.348 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b8e4b26b-c40a-467c-8a22-9ff1006a21be` | human | 0.348 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `e55fdee6-1ed9-49ba-8ead-fb0bd663125d` | human | 0.348 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6fa8c248-dc27-4e46-92da-a5a24e7e3137` | human | 0.348 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `603951f4-be6c-4127-a6b0-033d8a1a23df` | human | 0.348 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9da0b34d-bc5a-4dc3-9f4c-de449b3b3e2e` | human | 0.348 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6e5079e0-d4da-4ea6-85c6-109b5ec1d75b` | human | 0.348 |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
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
  "content_id": "8b211dba-6d06-4cd3-89fa-034ecd12e199",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.336,
  "model_score": 0.1635,
  "style_score": 0.5085,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "91e1e44f-3528-4081-bad8-e7366d844ba8",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.4487,
  "model_score": 0.5943,
  "style_score": 0.3031,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "9067fc3d-6e5c-42b7-b7b2-45ef53471f1d",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.5331,
  "model_score": 0.6662,
  "style_score": 0.4,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "b3ee4777-68a6-449a-86fb-d3b5ca676003",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.5454,
  "model_score": 0.6114,
  "style_score": 0.4795,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "779ee458-0a74-464c-9e28-8b445a67e990",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.3137,
  "model_score": 0.3212,
  "style_score": 0.3063,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "650dd692-4511-4158-9ad5-88647465d273",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.4501,
  "model_score": 0.5727,
  "style_score": 0.3275,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d2939047-1f6b-4f86-91ca-ec7d326ae255",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.4854,
  "model_score": 0.5862,
  "style_score": 0.3845,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "a1ceea18-c591-4b3f-8a51-06f6ce1bb5e3",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.4088,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "ed5b0764-b5fc-4f52-9e16-13446f2eb2e2",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.5485,
  "model_score": 0.7042,
  "style_score": 0.3928,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "c92d3b0e-241f-4ab7-96a4-8eb2b470466f",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.924,
  "model_score": 0.9792,
  "style_score": 0.8687,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "6a3a29f4-f7c2-4022-836b-780680c973e3",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5914,
  "model_score": 0.6175,
  "style_score": 0.5652,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "e035c0bb-229e-4de9-838d-a1738fb6e982",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.6945,
  "model_score": 0.7387,
  "style_score": 0.6503,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "e3cb8756-3c57-4a39-b7ab-ba09748033c0",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.7236,
  "model_score": 0.8051,
  "style_score": 0.642,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "64e56706-c9f5-4128-863e-c2b09409196f",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.6861,
  "model_score": 0.8329,
  "style_score": 0.5392,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "aae82b78-4afc-48f3-86eb-ea029bb3d12d",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.7438,
  "model_score": 0.8005,
  "style_score": 0.6871,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "4a74388e-4a7c-495f-b17e-490317ca7d28",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.7087,
  "model_score": 0.8814,
  "style_score": 0.536,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "79590cd2-fd94-4237-842a-fc6f385d589d",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.7454,
  "model_score": 0.8816,
  "style_score": 0.6093,
  "label": "We think this was probably written by AI.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "d4833c8e-509a-49b2-8173-bd401a59129d",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.4223,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "ebf9f8e3-7d26-4c1e-bfd8-82a0e9439e85",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.4541,
  "model_score": 0.4625,
  "style_score": 0.4458,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "02b21a45-01b7-4006-a1ff-b725e9d16243",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.2775,
  "model_score": 0.2044,
  "style_score": 0.3506,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "0a6cc434-91d0-4dd2-9831-d7e355a8ba71",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.5531,
  "model_score": 0.5943,
  "style_score": 0.5119,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "3518f9ca-d0ac-4c46-89c0-48f6faaaa4ba",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.4736,
  "model_score": 0.4998,
  "style_score": 0.4473,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "097dc3b8-8ebe-4689-a3c1-669615188531",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.4082,
  "model_score": 0.6401,
  "style_score": 0.1762,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "5f2a14d7-d5b7-4dc2-9d39-66a91fabaed2",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5659,
  "model_score": 0.5583,
  "style_score": 0.5735,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
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
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "c7efae69-8065-428c-b3b3-7ce356ecedf6",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.3333,
  "model_score": 0.0,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF07",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 200,
  "content_id": "64a4b39e-18dc-4371-92a4-e563b3cea1f7",
  "creator_id": null,
  "guess": "unsure",
  "confidence": 0.4531,
  "model_score": 0.2395,
  "style_score": 0.6667,
  "label": "We are not sure who wrote this. Please treat the result as uncertain.",
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "2424fd60-f2bd-4e58-9a9f-be1e1331ee32",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "f53eaffd-11a4-4787-bacc-5db9bb899e77",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "3b81ef70-489e-4453-b321-e7d70020c8db",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "45602345-0e02-41a9-8ddd-c6ec0b79c6b5",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "b8e4b26b-c40a-467c-8a22-9ff1006a21be",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "e55fdee6-1ed9-49ba-8ead-fb0bd663125d",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "6fa8c248-dc27-4e46-92da-a5a24e7e3137",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "603951f4-be6c-4127-a6b0-033d8a1a23df",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "9da0b34d-bc5a-4dc3-9f4c-de449b3b3e2e",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "6e5079e0-d4da-4ea6-85c6-109b5ec1d75b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3477,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
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
  "verdict": ""
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
  "verdict": ""
}
```
