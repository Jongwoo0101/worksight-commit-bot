from collections import defaultdict


def build_timeline(commits):
    timeline = defaultdict(list)

    for c in commits:
        timeline[c["date"]].append(c["summary"])

    return dict(timeline)