import os
import pandas as pd


def export_csv(data):
    # data 폴더 없으면 생성
    os.makedirs("data", exist_ok=True)

    df = pd.DataFrame(data)

    df.to_csv(
        "data/commit_report.csv",
        index=False,
        encoding="utf-8-sig"
    )