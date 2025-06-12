import meilisearch
import pandas as pd

client = meilisearch.Client('http://localhost:7700', 'aSampleMasterKey')

def search_company(symbol):
    # nasdaq : index 이름 
    return client.index('nasdaq').search(symbol)

# 자료 서칭을 위한 클래스
class SearchResult:
    # pass
    def __init__(self, item):
        self.item = item

    # 심볼값 가져오기 
    # @property = 파이썬 데코레이터, 클래스의 메서드를 마치 속성처럼 사용할 수 있음
    @property    
    def symbol(self):
        return self.item['Symbol']
    
    # 회사명 가져오기
    @property
    def name(self):
        return self.item['Name']
    
    # print() 또는 str()문을 만났을 때 출력형태
    def __str__(self):
        # return f"AAPL: Apple Inc"
        return f"{self.symbol}: {self.name}"
    

if __name__ == "__main__":

    # 서치 키워드 
    # symbol = "AAPL"
    symbol = "Apple"
    company_info = search_company(symbol)
    # print(company_info)
    hits = company_info['hits']
    # print(hits)
    # result = []
    # for hit in hits :
    #     print(SearchResult(hit))
    #     print("-"*20)
    #     result.append(SearchResult(hit))
    # 리스트 컴프리핸션으로 변경
    result = [SearchResult(hit) for hit in hits]
    # 최종결과
    print(result[0].name)
    print(result[0].symbol)




    # print(company_info['hits'])
    # company_symbol = company_info['hits'][0]['Symbol']
    # company_name = company_info['hits'][0]['Name']
    # company_Sector = company_info['hits'][0]['Sector']
    # company_Industry = company_info['hits'][0]['Industry']
    # company_MarketCap = company_info['hits'][0]['Market Cap']
    # print(f"Sector:{company_Sector},Industry:{company_Industry},MarketCap:{company_MarketCap}")
    # print (f"{company_symbol}:{company_name}")
 

   