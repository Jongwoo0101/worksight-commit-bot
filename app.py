from src.github_collector import fetch_commits
from src.commit_classifier import classify_commits
from src.contribution_analyzer import analyze_contributions
from src.timeline_analyzer import build_timeline
from src.important_filter import filter_important
from src.csv_exporter import export_csv
from src.ppt_exporter import export_ppt

REPO_NAME = "Jongwoo0101/genai-team-project"


def main():
    print("GitHub 커밋 수집 중...")
    commits = fetch_commits(REPO_NAME)

    print("분류 중...")
    classified = classify_commits(commits)

    print("중요 커밋 필터링...")
    important = filter_important(classified)

    print("기여도 분석...")
    contributions = analyze_contributions(classified)

    print("타임라인 생성...")
    timeline = build_timeline(classified)

    print("CSV 생성...")
    export_csv(classified)

    print("PPT 생성...")
    export_ppt(
        important,
        contributions,
        timeline
    )

    print("완료!")


if __name__ == "__main__":
    main()