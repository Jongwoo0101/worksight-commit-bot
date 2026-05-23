def classify_message(msg):
    lower = msg.lower()

    if lower.startswith("feat"):
        return "기능 개발"

    if lower.startswith("fix"):
        return "버그 수정"

    if lower.startswith("refactor"):
        return "구조 개선"

    if lower.startswith("docs"):
        return "문서 작업"

    if lower.startswith("test"):
        return "테스트"

    return "기타"


def summarize_message(msg):
    msg = msg.replace("feat:", "")
    msg = msg.replace("fix:", "")
    msg = msg.replace("refactor:", "")
    msg = msg.replace("docs:", "")
    msg = msg.replace("test:", "")
    msg = msg.strip()

    return msg


def classify_commits(commits):
    result = []

    for c in commits:
        category = classify_message(c["message"])
        summary = summarize_message(c["message"])

        result.append({
            "date": c["date"],
            "author": c["author"],
            "category": category,
            "summary": summary,
            "sha": c["sha"],

            # 추가!!
            "is_merge": c["is_merge"]
        })

    return result