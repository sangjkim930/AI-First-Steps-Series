# 9.4 AI는 관람객의 감성을 어떻게 읽을까?

「AI 첫걸음 시리즈」 Vol. 2의 9.4절
**AI는 관람객의 감성을 어떻게 읽을까?** 실습에 사용되는 데이터입니다.

## 데이터 안내

이 폴더에는 IMDb 영화 리뷰를 이용하여 텍스트의 긍정·부정 감성을 분석하는 실습에 필요한 데이터가 포함되어 있습니다.

실습에 사용하는 데이터는 스탠퍼드대학교의 Andrew Maas 연구팀이 공개한 **IMDb Large Movie Review Dataset**을 바탕으로 구성하였습니다. 원본 데이터에는 영화 리뷰와 각 리뷰의 감성 정보가 포함되어 있으며, 감성분석(Sentiment Analysis)의 대표적인 벤치마크 데이터셋으로 널리 활용됩니다.

교재 실습의 편의를 위해 전체 **50,000건의 리뷰**를 하나의 Excel 파일로 통합하였으며, 다음 두 개의 열로 구성되어 있습니다.

* `review` — 영화 리뷰 본문

* `sentiment` — 리뷰의 감성(`positive` 또는 `negative`)

* **데이터셋:** IMDb Large Movie Review Dataset

* **원 데이터 제공:** Stanford University / Andrew Maas 연구팀

* **분석 유형:** 감성분석(Sentiment Analysis), 텍스트 마이닝(Text Mining)

* **용도:** 교육 및 실습

## 제공 파일

* `imdb_reviews.xlsx` — 50,000건의 IMDb 영화 리뷰와 `positive`/`negative` 감성 정보를 하나의 파일로 통합한 교재 실습용 데이터

이 파일은 학습용 데이터와 테스트용 데이터를 하나로 통합한 형태이므로, Orange에서 실습 목적에 따라 원하는 비율로 데이터를 나누어 사용할 수 있습니다.

※ Orange에서 [Text Mining] 관련 위젯이 보이지 않는 경우에는 교재의 **부록 A1 「Orange Text Mining 애드온 설치와 문제 해결」** 을 참고하세요.
