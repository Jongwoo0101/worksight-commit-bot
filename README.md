# WorkSight Commit Bot

> GitHub 커밋 로그를 자동 분석하여  
> **개발 과정 요약, 팀원 기여도, 타임라인, PPT 보고서**를 생성하는 AI 기반 기획 보조 도구

---

## Overview

프로젝트 발표나 PPT 제작 시, GitHub의 수많은 커밋 로그를 직접 읽고 정리하는 것은 많은 시간이 듭니다.

**WorkSight Commit Bot**은 GitHub Repository의 커밋 내역을 자동 수집하고 분석하여:

- 커밋 분류
- 중요 커밋 추출
- 팀원별 기여도 분석
- 개발 타임라인 생성
- CSV 보고서 생성
- PPT 자동 생성

까지 한 번에 수행합니다.

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

### 2. Commit Classification

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

### 3. Important Commit Filtering

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

### 4. Contribution Analysis

팀원별 커밋 수를 분석합니다.

예시:

```text
WonJongU: 52 commits
TeammateA: 31 commits
TeammateB: 18 commits
```

---

### 5. Development Timeline

날짜별 커밋을 기반으로 개발 흐름을 자동 생성합니다.

예시:

```text
2026-05-01 → 로그인 기능 구현
2026-05-03 → 게시판 기능 개발
2026-05-07 → 화상회의 기능 추가
```

---

### 6. CSV Export

분석 결과를 CSV로 저장합니다.

생성 파일:

```bash
data/commit_report.csv
```

---

### 7. PPT Report Generation

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

### 8. Streamlit Web UI

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
│   └── ppt_exporter.py
└── data/
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

## Tech Stack

### Language

- Python 3.11

### Libraries

- PyGithub
- pandas
- python-pptx
- streamlit

---

## Example Output

### CSV

```csv
date,author,category,summary
2026-05-20,Won,버그 수정,handleJoinRoom 오류 수정
2026-05-21,Won,기능 개발,화상회의 기능 구현
```

---

### PPT

자동 생성되는 발표 자료 예시:

- 개발 과정 요약
- 팀원 기여도
- 개발 타임라인
- 중요 커밋 정리

---

## Future Improvements

- GitHub Pull Request 상세 분석
- Commit Keyword 기반 기능별 그룹화
- 커밋 메시지 자연어 요약 AI
- GitLab 지원
- Notion Export
- Jira Integration
- PPT 디자인 템플릿 개선

---

## Motivation

> GitHub의 커밋 로그를  
> **기획자가 바로 사용할 수 있는 개발 스토리**로 변환한다.

WorkSight Commit Bot은  
개발자와 기획자 사이의 정보 격차를 줄이고,  
프로젝트 발표 준비 시간을 크게 단축시키는 것을 목표로 합니다.
