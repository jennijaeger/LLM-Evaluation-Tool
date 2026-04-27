from llm_clients import get_all_clients
import pandas as pd

prompt = """
Schreibe eine Python-Funktion, die prüft, ob ein Wort ein Palindrom ist.
Füge außerdem 3 kurze Unit-Tests hinzu.
"""

clients = get_all_clients()

results = []

for client in clients:

    print("=" * 60)
    print(f"Modell: {client.name}")
    print("=" * 60)

    answer = client.generate(prompt)

    print(answer)
    print()

    results.append({
        "model": client.name,
        "prompt": prompt,
        "answer": answer
    })


# -------- speichern --------

df = pd.DataFrame(results)

df.to_csv(
    "results_single_prompt.csv",
    index=False
)

print("\nErgebnisse gespeichert in:")
print("results_single_prompt.csv")