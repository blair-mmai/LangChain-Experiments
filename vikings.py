# https://python.langchain.com/docs/get_started/quickstart

# Allows us to get env vars from a local ".env" folder
from dotenv import load_dotenv, find_dotenv

# used to get environment variable with API KEY
import os

# Use the most basic and common components of LangChain: prompt templates, models, and output parsers
import langchain


# This package contains the LangChain integrations for OpenAI through their openai SDK (i.e. via API KEY).
from langchain_openai import ChatOpenAI

def main(): 

    # pass
    load_dotenv(find_dotenv())


    # Get OpenAI API Key from user environment variable so that it's not showing in the code.
    # https://python.langchain.com/docs/integrations/llms/openai
    #OpenAI_Key = os.environ.get("OPENAI_API_KEY")
    OpenAI_Key = os.getenv("LOCAL_OPENAI_API_KEY")

    #print(os.environ.get("OPENAI_API_KEY"))
    #print(f"Key is: {OpenAI_Key}")
    
    # initialize model (if no param passed, it'll pull it directly from default env variable):
    # llm = ChatOpenAI()

    # initialize model with api key:
    # llm = ChatOpenAI(openapi_api_key=OpenAI_Key) # OPENAI_API_KEY)
    #llm = ChatOpenAI(openapi_api_key=OPENAI_API_KEY)
    #llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OPENAI_API_KEY)
    llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=OpenAI_Key)

    #requestString = "Give me 5 types of whales."
    requestString = "List top 5 things to do in Fargo, ND during the week. Add Viking stuff to the list."
    print(f"Request String is: {requestString}")

    #result=llm.invoke("Give me 5 types of whales.")    
    result=llm.invoke(requestString)    
    #result=llm.predict("Give me 5 types of whales.")  #predict() is being deprecated.
    print("\nbase result:")
    print(result)

    # import ChatPromptTemplate
    from langchain_core.prompts import ChatPromptTemplate
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are world class comedy writer."),
        ("user", "{input}")
    ])

    print("")
    
    chain = prompt | llm
    #resA=chain.invoke({"input": "Give me 5 types of whales."})
    resA=chain.invoke({"input": requestString})
    print("\nresA:")
    print(resA)
    
    from langchain_core.output_parsers import StrOutputParser
    output_parser = StrOutputParser()

    chainB = prompt | llm | output_parser
    resB=chainB.invoke({"input": requestString})

    print("\nresB:")
    print(resB)    
    
    #chain.invoke({"input": "how can langsmith help with testing?"})


if __name__ == "__main__":
    main()

