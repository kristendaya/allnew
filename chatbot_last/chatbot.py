from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

import os
from langchain.document_loaders import UnstructuredFileLoader, DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
import weaviate
from langchain.vectorstores.weaviate import Weaviate
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType, Tool
from langchain.memory import ConversationBufferMemory
from langchain.experimental.plan_and_execute import PlanAndExecute, load_agent_executor, load_chat_planner

os.environ["OPENAI_API_KEY"] =""

doc_loader = DirectoryLoader(
    'data/', # the relative directory address, remember we set root directory above
    glob='**/*.pdf',     # Let's load only pdf files in every subdirectory
    show_progress=True
)
docs = doc_loader.load()

splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=300
)
splitted_docs_list = splitter.split_documents(docs)


os.environ["WEAVIATE_API_KEY"] =""

auth_config = weaviate.auth.AuthApiKey(api_key=os.environ.get('WEAVIATE_API_KEY'))
client = weaviate.Client(
    url="",
    auth_client_secret=auth_config,
    additional_headers={
        "X-OpenAI-Api-Key": os.environ.get('OPENAI_API_KEY')
    }
)

class_obj = {
    "class": "LangChain",
    "vectorizer": "text2vec-openai",
}

try:
  # Add the class to the schema
  client.schema.create_class(class_obj)
except:
  print("Class already exists")

embeddings = OpenAIEmbeddings()
# I use 'LangChain' for index_name and 'text' for text_key
vectorstore = Weaviate(client, "LangChain", "text", embedding=embeddings)
documents = splitted_docs_list

texts = [d.page_content for d in documents]
metadatas = [d.metadata for d in documents]

vectorstore.add_texts(texts, metadatas=metadatas, embedding=embeddings)

vectorstore = Weaviate.from_texts(
    texts,
    embeddings,
    metadatas=metadatas,
    client=client,
)

query = "What was Core PCE inflation in December 2022?"
vectorstore.similarity_search(query)

# Google Custom Search Engine Keys
os.environ['GOOGLE_CSE_ID'] = "google-search"
os.environ['GOOGLE_API_KEY'] = "AIzaSyBTmsW80Q5Gsbk_sKeELiedzNWhAdSgVa4"

llm = ChatOpenAI()
retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore.as_retriever(),
)

query = "How was core pce inflation's trend in 2022?"
retrieval_qa.run(query)

# llm = ChatOpenAI() # which was defined before
# we load wikipedia
tools = load_tools(['wikipedia'], llm=llm)

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.run('which Gordon Ramsay restaurant is the best? ')

llm = ChatOpenAI()
tools = load_tools([
    'wikipedia',
    'google-search',
    'llm-math'
], llm=llm)

tools.append(Tool.from_function(
        func= retrieval_qa.run,
        name = "FOMC DB",
        description="Useful for federal reserve documents for interest rates and inflation."
        # coroutine= ... <- you can specify an async method if desired as well
    ))

memory = ConversationBufferMemory(memory_key='chat_history')
planner = load_chat_planner(llm)
executor = load_agent_executor(llm, tools, verbose=True)

agent = PlanAndExecute(
    planner=planner,
    executor=executor,
    verbose=True,
    reduce_k_below_max_tokens=True
)

agent.run("Compare what the fed said about inflation in USA, in March 2023 and December 2022?")
