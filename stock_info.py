import yfinance as yf
import pandas as pd

class Stock:
    # 생성자 : 기본값 설정
    def __init__(self, symbol):
        self.symbol = symbol
        self.ticker = yf.Ticker(symbol)

    # 회사 기본 정보
    def get_basic_info(self):
        basic_info = pd.DataFrame.from_dict(
            self.ticker.info, 
            orient='index', 
            columns=['values']
        )
        basic_info = basic_info.loc[['longName', 'marketCap', 'industry', 'sector', 'fullTimeEmployees', 'currentPrice', 'enterpriseValue']]
        return basic_info

    # 재무제표  수집
    def get_financial_statement(self):

        # 손익 계산서
        income_state = self.ticker.income_stmt.loc[['Total Revenue', 'Gross Profit',
                         'Operating Income', 'Net Income']].iloc[:, :4].to_markdown()
        # print(income_state)      
        # 대차대조표
        balance_sheet = self.ticker.balance_sheet.loc[['Total Assets', 
                        'Total Liabilities Net Minority Interest',
                        'Stockholders Equity']].iloc[:, :4].to_markdown()
        # 현금 흐름표
        cash_flow = self.ticker.cashflow.loc[['Operating Cash Flow', 
                                    'Investing Cash Flow',
                                    'Financing Cash Flow']].iloc[:, :4].to_markdown()
    
        financial_stats = f"""
        ### 손익계산서
        {income_state}
        ### 대차대조표
        {balance_sheet}
        ### 현금 흐름표
        {cash_flow}
        """
        print (financial_stats)
        return (financial_stats)
    
    def get_stock_volume(self):
        volume_data = self.ticker.history(period="6mo", interval="1d")
        volume_data_desc = volume_data.sort_index(ascending=False)
        return volume_data_desc

    # 주식 거래량

# python stock_info.py 실행할 때만 아래코드 실행됨
if __name__ == "__main__":
    # 회사 이름
    compay_name = "AAPL"
    # Stock 객체생성
    stock = Stock(compay_name)
    # print("회사 심볼", stock.symbol)
    # print("회사 티커객체", stock.ticker)
    # print(stock.get_basic_info())
    # print(stock.get_financial_statement())
    print(stock.get_stock_volume())