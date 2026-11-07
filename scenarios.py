"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "human-writing samples",
        "criterion": 1,
        # Original first-person samples written for this evaluation.
        "texts": [
            "I missed the first bus again, which was annoying, but the walk gave me time to wake up.",
            "My coffee went cold beside the laptop while I chased one small bug through the afternoon.",
            "I found an old receipt in my coat pocket and spent far too long trying to remember that day.",
            "The rain started before I reached the corner, so I waited under an awning with a stranger.",
            "I kept changing the title of the document because none of the words felt quite right.",
            "There was a crooked label on the storage box, and somehow that made the whole closet look untidy.",
            "I called my sister on the way home; we talked about dinner, work, and nothing important.",
            "The library was nearly empty except for a child turning pages loudly in the next aisle.",
            "I watered the plant, forgot about it, and then checked the soil again ten minutes later.",
            "By evening I had finished less than planned, but the one finished thing was finally understandable.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            (
                "The implementation of the proposed framework requires careful "
                "consideration of several key factors. The system processes inputs "
                "consistently and produces reliable results."
            ),
            "I walked home in the rain and noticed a blue bird beside the road.",
            "The system seems useful, but I am not sure how well it works in practice.",
        ],
    },
    {
        "name": "score separation",
        "criterion": 3,
        "texts": [
            (
                "The implementation of the proposed framework requires careful "
                "consideration of several key factors. First, the system must "
                "handle a wide variety of inputs and provide consistent results."
            ),
            (
                "I took the longer path home because the usual street was closed. "
                "A neighbor was watering flowers, and we talked briefly before I "
                "continued toward the station."
            ),
        ],
    },
    {
        "name": "appeal path prerequisite",
        "criterion": 4,
        "texts": [
            "This is an original submission created for testing the appeal workflow.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
