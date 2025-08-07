import os

from dotenv import load_dotenv
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
#from langchain_openai import OpenAI
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3", temperature=0.7)



#load .env 
load_dotenv()
#OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") 

#if not OPENAI_API_KEY:
#    raise ValueError('OPENAI_API_KEY not found. Please check your .env file.')

#Initializing the LLM 
#temperature is about randomness, higher temp means more creative 
#llm = OpenAI(openai_api_key = OPENAI_API_KEY, temperature=0.7)


#Store per user memory sessions 

session_memory_map = {}

#Function to get response. sesssion id is individual to each user. created each time a new user starts a conversation. 
# user query tracks text  
# session memory checks for conversation history for the session id. If theres no history we create a new conversation memory map for the id 
# initializing a conversation chain by taking the session id and initializing it
# the .predict method generates an ai response based on the previous context and the current query (itll always try to look for previous history)
#then itll return the response in string 

def get_response(session_id: str, user_query: str) -> str:
    if session_id not in session_memory_map:
        memory = ConversationBufferMemory()
        session_memory_map[session_id] = ConversationChain(llm=llm, memory=memory, verbose= True) 

    conversation = session_memory_map[session_id]
    return conversation.predict(input=user_query) 