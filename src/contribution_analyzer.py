from collections import Counter


def analyze_contributions(commits):
    authors = [c["author"] for c in commits]
    return dict(Counter(authors))