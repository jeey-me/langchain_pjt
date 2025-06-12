# 필요 라이브러리 import 
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from stock_info import Stock


# 필요한 변수 정의 

load_dotenv(override=True)

api_key = os.getenv('OPENAI_API_KEY')
# print(api_key)

# gpt model 객체 생성
# llm = ChatOpenAI(model="gpt-4o", api_key=api_key)
llm = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key , temperature=0)
llm

# 함수 정의 

def investment_report(company, symbol) :
    system_prompt = """
    Want assistance provided by qualified individuals enabled with experience on understanding charts using technical analysis tools while interpreting macroeconomic environment prevailing across world consequently assisting customers acquire long term advantages requires clear verdicts therefore seeking same through informed predictions written down precisely! First statement contains following content- “Can you tell us what future stock market looks like based upon current conditions ?".
    """
    user_prompt = """
    {company}에 주식을 투자해도 될까요? 마크다운 형식의 투자보고서를 한글로 작성해 주세요.
    야래의 기본 정보, 재무제표를 참고해 마크다운 형식의 투자 보고서를 한글로 작성해 주세요.

    기본정보:
    {basic_info}

    재무제표:
    {finacial_statement}
    """
    # 프롬프트 객체 생성 
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ])

    #output parser 객체 생성
    output_parser = StrOutputParser()
    

    # LCEL(LangChain Expression Language)객체 생성
    chain = prompt | llm | output_parser

    # 야후 파이낸스 api를 통한 필요한 정보 수집을 위한 stock객체 생성
    # company = "MicroSoft"
    # symbol = "MSFT"
    stock = Stock(symbol)

    # chain.invoke(프롬프트에 넘기는 변수값_dict형태)

    req_value = {
        "company":company,
        # 기본정보 :  basic_info
        "basic_info": stock.get_basic_info(),
        # 재무제표: finacial_statement
        "finacial_statement" : stock.get_financial_statement()
        }
    
    response = chain.invoke(req_value)

    
    # 리턴 값 정의 
    return response


# 모듈 테스트 
if __name__=="__main__" :

    company = "MicroSoft"
    symbol = "MSFT" 
    print(company)
    print(investment_report(company, symbol))