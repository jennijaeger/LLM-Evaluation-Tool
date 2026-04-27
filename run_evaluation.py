import json
import time
from datetime import datetime
from pathlib import Path

import pandas as pd

from llm_clients import get_all_clients


RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)


def load_scenarios():
    with open("scenarios.json", "r", encoding="utf-8") as file:
        return json.load(file)


def score_answer(answer, category):
    answer_lower = answer.lower()

    structure_score = 0
    content_score = 0
    length_score = 0

    if 30 <= len(answer) <= 3000:
        length_score = 1

    if category == "code_generation":
        if "def " in answer and "assert" in answer:
            structure_score = 1
        if "return" in answer:
            content_score = 1

    elif category == "bug_fixing":
        if "```" in answer or "def " in answer or "print" in answer:
            structure_score = 1
        if "fehler" in answer_lower or "korrigiert" in answer_lower or ":" in answer:
            content_score = 1

    elif category == "json_output":
        if "{" in answer and "}" in answer:
            structure_score = 1
        if ":" in answer:
            content_score = 1

    elif category == "summarization":
        bullet_count = answer.count("-") + answer.count("•")
        if bullet_count >= 3:
            structure_score = 1
        if len(answer.split()) >= 10:
            content_score = 1

    elif category == "reasoning":
        if any(char.isdigit() for char in answer) or "weil" in answer_lower:
            structure_score = 1
        if "antwort" in answer_lower or "lösung" in answer_lower or "daher" in answer_lower:
            content_score = 1

    total_score = round(
        structure_score * 0.4 +
        content_score * 0.4 +
        length_score * 0.2,
        2
    )

    return {
        "structure_score": structure_score,
        "content_score": content_score,
        "length_score": length_score,
        "total_score": total_score
    }


def run_evaluation():
    scenarios = load_scenarios()
    clients = get_all_clients()

    results = []

    for scenario in scenarios:
        for client in clients:
            print(f"Teste {scenario['id']} mit {client.name}...")

            start_time = time.time()

            try:
                answer = client.generate(scenario["prompt"])
                latency = round(time.time() - start_time, 2)
                scores = score_answer(answer, scenario["category"])

                results.append({
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "scenario_id": scenario["id"],
                    "category": scenario["category"],
                    "model": client.name,
                    "prompt": scenario["prompt"],
                    "answer": answer,
                    "latency_seconds": latency,
                    "structure_score": scores["structure_score"],
                    "content_score": scores["content_score"],
                    "length_score": scores["length_score"],
                    "total_score": scores["total_score"],
                    "status": "success",
                    "error": ""
                })

            except Exception as error:
                latency = round(time.time() - start_time, 2)

                results.append({
                    "timestamp": datetime.now().isoformat(timespec="seconds"),
                    "scenario_id": scenario["id"],
                    "category": scenario["category"],
                    "model": client.name,
                    "prompt": scenario["prompt"],
                    "answer": "",
                    "latency_seconds": latency,
                    "structure_score": 0,
                    "content_score": 0,
                    "length_score": 0,
                    "total_score": 0,
                    "status": "error",
                    "error": str(error)
                })

    df = pd.DataFrame(results)

    output_file = RESULTS_DIR / f"evaluation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    df.to_csv(output_file, index=False)

    print("\nEvaluation abgeschlossen.")
    print(f"Ergebnisse gespeichert in: {output_file}")


if __name__ == "__main__":
    run_evaluation()