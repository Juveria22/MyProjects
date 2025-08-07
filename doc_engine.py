import os

from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
#from llama_index.llms.openai import OpenAI as LlamaOpenAI
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

#initializes open ai gpt model with the help of the llama index
llama_llm = Ollama(model = "llama3")

embed_model = OllamaEmbedding(model_name="nomic-embed-text")

documents = SimpleDirectoryReader("data").load_data() 

#converts loaded document into vector index using the open ai embeddings. Stores the embeddings into an index that allows semantic search and retrieval. 
index = VectorStoreIndex.from_documents(documents, embed_model=embed_model) 

#transforms vector index into a query engine (try to query the documents) 
query_engine = index.as_query_engine(llm = llama_llm)

#the output from the query engine is sent. It takes the users query and returns the ai generated response from ur documents 
def query_documents(user_query: str) -> str:
    return str(query_engine.query(user_query)) 