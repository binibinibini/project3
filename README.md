# project3

## 1. 사용자 맞춤형 인체공학 솔루션<br>

사용자의 책상 환경을 촬영한 사진 한 장으로 잘못된 작업 환경을 진단하고, 인체공학적 개선 가이드를 제공하는 서비스입니다.<br>

## 2. 프로젝트 개요

사용자의 책상 이미지를 기반으로 업무 환경을 분석하고, 인체공학적 관점에서 개선이 필요한 요소를 찾아 맞춤형 가이드를 제공하는 AI 데스크 분석 서비스입니다. 재택근무 확산으로 장시간 컴퓨터 사용이 일상이 되면서 거북목, 손목 통증 등 VDT 증후군을 겪는 사람들이 늘어나고 있지만, 자신의 작업환경이 어떤 문제를 갖고 있는지 정확히 알기 어려운 상황입니다.
이에 YOLO 기반 객체 인식 기술로 모니터와 키보드 등 책상 구성 요소를 감지하고, 사용자 신체 정보와 인체공학 기준을 결합해 모니터 높이, 시청 거리 등의 위험도를 산출합니다. GPT가 분석 결과를 이해하기 쉬운 문장으로 제시해, 사용자가 단 몇 번의 클릭만으로 자신의 작업환경을 진단하고 개선 방향을 확인할 수 있도록 돕습니다. <br>
프로젝트 최종 목표는 누구나 손쉽게 접근할 수 있는 AI 코칭을 통해 통증을 예방하고 작업 효율을 높이며, 생활 속에서 직접적인 변화를 체감할 수 있는 솔루션을 목표로 합니다.

[카테고리 목록](https://docs.google.com/spreadsheets/d/1tteyq5jXOqYlGVjmUWLDkb59NdvOc6gyuN06nWfIHwU/edit?usp=drive_link)

[데이터 수집](https://drive.google.com/drive/folders/1Cpmg6iK_5-4j9rLjQ5uu2IoLHG59iPYU?usp=drive_link)

[모니터 높이 공식 산출 데이터](https://docs.google.com/spreadsheets/d/1CKce8DtY3HxBoi0hGiNBAbWmlRsmGDXbWE2uwdYXi98/edit?usp=drive_link)

[참고한 논문](https://drive.google.com/drive/folders/1GK4rzccEKPsFuCcLOu4epIGrE5LShO8m?usp=drive_link)

[웹 시연 영상](https://drive.google.com/file/d/1SkuHXsg7MpjtQxo13PyvC6Rwkds4LHaY/view?usp=drive_link)

[전체 코드](https://github.com/binibinibini/project3.git)

## 3. 사용 기술<br>
YOLO(Roboflow), OpenCV, Numpy, Python, Streamlit, GPT 기반 리포트 생성


## 4. 역할 <br>
로보플로우 객체 라벨링<br>

YOLO 학습 코드 작성 (?)<br>

GPT 프롬프트 로직 구현<br>

UI/UX 설계 및 시스템 연동<br>







5️⃣ 데이터셋 및 라벨링 과정

총 수집량 → 정제 → 증강 → 최종 학습 데이터 수

라벨링 기준 정립 과정과 클래스 종류

데이터 불균형 해결 노력

Roboflow 사용법 요약(캡처 이미지 있으면 굿!)

6️⃣ 인체공학 가이드라인 설명 (대표 2~3개만 상세하게)

Cornell, 사이즈코리아 근거 명시

비율 기반 계산 방식이 핵심 포인트

JSON 형태 결과 예시 첨부

7️⃣ 모델 성능

mAP, 각 클래스별 정확도 그래프

Before/After 개선 시각 자료














## 5. 결과 & 성과 <br>
정확도<br>
75.9 <br>

서비스 흐름<br>
<img width="1071" height="320" alt="image" src="https://github.com/user-attachments/assets/ccd415cf-4252-4a54-bcd9-772dae921371" />


[발표자료](https://docs.google.com/presentation/d/1MKx2OHbTf_ViDdTwbASfQeyOhodeTja7zB3pLnXR_uc/edit?usp=drive_link)
