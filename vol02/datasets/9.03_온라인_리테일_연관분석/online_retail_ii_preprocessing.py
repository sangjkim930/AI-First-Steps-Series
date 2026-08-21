import Orange.data.pandas_compat as p
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix

# Orange 데이터를 pandas 데이터프레임으로 변환
df = pd.concat(in_data.to_pandas_dfs(), axis=1)

# Country가 숫자 코드로 입력된 경우 국가명으로 변환
if pd.api.types.is_numeric_dtype(df["Country"]):
    country_var = in_data.domain["Country"]
    df["Country"] = df["Country"].map(
        dict(enumerate(country_var.values))
    )

# InvoiceDate 형식에 따라 연도와 월 추출
if pd.api.types.is_numeric_dtype(df["InvoiceDate"]):
    invoice_date = pd.to_datetime(df["InvoiceDate"], unit="s")
else:
    invoice_date = pd.to_datetime(df["InvoiceDate"], errors="coerce")

df["Year"] = invoice_date.dt.year.astype("Int64").astype(str)
df["Month"] = (
    invoice_date.dt.month.astype("Int64").astype(str).str.zfill(2)
)

# 2011년 영국의 정상 거래만 선택
df = df[
    (df["Country"] == "United Kingdom")
    & (df["Year"] == "2011")
    & (df["Quantity"] > 0)
    & (~df["Invoice"].astype(str).str.startswith("C"))
    & (df["Description"].notna())
    & (df["Description"].astype(str).str.strip() != "")
].copy()

# 11월 거래만 선택
df = df[df["Month"] == "11"].copy()

# 거래번호와 상품명 정리
df["TransactionID"] = df["Invoice"].astype(str)
df["Item"] = (
    df["Description"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.strip()
)

df = df[["TransactionID", "Item"]]

# 거래별 상품 포함 여부를 희소행렬로 변환
transaction_codes, transaction_ids = pd.factorize(
    df["TransactionID"]
)
item_codes, item_names = pd.factorize(df["Item"])

matrix = csr_matrix(
    (
        np.ones(len(df), dtype=np.int8),
        (transaction_codes, item_codes),
    ),
    shape=(len(transaction_ids), len(item_names)),
)

# 한 거래에 같은 상품이 여러 번 기록된 경우 합산값을 1로 통일(구매 여부만 표시)
matrix.data[:] = 1

transaction = pd.DataFrame(
    matrix.toarray(),
    columns=item_names.astype(str),
)

transaction.insert(0, "TransactionID", transaction_ids)

# 구매 여부를 1과 결측값으로 표시
item_columns = transaction.columns[1:]

transaction[item_columns] = (
    transaction[item_columns]
    .astype("Int8")
    .mask(transaction[item_columns] == 0)
    .astype("category")
)

# 변환된 데이터를 Orange로 전달
out_data = p.table_from_frame(transaction)
