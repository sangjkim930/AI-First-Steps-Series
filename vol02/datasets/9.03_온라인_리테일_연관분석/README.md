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

- `online_retail_ii_preprocessing.py` — Online Retail II 원본 데이터를 정제하고, 2011년 11월 영국 거래를 선별하여 연관분석에 사용할 수 있는 형태로 변환하는 Python 코드
- `online_retail_ii_uk_2011_11.xlsx` — 위 Python 전처리 과정을 미리 적용하여, Orange에서 이후 연관분석 실습을 바로 진행할 수 있도록 구성한 데이터

## 원본 데이터

실습의 원본 데이터는 UCI Machine Learning Repository의 **Online Retail II** 데이터셋입니다.

- **원본 파일:** `online_retail_II.xlsx`
- **UCI 주소:** https://doi.org/10.24432/C5CG6D
- **라이선스:** CC BY 4.0

원본 파일은 용량이 크기 때문에 이 GitHub 저장소에서는 직접 제공하지 않습니다. UCI에서 원본 파일을 내려받아 Orange의 [File] 위젯으로 불러온 뒤, `online_retail_ii_preprocessing.py`의 코드를 [Python Script] 위젯에서 실행하여 전처리 과정을 직접 실습할 수 있습니다.

Python 전처리 과정을 생략하려면 이 폴더에서 제공하는 `online_retail_ii_uk_2011_11.xlsx` 파일을 사용하면 됩니다.
