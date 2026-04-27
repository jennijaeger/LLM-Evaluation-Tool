from pathlib import Path
import pandas as pd


RESULTS_DIR = Path("results")


def get_latest_result_file():
    files = sorted(RESULTS_DIR.glob("evaluation_*.csv"))

    if not files:
        raise FileNotFoundError(
            "No evaluation files found in results directory."
        )

    return files[-1]


def analyze_results():
    file_path = get_latest_result_file()

    print("\nAnalyzing file:")
    print(file_path)

    df = pd.read_csv(file_path)

    print("\n" + "=" * 60)
    print("Average Score per Model")
    print("=" * 60)

    print(
        df.groupby("model")["total_score"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n" + "=" * 60)
    print("Average Latency per Model (seconds)")
    print("=" * 60)

    print(
        df.groupby("model")["latency_seconds"]
        .mean()
        .sort_values()
    )

    print("\n" + "=" * 60)
    print("Average Score per Category")
    print("=" * 60)

    print(
        df.groupby("category")["total_score"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n" + "=" * 60)
    print("Error Count per Model")
    print("=" * 60)

    errors = df[df["status"] == "error"]

    if len(errors) > 0:
        print(errors.groupby("model").size())
    else:
        print("No errors recorded.")


if __name__ == "__main__":
    analyze_results()