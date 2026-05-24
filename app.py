from src.github_collector import fetch_commits
from src.commit_classifier import classify_commits
from src.contribution_analyzer import analyze_contributions
from src.timeline_analyzer import build_timeline
from src.important_filter import filter_important
from src.csv_exporter import export_csv
from src.ppt_exporter import export_ppt

# 추가
from src.state_manager import save_last_sha
from src.changelog_generator import build_commit_message
from src.git_auto_commit import commit_changes


REPO_NAME = "Jongwoo0101/genai-team-project"


def main():
    print("GitHub 커밋 수집 중...")
    commits = fetch_commits(REPO_NAME)

    # 새 커밋 없으면 종료
    if not commits:
        print("새로운 커밋이 없습니다.")
        return

    print(f"새 커밋 {len(commits)}개 발견")

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
        classified,
        contributions,
        timeline
    )

    # 마지막 처리 SHA 저장
    latest_sha = commits[0]["sha"]
    save_last_sha(latest_sha)
    print(f"마지막 SHA 저장 완료: {latest_sha}")

    # 자동 커밋 메시지 생성
    print("변경 로그 생성...")
    commit_message = build_commit_message(commits)

    if commit_message:
        print("봇 레포 자동 커밋 중...")
        commit_changes(commit_message)

    print("완료!")


if __name__ == "__main__":
    main()