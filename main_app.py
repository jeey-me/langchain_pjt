# streamlit run main_app.py
import streamlit as st
from report_service import investment_report
from search_index import SearchResult, search_company
from stock_info import Stock

st.title("AI 투자 보고서 생성 서비스")
search_symbol = st.text_input("회사명", "Apple Inc")
# company_list = ["AAPL: Apple Inc",
#                 "APLE: Apple Hospitality REIT Inc"]
# company_selected = st.selectbox("회사 선택", company_list, index=0)

# 회사 이름, symbol
# symbol = "AAPL"
# compay = "Apple Inc"

company_info = search_company(search_symbol)
hits = company_info['hits']

company_list = [SearchResult(hit)for hit in hits]
company_selected = st.selectbox("회사명 선택", company_list, index=0)
print(company_selected.symbol)
print(company_selected.name)
search_symbol = company_selected.symbol
company_selected= company_selected.name
# search_symbol = st.text_input("회사명","MSFT")
# 서치 목록 만들기
# # hits = search_company(search_symbol)['hits']  
# search_results = [SearchResult(hit) for hit in hits]
# # Symbol, Name 추출
# company_selected = st.selectbox("회사 선택", search_results)

# #회사이름
# search_symbol = "MSFT"
# company_selected = "Microsoft"

# tab으로 구분해서 보기
tabs = ["주식 정보", "투자 보고서"]
tab1, tab2 = st.tabs(tabs)

# 주식 거래량 시각화
with tab1:
    st.header(f"{search_symbol}의 6개월 주식 거래량")
    stock = Stock(search_symbol)
    volume = stock.get_stock_volume()
    st.line_chart(volume, use_container_width=True)

with tab2:
    st.header(f"{search_symbol} 투자보고서 생성")
    
    if st.button("투자 보고서 생성"):
        with st.spinner(text="투자 보고서 생성 중..."):
            report = investment_report(search_symbol, company_selected)
            st.success("투자 보고서 생성 완료!")            
        st.write(report)