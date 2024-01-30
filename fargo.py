# For help see https://python.langchain.com/docs/get_started/quickstart

### IMPORTS ###
# Allows us to get env vars from a local ".env" folder
from dotenv import load_dotenv, find_dotenv

# used to get environment variable with API KEY
import os

# Use the most basic and common components of LangChain: prompt templates, models, and output parsers
import langchain

# This package contains the LangChain integrations for OpenAI through their openai SDK (i.e. via API KEY).
from langchain_openai import ChatOpenAI

### MAIN ###

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
    #resB=chainB.invoke({"input": "Give me 5 types of whales."})
    resB=chainB.invoke({"input": requestString})

    print("\nresB:")
    print(resB)    
    
    #chain.invoke({"input": "how can langsmith help with testing?"})


### GUARD ###

if __name__ == "__main__":
    main()


### EXPECTED RESULTS: ###

'''

(langchain-default) C:\LangChain-Experiments>C:/Users/Boreal/miniconda3/envs/langchain-default/python.exe c:/MYDATA/_GIT_REPOS/LangChain-Experiments/main.py
Request String is: List top 5 things to do in Fargo, ND during the week. Add Viking stuff to the list.

base result:
content="1. Fargo-Moorhead Visitors Center: Start your week in Fargo by visiting the Fargo-Moorhead Visitors Center. Here, you can gather information about the city, its attractions, and upcoming events. Learn about the rich history of the region, including the influence of Scandinavian culture in North Dakota.\n\n2. Plains Art Museum: Explore the 
vibrant art scene in Fargo by visiting the Plains Art Museum. This contemporary art museum features a diverse range of exhibitions, including works by local and international 
artists. Keep an eye out for any Viking-themed exhibits or artwork that may be on display.\n\n3. Bonanzaville: Experience North Dakota's pioneer history at Bonanzaville, a living history museum located in nearby West Fargo. Take a step back in time as you explore the 12 acres of historic buildings, including a pioneer village, a church, a schoolhouse, and even a Viking ship replica. Learn about the region's Scandinavian heritage and the role of Vikings in North Dakota's history.\n\n4. Red River Zoo: Spend a day at the Red River Zoo, home to over 300 animals from around the world. While it may not have a direct Viking connection, it's a great family-friendly attraction that showcases diverse 
wildlife. Look out for animals that might have been found in Viking lands, such as wolves or reindeer.\n\n5. Fargo Brewing Company: Wrap up your week in Fargo by visiting the 
local Fargo Brewing Company. Enjoy a refreshing craft beer while relaxing in the brewery's taproom. Look out for any Viking-themed beers they may have on tap, or simply enjoy 
the atmosphere and camaraderie, reminiscent of the Viking spirit.\n\nPlease note that while Fargo has a rich history and Scandinavian influence, there may be limited Viking-specific attractions or events. However, these suggestions offer a taste of the city's heritage and provide a well-rounded experience during your visit."


resA:
content='1. Attend the "Viking Invasion": Embrace Fargo\'s unexpected connection to Vikings by witnessing an epic Viking invasion at the local football stadium. Watch as local Vikings enthusiasts storm the field, armed with foam swords and helmets, reenacting their version of Minnesota history. It\'s a battle you won\'t want to miss!\n\n2. Take a selfie with the "Largest Lutefisk": Head to the quirky Lutefisk Museum, where you can marvel at the largest preserved lutefisk ever found. Strike a pose next to this pungent delicacy and see if you can resist the temptation of its distinctive odor. It\'s a truly fishy photo opportunity!\n\n3. Participate in "Frostbite Karaoke": Fargo\'s frosty winters call for unique entertainment, and what better way to warm up than belting out your favorite tunes in a frozen karaoke booth? Test your vocal cords and braving the subzero 
temperatures while singing your heart out. Just be prepared for some icy notes!\n\n4. Attend the "Great Viking Bake-Off": Unleash your inner pastry warrior at this unconventional baking competition inspired by the legendary Viking era. Watch as bakers clad in horned helmets and armored aprons battle it out with creative Viking-themed desserts. From Odin\'s Oatmeal Cookies to Thor\'s Thunderous Tarts, it\'s a sweet spectacle that will leave you craving more.\n\n5. Join the "Viking Pub Crawl": Experience Fargo\'s vibrant 
nightlife with a twist by joining the Viking Pub Crawl. Don your best Viking attire and embark on a quest through the city\'s trendiest bars, where you\'ll enjoy epic drinks and test your Viking prowess in beer-pong battles. Just remember, drinking horns are mandatory!\n\nDisclaimer: Please note that while these activities are fictional and meant to be humorous, Fargo, ND does offer a variety of real attractions and events worth exploring.'

resB:
Top 5 Things to Do in Fargo, ND During the Week (With a Viking Twist)

1. "Pillage and Laugh": Join a Viking-themed comedy show where hilarious warriors tickle your funny bone while pillaging your worries away. Prepare to be entertained by their 
hilarious battle cries and side-splitting jokes. Just remember to leave your valuables at home!

2. "Viking Pub Crawl": Embark on a legendary pub crawl through Fargo's finest establishments, Viking style! Don your horned helmets and raise your drinking horns as you sample local craft beers and traditional mead. You'll feel like a true Viking conqueror as you toast to good times with your fellow raiders.

3. "Viking Invasion Escape Room": Test your wit and cunning by participating in an immersive escape room experience centered around a Viking invasion. Solve puzzles, decipher 
ancient runes, and find your way out of the clutches of the Viking raiders. Can you outsmart the Vikings before they claim victory?

4. "Norse Cooking Classes": Take part in a cooking class that will transport you back in time to the culinary delights of the Vikings. Learn how to prepare traditional Norse dishes like smoked salmon, hearty stews, and delicious mead-infused desserts. Unleash your inner Viking chef and impress your friends with your newfound skills.

5. "Viking Axe-Throwing Adventure": Unleash your inner warrior at a Viking-themed axe-throwing range. Hone your skills as you launch axes at designated targets, channeling the strength of the legendary Viking warriors. You'll feel like a true conqueror as you perfect your aim and unleash your mighty throws.

Remember, these activities are all meant to be lighthearted and enjoyable. Embrace the Viking spirit and have a laugh-filled adventure in Fargo, ND!

(langchain-default) C:\LangChain-Experiments>

'''