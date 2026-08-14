# 10.4 합격 예측

「AI 첫걸음 시리즈」 Vol. 1의 10.4절
**합격 예측: 입시의 과학** 실습에 사용되는 데이터입니다.

## 데이터 안내

이 폴더에는 대학원 지원자의 정보를 이용하여 합격 가능성을 예측하는 실습에 필요한 데이터가 포함되어 있습니다.

원본 데이터는 Kaggle의 **Graduate Admission 2** 데이터셋에서 다운로드하였으며, 교재의 실습을 위해 원본 데이터를 변형하거나 새로운 예측용 데이터를 추가한 파일도 함께 제공합니다.

* **원본 데이터셋:** Graduate Admission 2
* **출처:** Kaggle
* **Kaggle 주소:** https://www.kaggle.com/datasets/mohansacharya/graduate-admissions
* **용도:** 교육 및 실습

## 제공 파일

* `Admission_Predict_Ver1.1.csv` — Kaggle에서 제공하는 원본 데이터
* `Admission_Predict_binary.csv` — 합격 가능성의 기준값을 **0.85**로 설정하여 이진 분류 실습용으로 변환한 데이터
* `Admission_Predict_new.csv` — 학습된 모델을 이용하여 **새로운 지원자의 합격 여부를 예측**하기 위한 데이터
* `Admission_Predict_thresholds.csv` — **여러 기준값(threshold)**을 적용하여 분류 결과의 변화를 비교하기 위한 실습 데이터

※ `Admission_Predict_binary.csv`, `Admission_Predict_new.csv`, `Admission_Predict_thresholds.csv`는 교재의 실습을 위해 가공하거나 별도로 구성한 데이터입니다.

