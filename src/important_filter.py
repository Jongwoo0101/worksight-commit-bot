IMPORTANT = [
    "기능 개발",
    "버그 수정",
    "구조 개선"
]


def filter_important(commits):
    return [
        c for c in commits
        if c["category"] in IMPORTANT
    ]