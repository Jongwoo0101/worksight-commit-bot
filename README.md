# WorkSight Commit Bot

> GitHub 커밋 로그를 자동 분석하여  
> **개발 과정 요약, 팀원 기여도, 타임라인, PPT 보고서**를 생성하고,  
> **새로운 변경사항을 지속적으로 추적하는 AI 기반 기획 보조 도구**

---

## Overview

**WorkSight Commit Bot**은 GitHub Repository의 커밋 내역을 자동 수집하고 분석하여:

- 커밋 분류
- 중요 커밋 추출
- 팀원별 기여도 분석
- 개발 타임라인 생성
- CSV 보고서 생성
- PPT 자동 생성
- 새로운 커밋만 자동 감지 및 누적 저장
- 변경 로그 기반 자동 커밋 메시지 생성


---

## Features

### 1. GitHub Commit Collection

GitHub Repository의 커밋 내역을 자동 수집합니다.

수집 정보:

- Commit SHA
- Author
- Date
- Commit Message
- Merge 여부

---

### 2. Incremental Update Tracking

처음 실행 시 전체 커밋을 저장하고,  
이후 실행부터는 **새롭게 추가된 커밋만 감지**합니다.

```text
처음 실행 → 169개 저장
다음 실행 → 새 커밋 2개 발견
결과 → 총 171개 유지
```

내부적으로 마지막 처리한 SHA를 저장합니다.

```text
state/last_sha.txt
```

---

### 3. Commit Classification

커밋 메시지를 자동 분류합니다.

| Prefix | Category |
|---|---|
| `feat:` | 기능 개발 |
| `fix:` | 버그 수정 |
| `refactor:` | 구조 개선 |
| `docs:` | 문서 작업 |
| `test:` | 테스트 |
| 기타 | 기타 |

---

### 4. Important Commit Filtering

중요한 커밋만 자동 추출합니다.

포함:

- 기능 개발
- 버그 수정
- 구조 개선

제외:

- chore
- merge noise
- 기타 불필요한 로그

---

### 5. Contribution Analysis

팀원별 커밋 수를 분석합니다.

예시:

```text
원종우: 52 commits
TeammateA: 31 commits
TeammateB: 18 commits
```

---

### 6. Development Timeline

날짜별 커밋을 기반으로 개발 흐름을 자동 생성합니다.

예시:

```text
2026-05-01 → 로그인 기능 구현
2026-05-03 → 게시판 기능 개발
2026-05-07 → 화상회의 기능 추가
```

---

### 7. CSV Export

분석 결과를 CSV로 저장합니다.

기존 데이터를 유지하면서 **새 커밋만 append**합니다.

생성 파일:

```bash
data/commit_report.csv
```

---

### 8. PPT Report Generation

프로젝트 발표용 PPT를 자동 생성합니다.

포함 내용:

- 프로젝트 제목
- 팀원 기여도
- 개발 타임라인
- 중요 커밋 목록
- Merge PR 표시

생성 파일:

```bash
data/commit_report.pptx
```

---

### 9. Auto Changelog Commit 

새로운 변경사항이 감지되면,  
**WorkSight Commit Bot 자체 레포에도 자동으로 커밋**합니다.

예시:

```text
feat: target repo 신규 커밋 3건 반영
- fix: handleJoinRoom bug 작성자: 원종우 코드: a3f91bc
- feat: refresh token 작성자: 원종우 코드: b72de11
```

---

### 10. Streamlit Web UI

브라우저에서 GitHub Repository URL만 입력하면 자동 생성 가능합니다.

---

## Project Structure

```text
worksight-commit-bot/
├── app.py
├── requirements.txt
├── ui.py
├── src/
│   ├── github_collector.py
│   ├── commit_classifier.py
│   ├── contribution_analyzer.py
│   ├── timeline_analyzer.py
│   ├── important_filter.py
│   ├── csv_exporter.py
│   ├── ppt_exporter.py
│   ├── state_manager.py
│   ├── changelog_generator.py
│   └── git_auto_commit.py
├── data/
└── state/
    └── last_sha.txt
```

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/your-username/worksight-commit-bot.git
cd worksight-commit-bot
```

---

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### CLI Mode

`app.py`에서 Repository를 지정합니다.

```python
REPO_NAME = "Jongwoo0101/genai-team-project"
```

실행:

```bash
python app.py
```

결과:

```text
data/
├── commit_report.csv
└── commit_report.pptx
```

---

### Web UI Mode

실행:

```bash
streamlit run ui.py
```

브라우저에서:

1. GitHub Repository 입력
2. Generate 클릭
3. CSV 다운로드

---

## Workflow

```text
Target Repository 변경 감지
        ↓
새 커밋 수집
        ↓
커밋 분류 및 분석
        ↓
CSV / PPT 업데이트
        ↓
last_sha 저장
        ↓
WorkSight Commit Bot 자동 커밋
```

---

## Tech Stack

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="50" height="50"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="50" height="50"/>
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.png" width="50" height="50"/>
  <img src="https://cdn-icons-png.flaticon.com/512/888/888871.png" width="50" height="50"/>
  <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="50" height="50"/>
</p>

