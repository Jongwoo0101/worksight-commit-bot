import os
from pptx import Presentation


def export_ppt(commits, contributions, timeline):
    os.makedirs("data", exist_ok=True)

    prs = Presentation()

    # 제목
    slide = prs.slides.add_slide(prs.slide_layouts[0])
    slide.shapes.title.text = "개발 과정 요약"
    slide.placeholders[1].text = "GitHub Commit 기반 자동 생성"

    # 팀원 기여도
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "팀원 기여도"

    text = ""
    for author, count in contributions.items():
        text += f"{author}: {count} commits\n"

    slide.placeholders[1].text = text

    # 타임라인
    slide = prs.slides.add_slide(prs.slide_layouts[1])
    slide.shapes.title.text = "개발 타임라인"

    text = ""
    for date, items in list(timeline.items())[:10]:
        text += f"{date}\n"
        text += f"- {items[0]}\n\n"

    slide.placeholders[1].text = text

    # 중요 커밋
    for commit in commits[:10]:
        slide = prs.slides.add_slide(prs.slide_layouts[1])

        title = commit["category"]

        if commit.get("is_merge", False):
            title += " (PR Merge)"

        slide.shapes.title.text = title

        body = (
            f"{commit['date']}\n"
            f"{commit['author']}\n"
            f"{commit['summary']}"
        )

        slide.placeholders[1].text = body

    prs.save("data/commit_report.pptx")