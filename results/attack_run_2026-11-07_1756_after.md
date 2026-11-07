# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 17:56
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `15dd16c2-c41e-49d2-b2db-cfa5c245c476` | human | 0.336 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `d60b880d-0356-4a87-8e78-60235d85388a` | unsure | 0.449 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `fb7ff476-46a3-4d0f-aa45-26721d0cbb98` | unsure | 0.533 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `2ecc99cf-e7da-4ffc-94a8-2c7fdccf903e` | unsure | 0.545 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f8349cfd-3e88-45d1-b948-2456b7a4cd9a` | human | 0.314 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `9bfd107d-20ea-48bc-8e5e-c3288c57722b` | unsure | 0.450 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `0760971d-6539-4b91-8978-b8f1122f3ce0` | unsure | 0.485 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `eaa5eecc-9017-48d0-86cb-0cfbbc0bf1b7` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `49f6a7b8-af13-482f-b5f4-9d33c48a2657` | unsure | 0.548 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `cd718927-98ce-494e-b00c-126bcd01d133` | ai | 0.924 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `f720abc3-65cd-4f98-bd55-1dd8c5763117` | unsure | 0.591 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `c271fbe5-b8b0-46c5-b4aa-d7175a414142` | ai | 0.695 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4abef71c-9c69-4f2d-9d2c-1d955d84267a` | ai | 0.724 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `8c61239c-7eb5-4977-b939-857c536d0214` | ai | 0.686 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `3f595063-d258-4e45-91c9-613c241313f9` | ai | 0.744 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `8ac7e5bb-215d-4cb3-9f5a-ea0cfb74f443` | ai | 0.709 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `7f0a2a26-3420-4433-9694-10c9a3c01c1c` | ai | 0.745 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `c45a0bb5-6bed-4451-9242-abd0d3eac9e4` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `3c261957-7079-4e9b-9b1f-592df6a13363` | unsure | 0.454 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `ff442220-8a1e-4539-aa43-d9b6547daee0` | human | 0.278 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `d2f45dfa-4848-4ee9-833c-1e9f63546d15` | unsure | 0.553 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0d5b2e08-76cc-429c-a261-fcdd0d006725` | unsure | 0.474 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `d3c077af-537f-420e-ba7e-d8b5611d68ca` | unsure | 0.408 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `d66a8745-4330-4c78-99a7-70ad2a7f8406` | unsure | 0.566 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `436c71bb-4ceb-4086-85eb-529de30d6bc9` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `5e273de4-8e08-4ed7-a061-18a16542a5ef` | unsure | 0.453 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b3f50319-cf2c-4b58-8252-17f0d3190caf` | human | 0.348 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b1da72d4-8ba3-4ed7-bf8d-218d68987bdd` | human | 0.348 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a324711b-97f4-45a4-b392-f742ac739a68` | human | 0.348 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `cab7c82b-b567-4b03-b7de-95a61a136e6e` | human | 0.348 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `f4767a43-47f7-46eb-b834-93f0a57c6c04` | human | 0.348 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d25de34c-3947-4df8-8f89-536a04ade967` | human | 0.348 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `fa677afb-559c-4195-b29f-4c021d8bc9ae` | human | 0.348 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `75ac8288-fb72-456c-b9e5-0f5cbc348165` | human | 0.348 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `451bedfc-eb7c-4cd9-8f04-fb00b67c26b5` | human | 0.348 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d0628810-d58d-4858-bd4d-fa120367c8ef` | human | 0.348 |  |
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
  "content_id": "15dd16c2-c41e-49d2-b2db-cfa5c245c476",
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
  "content_id": "d60b880d-0356-4a87-8e78-60235d85388a",
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
  "content_id": "fb7ff476-46a3-4d0f-aa45-26721d0cbb98",
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
  "content_id": "2ecc99cf-e7da-4ffc-94a8-2c7fdccf903e",
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
  "content_id": "f8349cfd-3e88-45d1-b948-2456b7a4cd9a",
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
  "content_id": "9bfd107d-20ea-48bc-8e5e-c3288c57722b",
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
  "content_id": "0760971d-6539-4b91-8978-b8f1122f3ce0",
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
  "content_id": "eaa5eecc-9017-48d0-86cb-0cfbbc0bf1b7",
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
  "content_id": "49f6a7b8-af13-482f-b5f4-9d33c48a2657",
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
  "content_id": "cd718927-98ce-494e-b00c-126bcd01d133",
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
  "content_id": "f720abc3-65cd-4f98-bd55-1dd8c5763117",
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
  "content_id": "c271fbe5-b8b0-46c5-b4aa-d7175a414142",
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
  "content_id": "4abef71c-9c69-4f2d-9d2c-1d955d84267a",
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
  "content_id": "8c61239c-7eb5-4977-b939-857c536d0214",
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
  "content_id": "3f595063-d258-4e45-91c9-613c241313f9",
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
  "content_id": "8ac7e5bb-215d-4cb3-9f5a-ea0cfb74f443",
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
  "content_id": "7f0a2a26-3420-4433-9694-10c9a3c01c1c",
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
  "content_id": "c45a0bb5-6bed-4451-9242-abd0d3eac9e4",
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
  "content_id": "3c261957-7079-4e9b-9b1f-592df6a13363",
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
  "content_id": "ff442220-8a1e-4539-aa43-d9b6547daee0",
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
  "content_id": "d2f45dfa-4848-4ee9-833c-1e9f63546d15",
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
  "content_id": "0d5b2e08-76cc-429c-a261-fcdd0d006725",
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
  "content_id": "d3c077af-537f-420e-ba7e-d8b5611d68ca",
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
  "content_id": "d66a8745-4330-4c78-99a7-70ad2a7f8406",
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
  "content_id": "436c71bb-4ceb-4086-85eb-529de30d6bc9",
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
  "content_id": "5e273de4-8e08-4ed7-a061-18a16542a5ef",
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
  "content_id": "b3f50319-cf2c-4b58-8252-17f0d3190caf",
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
  "content_id": "b1da72d4-8ba3-4ed7-bf8d-218d68987bdd",
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
  "content_id": "a324711b-97f4-45a4-b392-f742ac739a68",
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
  "content_id": "cab7c82b-b567-4b03-b7de-95a61a136e6e",
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
  "content_id": "f4767a43-47f7-46eb-b834-93f0a57c6c04",
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
  "content_id": "d25de34c-3947-4df8-8f89-536a04ade967",
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
  "content_id": "fa677afb-559c-4195-b29f-4c021d8bc9ae",
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
  "content_id": "75ac8288-fb72-456c-b9e5-0f5cbc348165",
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
  "content_id": "451bedfc-eb7c-4cd9-8f04-fb00b67c26b5",
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
  "content_id": "d0628810-d58d-4858-bd4d-fa120367c8ef",
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
