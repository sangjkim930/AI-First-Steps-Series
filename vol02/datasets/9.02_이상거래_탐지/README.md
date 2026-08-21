# 9.2 은행은 이상거래를 어떻게 찾을까?

「AI 첫걸음 시리즈」 Vol. 2의 9.2절
**은행은 이상거래를 어떻게 찾을까?** 실습에 사용되는 데이터 안내입니다.

## 데이터 안내

이번 실습에서는 신용카드 거래에서 정상 거래와 이상거래를 구분하는 이상 탐지(Anomaly Detection) 실습을 진행합니다.

실습에 사용하는 데이터는 벨기에 브뤼셀자유대학교(ULB) 머신러닝 그룹이 공개한 **Credit Card Fraud Detection** 데이터셋입니다. 이 데이터에는 2013년 9월 유럽 카드사용자의 이틀간 거래 **284,807건**이 포함되어 있으며, 이상 탐지 연구에서 대표적으로 활용되는 벤치마크 데이터셋입니다.

* **데이터셋:** Credit Card Fraud Detection
* **원본 파일:** `creditcard.csv`
* **출처:** Kaggle / ULB Machine Learning Group
* **Kaggle 주소:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud
* **분석 유형:** 이상 탐지(Anomaly Detection)
* **용도:** 교육 및 실습

## 데이터 다운로드

`creditcard.csv`는 파일 용량이 크기 때문에 이 GitHub 저장소에서는 직접 제공하지 않습니다.

위의 Kaggle 페이지에서 원본 데이터를 다운로드한 후, 압축을 해제하여 `creditcard.csv` 파일을 Orange의 [File] 위젯에서 불러와 사용합니다.

※ 원본 데이터와 변수에 대한 자세한 설명은 Kaggle 데이터 페이지에서 확인할 수 있습니다.
