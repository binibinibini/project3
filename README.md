# project3

## 1. 사용자 맞춤형 인체공학 솔루션<br>

사용자의 책상 환경을 촬영한 사진 한 장으로 잘못된 작업 환경을 진단하고, 인체공학적 개선 가이드를 제공하는 서비스입니다.<br>
<br>

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
<br>

## 3. 사용 기술<br>
YOLO(Roboflow), OpenCV, Numpy, Python, Streamlit, GPT 기반 리포트 생성
<br>


## 4. 역할 <br>

Roboflow 객체 라벨링<br>
- Roboflow를 사용해 초기 라벨링 후 객체별 정확도를 확인하며 성능이 낮은 클래스는 추가 데이터를 수집해 증강 및 보강 학습 진행
- 여러 차례 학습에도 개선되지 않는 객체는 제거하여 최종 라벨링 기준을 정교화


YOLO 학습 실험 및 성능 검증 <br>
- YOLO 모델의 성능을 확인하기 위해 epoch, 이미지 사이즈 등 하이퍼파라미터를 조정하며 성능 변화를 실험
- 분석 결과를 바탕으로 일부 클래스는 데이터 추가 수집 또는 클래스 제외를 검토하며 전체 라벨링 기준을 조정했고, 데이터셋 품질을 개선하는 데 기여함


GPT 프롬프트 로직 구현<br>
- YOLO와 Guideline 코드가 생성한 분석 결과를 기반으로, GPT가 사용자 맞춤형 인체공학 리포트를 생성하도록 프롬프트를 설계


UI/UX 설계 및 시스템 연동<br>
- Streamlit 기반 전체 사용자 흐름 설계 및 사용성 개선
- 페이지 간 이동, 버튼 위치, 정보 배치 등 UI/UX 전반을 재정비
- YOLO-인체공학적 가이드라인 코드-GPT 리포트 생성 흐름을 하나의 통합된 파이프라인으로 연결해 서비스 형태로 완성
<br>

## 5. 데이터셋 및 라벨링 과정 <br>

최종 학습 데이터 수<br>
3,460장
<br>

라벨링 객체<br>
screen, monitor support, laptop, keyboard, mouse, desk lamp, window, wrist rest
<br>

Roboflow 라벨링<br>
<img width="374" height="199" alt="image" src="https://github.com/user-attachments/assets/d040a7d8-f0cc-4625-91bd-c7566401de2c" />
<br>


## 6. 인체공학 가이드라인 <br>

- 각종 인체 공학 관련 사이트를 조사하며, 비율 기반의 인체공학적 계산법 생성

<img width="1196" height="484" alt="image" src="https://github.com/user-attachments/assets/92291017-fa70-47d9-81aa-a293e59af4f3" />

<br>

## 7. 결과 <br>

객체별 정확도
<img width="1196" height="550" alt="image" src="https://github.com/user-attachments/assets/8b70f5c1-533a-4413-8ffc-0ca762bae597" />


전체 최종 정확도<br>
75.9 <br>

서비스 흐름<br>
<img width="1071" height="320" alt="image" src="https://github.com/user-attachments/assets/ccd415cf-4252-4a54-bcd9-772dae921371" />

<br>

[발표자료](https://docs.google.com/presentation/d/1MKx2OHbTf_ViDdTwbASfQeyOhodeTja7zB3pLnXR_uc/edit?usp=drive_link)
