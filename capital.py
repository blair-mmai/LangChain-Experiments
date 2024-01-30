# gets capital city of country and then an API call to get weather information in capital.

import os

# Allows us to get env vars from a local ".env" folder
from dotenv import load_dotenv, find_dotenv

# Use the most basic and common components of LangChain: prompt templates, models, and output parsers
import langchain_community

# This package contains the LangChain integrations for OpenAI through their openai SDK (i.e. via API KEY).
# from langchain_openai import ChatOpenAI #being deprecated
# from langchain_community.chat_models import ChatOpenAI #being deprecated
from langchain_openai.chat_models import ChatOpenAI #being deprecated
from langchain.prompts.chat import HumanMessagePromptTemplate, ChatPromptTemplate

# pydantic example:  https://youtu.be/I4mFqyqFkxg?si=H00I1mQwFC7O_eDs&t=467
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


from langchain_core._api.deprecation import suppress_langchain_deprecation_warning

class Country(BaseModel):
        capital: str = Field(description="capital of the country")
        name: str = Field(description="name of the country")

OPENAI_MODEL = "gpt-4"
OPENAI_API_KEY = os.getenv("LOCAL_OPENAI_API_KEY")

PROMPT_COUNTRY_INFO = """
    Provide information about {country}.  If the country doesnt exist make something up.
    {format_instructions}

"""

def main(): 

    print("In main.")

    load_dotenv(find_dotenv())

    llm = ChatOpenAI(model=OPENAI_MODEL, api_key=OPENAI_API_KEY)
    parser = PydanticOutputParser(pydantic_object=Country)

    # get user input
    country = input("Enter the name of a country: ")

    message = HumanMessagePromptTemplate.from_template(template=PROMPT_COUNTRY_INFO)
    chat_prompt = ChatPromptTemplate.from_messages(messages=[message])
    chat_prompt_with_values = chat_prompt.format_prompt(
         country=country, format_instructions=parser.get_format_instructions()
    )

    with suppress_langchain_deprecation_warning():
        response = llm(chat_prompt_with_values.to_messages())
    
    data = parser.parse(response.content)
    print(f"The capital of {data.name} is {data.capital}.")

if __name__ == "__main__":
    main()

