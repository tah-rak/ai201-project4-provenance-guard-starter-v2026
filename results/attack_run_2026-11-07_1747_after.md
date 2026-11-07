# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-07 17:47
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
| EV01 | evasion | signal two: typos raise word variety | 200 | `e3415f21-01e5-465f-8f7a-cbc9e05452f1` | human | 0.336 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `77df0dec-a7fa-45cf-83a0-c75b27c61ab6` | unsure | 0.449 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `2fedbf2e-997c-43be-80c4-4bac2ed4c1ff` | unsure | 0.533 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `8a66526f-7607-46b1-b2ca-42974724768e` | unsure | 0.545 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `f63a4a92-acb6-4f7f-a541-797ef753ed65` | human | 0.314 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `0aa9a735-7d88-49b6-85d7-6c6c8f83d006` | unsure | 0.450 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `638066bd-6074-4a58-8f08-79f7327c1285` | unsure | 0.485 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `65f993b4-e59f-4cca-89db-b7ed3e08cbae` | unsure | 0.409 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `7144f951-fb86-420c-8aea-c479d3f9a0dd` | unsure | 0.548 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `a95ec52c-30fa-497a-9c34-c5cf7c3a9235` | ai | 0.924 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `eb9641dc-15e1-4ff3-b696-16ce93a65366` | unsure | 0.591 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `78094061-fb17-45fd-a7e6-b954eb7b2c92` | ai | 0.695 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `4e50fada-5fd9-4963-8e7a-6171aae4141a` | ai | 0.724 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `56c718bf-71c5-4e5e-8a8a-0df163d656c5` | ai | 0.686 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `46d7abd3-a0ae-40e2-91b3-8e9cbb50f5cc` | ai | 0.744 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `e7896347-fd08-4e16-8ec7-53bb0c382b46` | ai | 0.709 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f786d944-23cb-49a4-8761-939c56131b97` | ai | 0.745 |  |
| FP08 | false_positive | very short genuine human submission | 200 | `92bda60b-a184-4ef2-9a69-069a12a40b8e` | unsure | 0.422 |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7b1c5033-3752-4cd2-81d8-e63a2e7e9ffd` | unsure | 0.454 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `08c99025-73a3-4309-9d93-c5bdba2c96b6` | human | 0.278 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `038a72c4-4c69-4f8c-b3de-a46dff0a1047` | unsure | 0.553 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `f0498e19-5dee-43f9-8130-ddef298f53e3` | unsure | 0.474 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `106e3f4c-fcc9-468f-b5ab-7d92e0c97660` | unsure | 0.408 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `e8ef6d86-417e-4653-a38d-e6450f19da00` | unsure | 0.566 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 200 | `53215922-c1cd-4980-9545-4f0b6075c9ae` | human | 0.333 |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 400 | `—` | — | — |  |
| MF08 | malformed | text is 60,000 characters | 400 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 200 | `c1d91bc1-5ad3-425f-8c30-d64df272bc05` | unsure | 0.453 |  |
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
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d974eeec-e12d-4509-b117-ea2a5277531a` | human | 0.348 |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `6adaea47-fecb-4edc-8c45-bbebaf12ddb8` | human | 0.348 |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `825e7833-e738-4951-82c8-8785648b9238` | human | 0.348 |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9fd6c34c-8d7a-426e-a6ce-95e4c779c5db` | human | 0.348 |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `84827da5-f4bc-4d11-9561-9bfbae82fcd2` | human | 0.348 |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `a5f2ad75-033a-4ec7-a006-d62b86fe8f3d` | human | 0.348 |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1c82ea56-f40b-4acc-8eab-26b502992d77` | human | 0.348 |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b6bf0c94-d31f-48d8-aba3-7a00a863d735` | human | 0.348 |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `d22c296c-e507-48b2-8ff7-8509e3761902` | human | 0.348 |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `c42d6575-9887-4f5f-a3f5-2ca6e040675b` | human | 0.348 |  |
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
  "content_id": "e3415f21-01e5-465f-8f7a-cbc9e05452f1",
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
  "content_id": "77df0dec-a7fa-45cf-83a0-c75b27c61ab6",
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
  "content_id": "2fedbf2e-997c-43be-80c4-4bac2ed4c1ff",
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
  "content_id": "8a66526f-7607-46b1-b2ca-42974724768e",
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
  "content_id": "f63a4a92-acb6-4f7f-a541-797ef753ed65",
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
  "content_id": "0aa9a735-7d88-49b6-85d7-6c6c8f83d006",
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
  "content_id": "638066bd-6074-4a58-8f08-79f7327c1285",
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
  "content_id": "65f993b4-e59f-4cca-89db-b7ed3e08cbae",
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
  "content_id": "7144f951-fb86-420c-8aea-c479d3f9a0dd",
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
  "content_id": "a95ec52c-30fa-497a-9c34-c5cf7c3a9235",
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
  "content_id": "eb9641dc-15e1-4ff3-b696-16ce93a65366",
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
  "content_id": "78094061-fb17-45fd-a7e6-b954eb7b2c92",
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
  "content_id": "4e50fada-5fd9-4963-8e7a-6171aae4141a",
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
  "content_id": "56c718bf-71c5-4e5e-8a8a-0df163d656c5",
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
  "content_id": "46d7abd3-a0ae-40e2-91b3-8e9cbb50f5cc",
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
  "content_id": "e7896347-fd08-4e16-8ec7-53bb0c382b46",
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
  "content_id": "f786d944-23cb-49a4-8761-939c56131b97",
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
  "content_id": "92bda60b-a184-4ef2-9a69-069a12a40b8e",
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
  "content_id": "7b1c5033-3752-4cd2-81d8-e63a2e7e9ffd",
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
  "content_id": "08c99025-73a3-4309-9d93-c5bdba2c96b6",
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
  "content_id": "038a72c4-4c69-4f8c-b3de-a46dff0a1047",
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
  "content_id": "f0498e19-5dee-43f9-8130-ddef298f53e3",
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
  "content_id": "106e3f4c-fcc9-468f-b5ab-7d92e0c97660",
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
  "content_id": "e8ef6d86-417e-4653-a38d-e6450f19da00",
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
  "content_id": "53215922-c1cd-4980-9545-4f0b6075c9ae",
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
  "content_id": "c1d91bc1-5ad3-425f-8c30-d64df272bc05",
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
  "content_id": "d974eeec-e12d-4509-b117-ea2a5277531a",
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
  "content_id": "6adaea47-fecb-4edc-8c45-bbebaf12ddb8",
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
  "content_id": "825e7833-e738-4951-82c8-8785648b9238",
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
  "content_id": "9fd6c34c-8d7a-426e-a6ce-95e4c779c5db",
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
  "content_id": "84827da5-f4bc-4d11-9561-9bfbae82fcd2",
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
  "content_id": "a5f2ad75-033a-4ec7-a006-d62b86fe8f3d",
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
  "content_id": "1c82ea56-f40b-4acc-8eab-26b502992d77",
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
  "content_id": "b6bf0c94-d31f-48d8-aba3-7a00a863d735",
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
  "content_id": "d22c296c-e507-48b2-8ff7-8509e3761902",
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
  "content_id": "c42d6575-9887-4f5f-a3f5-2ca6e040675b",
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
