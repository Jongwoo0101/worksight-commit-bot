from github import Github


def fetch_commits(repo_name):
    g = Github()
    repo = g.get_repo(repo_name)

    commits = []

    for commit in repo.get_commits():
        msg = commit.commit.message.strip()

        commits.append({
            "sha": commit.sha[:7],
            "author": commit.commit.author.name,
            "date": commit.commit.author.date.strftime("%Y-%m-%d"),
            "message": msg,
            "is_merge": "merge pull request" in msg.lower()
        })

    return commits