# 10.10 집값 예측

「AI 첫걸음 시리즈」 Vol. 1의 10.10절
**집값 예측: 부동산 전문가 되기** 실습에 사용되는 데이터 안내입니다.

## 데이터 안내

이번 실습에서는 Kaggle의 **House Prices - Advanced Regression Techniques** 대회에서 제공하는 데이터를 사용합니다.

대회 데이터는 이 GitHub 저장소에서 직접 제공하지 않습니다. 아래 Kaggle 대회 페이지에 접속하여 **[Join Competition]**을 클릭하고 대회 규칙에 동의한 후, **[Data]** 탭에서 직접 다운로드하여 사용합니다.

* **데이터셋:** House Prices - Advanced Regression Techniques
* **출처:** Kaggle Competition
* **Kaggle 주소:** https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques
* **분석 유형:** 회귀(Regression)
* **용도:** 교육 및 실습

## 다운로드 파일

데이터를 다운로드하면 다음과 같은 파일이 제공됩니다.

* `train.csv` — 모델 학습 및 평가에 사용하는 데이터
* `test.csv` — 학습된 모델을 이용하여 집값을 예측하는 데이터
* `data_description.txt` — 각 변수에 대한 상세 설명
* `sample_submission.csv` — Kaggle 제출 파일의 형식 예시

이번 실습에서는 `train.csv`와 `test.csv`를 직접 사용합니다. 모델 생성과 평가는 `train.csv`를 이용하고, 이후 새로운 데이터에 대한 예측 단계에서는 `test.csv`를 사용합니다.

※ Kaggle 대회 데이터는 이 저장소에 포함하지 않으므로, 위의 Kaggle 대회 페이지에서 직접 다운로드해 주세요.
