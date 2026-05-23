import streamlit as st
from src.github_collector import fetch_commits
from src.commit_classifier import classify_commits
from src.csv_exporter import export_csv

st.title("WorkSight Commit Bot")

repo = st.text_input(
    "GitHub Repo",
    "Jongwoo0101/genai-team-project"
)

if st.button("Generate"):
    commits = fetch_commits(repo)
    classified = classify_commits(commits)

    export_csv(classified)

    st.success("완료!")
    st.write(f"{len(commits)} commits collected")
    st.download_button(
        "CSV 다운로드",
        open("data/commit_report.csv", "rb"),
        file_name="commit_report.csv"
    )