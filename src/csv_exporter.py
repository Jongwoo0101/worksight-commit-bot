import os
import pandas as pd


OUTPUT_PATH = "data/commit_report.csv"


def export_csv(new_data):
    os.makedirs("data", exist_ok=True)

    new_df = pd.DataFrame(new_data)

    # 기존 CSV 있으면 읽기
    if os.path.exists(OUTPUT_PATH):
        old_df = pd.read_csv(OUTPUT_PATH)

        # 기존 + 새 데이터 합치기
        combined = pd.concat(
            [new_df, old_df],
            ignore_index=True
        )

        # sha 기준 중복 제거
        combined = combined.drop_duplicates(
            subset=["sha"]
        )

    else:
        combined = new_df

    # 최신순 정렬
    combined = combined.sort_values(
        by="date",
        ascending=False
    )

    combined.to_csv(
        OUTPUT_PATH,
        index=False,
        encoding="utf-8-sig"
    )

    print(
        f"CSV 저장 완료 "
        f"(총 {len(combined)}개 커밋)"
    )