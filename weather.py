# calls weather API

import os

from dotenv import load_dotenv, find_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.chains.api  import open_meteo_docs
from langchain.chains      import APIChain

load_dotenv(find_dotenv())

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_API_KEY = os.getenv("LOCAL_OPENAI_API_KEY")

def main(): 

    llm = ChatOpenAI(model=OPENAI_MODEL, api_key=OPENAI_API_KEY)

    requestString="What is the weather in Toronto in Celsius"
    llm.invoke(requestString)

    chain_new = APIChain.from_llm_and_api_docs(
        llm, open_meteo_docs.OPEN_METEO_DOCS, verbose=False        
    )

    result = chain_new.run("Also provide the precipitation expected tonight.")

    print(f"The weather in Toronto: {result}")
 
    
if __name__ == "__main__":
    main()

