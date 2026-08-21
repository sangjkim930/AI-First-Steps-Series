# 8.5 리뷰 속 숨은 주제를 찾아라

「AI 첫걸음 시리즈」 Vol. 2의 8.5절
**리뷰 속 숨은 주제를 찾아라: 토픽모델링** 실습에 사용되는 데이터입니다.

## 데이터 안내

이 폴더에는 아마존 제품 리뷰를 이용하여 리뷰 속에 숨어 있는 주요 주제를 찾아보는 토픽모델링 실습에 필요한 데이터가 포함되어 있습니다.

원본 데이터는 Kaggle의 **Amazon Product Reviews Dataset**에서 다운로드할 수 있습니다. 이 데이터셋에는 킨들, 파이어 태블릿, 파이어 TV, 에코 닷, 각종 액세서리 등 다양한 아마존 전자제품에 대해 고객이 작성한 리뷰와 제품 관련 정보가 포함되어 있습니다.

원본 파일 `7817_1.csv`에는 제품 ID, 브랜드, 카테고리, 가격, 리뷰 본문, 평점, 작성자, 작성일 등 다양한 정보가 포함되어 있습니다. 이번 실습에서는 리뷰 본문의 잠재적인 주제를 분석하는 데 초점을 맞추기 위해 중복 리뷰와 비영어 리뷰를 제거하는 등의 전처리를 수행한 데이터를 사용합니다.

* **데이터셋:** Amazon Product Reviews Dataset
* **원본 파일:** `7817_1.csv`
* **출처:** Kaggle
* **Kaggle 주소:** https://www.kaggle.com/datasets/yasserh/amazon-product-reviews-dataset
* **분석 유형:** 토픽모델링(Topic Modeling)
* **용도:** 교육 및 실습

## 제공 파일

* `amazon_reviews_processed.xlsx` — 원본 Amazon Product Reviews Dataset에서 중복 리뷰와 비영어 리뷰 등을 제거하여 토픽모델링 실습에 사용할 수 있도록 전처리한 데이터

원본 데이터가 필요한 경우 위의 Kaggle 페이지에서 `7817_1.csv` 파일을 직접 다운로드할 수 있습니다.

※ Orange에서 [Text Mining] 관련 위젯이 보이지 않는 경우에는 교재의 **부록 A1 「Orange Text Mining 애드온 설치와 문제 해결」** 을 참고하세요.
