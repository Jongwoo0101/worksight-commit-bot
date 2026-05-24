def build_commit_message(commits):
    if not commits:
        return None

    lines = []
    lines.append(
        f"feat: target repo 신규 커밋 {len(commits)}건 반영"
    )

    for c in commits[:5]:
        lines.append(
            f"- {c['message']} "
            f"작성자: {c['author']} "
            f"코드: {c['sha']}"
        )

    return "\n".join(lines)