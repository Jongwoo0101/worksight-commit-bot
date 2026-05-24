from pathlib import Path

STATE_FILE = Path("state/last_sha.txt")


def load_last_sha():
    if not STATE_FILE.exists():
        return None

    return STATE_FILE.read_text().strip()


def save_last_sha(sha):
    STATE_FILE.parent.mkdir(exist_ok=True)
    STATE_FILE.write_text(sha)