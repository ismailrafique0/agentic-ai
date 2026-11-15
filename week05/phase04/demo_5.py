import json
import time
from ollama import chat

MODEL = "qwen2.5-coder:7b"

claims_dataset = [
    {
        "id": 1,
        "claim": (
            "A pipe burst in my house, but I have no repair estimate."
        ),
        "expected_category": "Property Damage",
        "required_missing": [
            "repair estimate",
            "damage extent",
        ],
    },
    {
        "id": 2,
        "claim": (
            "My car was hit in a parking lot, and the other driver left."
        ),
        "expected_category": "Vehicle Damage",
        "required_missing": [
            "incident date",
            "damage details",
        ],
    },
    {
        "id": 3,
        "claim": (
            "My laptop was stolen from my office, but I have no police report."
        ),
        "expected_category": "Theft",
        "required_missing": [
            "police report",
            "theft date",
        ],
    },
    {
        "id": 4,
        "claim": (
            "I paid for an emergency hospital visit after an accident."
        ),
        "expected_category": "Medical Expense",
        "required_missing": [
            "medical bill",
            "accident details",
        ],
    },
    {
        "id": 5,
        "claim": (
            "A storm damaged the roof of my house yesterday."
        ),
        "expected_category": "Property Damage",
        "required_missing": [
            "damage estimate",
            "damage extent",
        ],
    },
]


def original_prompt(claim: str) -> str:
    return f"""
Classify this insurance claim and identify missing information.

Claim: {claim}

Return JSON with:
- category
- summary
- missing_information (list)
"""


def enhanced_prompt(claim: str) -> str:
    return f"""
You are a preliminary insurance-claim triage assistant.

Classify the claim and identify missing information.

Allowed categories: Property Damage, Vehicle Damage, Medical Expense, Theft, Other.

Rules:
- Select exactly one category from the allowed list.
- Do not invent facts that are not in the claim.
- Do not approve or deny the claim.
- If the available information is insufficient, explain what is missing.
- Recommend human review when appropriate.

Claim:
{claim}

Return JSON with:
- category
- summary
- missing_information (list)
- human_review_recommendation (Yes/No)
"""


def run_model(prompt: str) -> tuple[str, float]:
    start = time.perf_counter()

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format="json",
        options={"temperature": 0},
    )

    latency_seconds = time.perf_counter() - start
    return response.message.content, latency_seconds


with open("results.jsonl", "w", encoding="utf-8") as output_file:
    for item in claims_dataset:
        for version, prompt_function in [
            ("original", original_prompt),
            ("enhanced", enhanced_prompt),
        ]:
            raw_output, latency = run_model(
                prompt_function(item["claim"])
            )

            record = {
                "id": item["id"],
                "version": version,
                "expected_category": item["expected_category"],
                "required_missing": item["required_missing"],
                "claim": item["claim"],
                "raw_output": raw_output,
                "latency_seconds": round(latency, 3),
            }

            output_file.write(
                json.dumps(record, ensure_ascii=False) + "\n"
            )

            print(
                f"Claim {item['id']} | {version} | "
                f"{latency:.2f}s"
            )
            print(raw_output)
            print("-" * 60)