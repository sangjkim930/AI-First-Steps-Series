# 9.3 마트는 왜 맥주와 기저귀를 함께 진열할까?

「AI 첫걸음 시리즈」 Vol. 2의 9.3절
**마트는 왜 맥주와 기저귀를 함께 진열할까?** 실습에 사용되는 데이터입니다.

## 데이터 안내

이번 실습에서는 온라인 소매업체의 실제 구매 기록을 이용하여 함께 구매되는 상품의 패턴을 찾는 연관분석을 수행합니다.

원본 데이터는 UCI Machine Learning Repository에서 제공하는 **Online Retail II** 데이터셋입니다. 이 데이터에는 영국 소재 온라인 소매업체가 2009년 12월부터 2011년 12월까지 기록한 구매 내역이 포함되어 있습니다.

이번 실습에서는 원본 데이터 가운데 **2011년 11월 영국(United Kingdom) 거래**만 선택하고, 취소 거래와 분석에 적합하지 않은 기록을 제거한 데이터를 사용합니다. 이후 거래별로 구매한 상품을 정리하여 Orange의 연관분석에 사용할 수 있는 형태로 변환합니다.

* **데이터셋:** Online Retail II
* **원 데이터 출처:** UCI Machine Learning Repository
* **DOI:** https://doi.org/10.24432/C5CG6D
* **라이선스:** CC BY 4.0
* **분석 유형:** 연관분석(Association Analysis)
* **용도:** 교육 및 실습

## 제공 파일

* `online_retail_ii_preprocessing.py` — Online Retail II 원본 데이터에서 실습에 필요한 거래를 선별하고 정제하기 위한 Python 전처리 코드
* `online_retail_ii_uk_2011_11_transactions.csv` — 원본 데이터에서 2011년 11월 영국 거래를 선택하고, 취소 거래와 분석에 적합하지 않은 기록을 제거한 전처리 데이터
* `online_retail_ii_uk_2011_11_onehot.xlsx` — 전처리된 데이터를 거래별 상품 형태로 변환하여 Orange에서 연관분석을 바로 수행할 수 있도록 구성한 데이터

## 실습 방법

실습은 다음과 같은 방법으로 진행할 수 있습니다.

1. **전처리 과정부터 직접 실습하기**
   UCI Machine Learning Repository에서 Online Retail II 원본 데이터를 내려받은 뒤, `online_retail_ii_preprocessing.py`의 코드를 Orange의 [Python Script] 위젯에서 실행합니다.

2. **전처리된 데이터부터 시작하기**
   `online_retail_ii_uk_2011_11_transactions.csv`를 이용하여 전처리 이후 단계부터 실습합니다.

3. **연관분석부터 바로 시작하기**
   `online_retail_ii_uk_2011_11_onehot.xlsx`를 [File] 위젯으로 불러와 [Frequent Itemsets]와 [Association Rules]를 이용한 연관분석을 바로 진행합니다.
