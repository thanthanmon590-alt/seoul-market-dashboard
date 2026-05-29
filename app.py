import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Korean font setting for Mac
plt.rcParams["font.family"] = "NanumGothic"
plt.rcParams["axes.unicode_minus"] = False

# ==============================
# 1. 페이지 설정
# ==============================
st.set_page_config(
    page_title="서울시 골목상권 매출과 생활인구 분석",
    layout="wide"
)

st.title("서울시 골목상권 매출과 생활인구 분석")
st.write("2024년과 2025년 데이터를 비교하여 골목상권의 매출과 생활인구 관계를 분석합니다.")

# ==============================
# 2. 데이터 불러오기
# ==============================
year_sales = pd.read_csv("year_sales.csv")
district_sales = pd.read_csv("district_sales.csv")
industry_top10 = pd.read_csv("industry_top10.csv")
market_top10 = pd.read_csv("market_top10.csv")
population_sales = pd.read_csv("population_sales.csv")

# ==============================
# 3. 연도별 총매출 비교
# ==============================
st.header("1. 2024년과 2025년 총매출 비교")
st.write("연도별 총매출을 비교하여 전체 매출 변화가 있는지 확인합니다.")

st.bar_chart(
    year_sales.set_index("연도")["당월_매출_금액"]
)

# ==============================
# 4. 자치구별 매출 비교
# ==============================
st.header("2. 자치구별 매출 비교")
st.write("각 연도별로 자치구별 총매출을 비교합니다.")

selected_year_district = st.selectbox(
    "자치구별 매출을 확인할 연도를 선택하세요",
    sorted(district_sales["연도"].astype(str).unique())
)

district_filtered = district_sales[
    district_sales["연도"].astype(str) == selected_year_district
]

district_filtered = district_filtered.reset_index(drop=True)

st.bar_chart(
    district_filtered.set_index("자치구_코드_명")["당월_매출_금액"]
)

st.dataframe(district_filtered)

# ==============================
# 5. 업종별 매출 Top 10
# ==============================
st.header("3. 업종별 매출 Top 10 비교")
st.write("각 연도별로 매출이 높은 업종 Top 10을 비교합니다.")

selected_year_industry = st.selectbox(
    "업종별 매출을 확인할 연도를 선택하세요",
    sorted(industry_top10["연도"].astype(str).unique())
)

industry_filtered = industry_top10[
    industry_top10["연도"].astype(str) == selected_year_industry
]

industry_filtered = industry_filtered.reset_index(drop=True)

st.bar_chart(
    industry_filtered.set_index("서비스_업종_코드_명")["당월_매출_금액"]
)

st.dataframe(industry_filtered)

# ==============================
# 6. 상권별 매출 Top 10
# ==============================
st.header("4. 상권별 매출 Top 10 비교")
st.write("각 연도별로 매출이 높은 상권 Top 10을 비교합니다.")

selected_year_market = st.selectbox(
    "상권별 매출을 확인할 연도를 선택하세요",
    sorted(market_top10["연도"].astype(str).unique())
)

market_filtered = market_top10[
    market_top10["연도"].astype(str) == selected_year_market
]

market_filtered = market_filtered.reset_index(drop=True)

st.bar_chart(
    market_filtered.set_index("상권_코드_명_매출")["당월_매출_금액"]
)

st.dataframe(market_filtered)

# ==============================
# 7. 생활인구와 매출 관계
# ==============================
st.header("5. 생활인구와 매출의 관계")
st.write("상권별 평균 유동인구와 총매출의 관계를 산점도로 확인합니다.")

selected_year_pop = st.selectbox(
    "생활인구와 매출 관계를 확인할 연도를 선택하세요",
    sorted(population_sales["연도"].astype(str).unique())
)

pop_filtered = population_sales[
    population_sales["연도"].astype(str) == selected_year_pop
]

pop_filtered = pop_filtered.reset_index(drop=True)

fig, ax = plt.subplots()
ax.scatter(pop_filtered["평균유동인구"], pop_filtered["총매출"])
ax.set_xlabel("평균 유동인구")
ax.set_ylabel("총매출")
ax.set_title(f"{selected_year_pop}년 생활인구와 매출 관계")

st.pyplot(fig)

st.dataframe(pop_filtered)

# ==============================
# 8. 분석 요약
# ==============================
st.header("분석 요약")
st.write("""
이 대시보드는 서울시 골목상권의 매출과 생활인구 관계를 확인하기 위한 것입니다.
2024년과 2025년 총매출을 비교하고, 자치구별·업종별·상권별 매출 차이를 살펴봅니다.
또한 생활인구가 많은 상권일수록 매출도 높게 나타나는지 산점도를 통해 확인합니다.
""")