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
os.environ['GOOGLE_CSE_ID'] = ""
os.environ['GOOGLE_API_KEY'] = ""

doc_loader = DirectoryLoader(
    'data/',
    glob='./*.pdf',
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
    url="https://langchain",
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
  client.schema.create_class(class_obj)
except:
  print("Class already exists")

embeddings = OpenAIEmbeddings()
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

llm = ChatOpenAI()
retrieval_qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type='stuff',
    retriever=vectorstore.as_retriever(),
)

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

while True:
    user_input = input("질문 입력 (종료하려면 'exit' 입력): ")
    if user_input.lower() == 'exit':
        break
    else:
        response = agent.run(user_input)
        print(response)
