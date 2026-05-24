from github import Github
from src.state_manager import load_last_sha


def fetch_commits(repo_name):
    g = Github()
    repo = g.get_repo(repo_name)

    last_sha = load_last_sha()

    commits = []

    for commit in repo.get_commits():
        sha = commit.sha[:7]

        if sha == last_sha:
            break

        msg = commit.commit.message.strip()

        commits.append({
            "sha": sha,
            "author": commit.commit.author.name,
            "date": commit.commit.author.date.strftime("%Y-%m-%d"),
            "message": msg,
            "is_merge": "merge pull request" in msg.lower()
        })

    return commits