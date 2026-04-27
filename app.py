from pathlib import Path

import pandas as pd
import streamlit as st


RESULTS_DIR = Path("results")


def get_result_files():
    return sorted(RESULTS_DIR.glob("evaluation_*.csv"), reverse=True)


st.set_page_config(
    page_title="LLM Evaluation Dashboard",
    layout="wide"
)

st.title("LLM Evaluation Dashboard")
st.write("Comparison of GPT, Claude and Gemini across practical benchmark scenarios.")

result_files = get_result_files()

if not result_files:
    st.warning("No evaluation result files found.")
    st.stop()

selected_file = st.selectbox(
    "Select evaluation result file",
    result_files,
    format_func=lambda file: file.name
)

df = pd.read_csv(selected_file)

st.subheader("Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Tests", len(df))
col2.metric("Average Score", round(df["total_score"].mean(), 3))
col3.metric("Average Latency", round(df["latency_seconds"].mean(), 2))

st.subheader("Average Score per Model")
score_by_model = (
    df.groupby("model")["total_score"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(score_by_model)

st.subheader("Average Latency per Model")
latency_by_model = (
    df.groupby("model")["latency_seconds"]
    .mean()
    .sort_values()
)

st.bar_chart(latency_by_model)

st.subheader("Average Score per Category")
score_by_category = (
    df.groupby("category")["total_score"]
    .mean()
    .sort_values(ascending=False)
)

st.bar_chart(score_by_category)

st.subheader("Detailed Results")
st.dataframe(df, use_container_width=True)

st.subheader("Inspect Individual Answer")

selected_index = st.selectbox(
    "Select row",
    df.index,
    format_func=lambda index: f"{df.loc[index, 'scenario_id']} - {df.loc[index, 'model']}"
)

st.markdown("### Prompt")
st.write(df.loc[selected_index, "prompt"])

st.markdown("### Answer")
st.write(df.loc[selected_index, "answer"])

st.markdown("### Scores")

score_cols = [
    "structure_score",
    "content_score",
    "length_score",
    "total_score",
    "latency_seconds"
]

st.dataframe(
    df.loc[[selected_index], score_cols],
    use_container_width=True
)