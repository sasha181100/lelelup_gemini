from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

import os
import google.generativeai as genai
from langchain.retrievers import BM25Retriever, EnsembleRetriever
from Loader.loader import *
GOOGLE_API_KEY = 'AIzaSyC02h1AJhpEL5whQQBYzdbHdgNStdZU2ko'
EMBEDDING_MODEL_NAME = "models/embedding-001"
DB_PATH = "../db"
def retrieve(query, chat_history):
    print(GOOGLE_API_KEY)
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL_NAME, google_api_key=GOOGLE_API_KEY)

    preprocessing_prompt = f'''
    '''

    prompt_retriever = f'''
    Ты - ИИ-помощник для выделения сути из текста. У тебя есть документы содержащие информацию о компании. Мне нужно извлечь из этой нужные фрагменты информации помогающие ответить на
     вопрос. Сформулируй запрос к векторной базе данных в которой хранится этот документ исходя из ВОПРОСА ПОЛЬЗОВАТЕЛЯ и ИСТОРИИ ПЕРЕПИСКИ пользователя и Менеджера
     ВОПРОС ПОЛЬЗОВАТЕЛЯ: {query}.  
     ИСТОРИЯ ПЕРЕПИСКИ: {chat_history}
     В ответе напиши одно предложение только текст по которому будет 
     осуществляться семантический поиск и векторной базе данных. Цель - найти максимально похожие к запросу 
    пользователя документы. В ответе напиши ровно 1 предложение в формате: Текст для поиска: "ТВОЙ ОТВЕТ". 
    Важно чтобы твой ответ был в кавычках.'''
    model = genai.GenerativeModel(model_name='gemini-1.0-pro')

    response = model.generate_content(prompt_retriever)
    print(response.text.split(sep='"'))
    final_query = response.text.split(sep='"')
    # text_splitter = RecursiveCharacterTextSplitter()
    # docs = text_splitter.split_documents(documents)
    # bm25_retriever = BM25Retriever.from_texts(docs)
    # bm25_retriever.k = 2
    print(DB_PATH)
    retriever = Chroma(persist_directory=DB_PATH, embedding_function=embeddings).as_retriever(
        search_type = "mmr",
        search_kwargs ={
            'k': 7,
        }
    )

    docs = retriever.get_relevant_documents(final_query)

    return docs

    # """
    # Creates embeddings for texts and builds a vector index for retrieval.
    # Args:
    # texts (list): List of texts to create embeddings for.
    # model_name (str): Name of the embedding model.
    # api_key (str): API key for accessing Google Generative AI.
    # Returns:
    # retriever: Vector index for text retrieval.
    # """
    # query_vector = embeddings.model.encode("Представь что ты ассистент в компании, занимающейся продажами конструкторов. Ответь на вопрос клиента используя только информацию из прикрепленных данных, не выдумывай. Итак вопрос клиента: \"сколько кг выдерживает металлический конструктор?\ Отвечай на русском языке")
    # type(Chroma.from_documents(texts, embeddings)
    # results = vector_index.search(query_vector, k=0)
    # print(results)

def create_db(docs):
    """
    Creates embeddings for texts and builds a vector index for retrieval.
    Args:
    texts (list): List of texts to create embeddings for.
    model_name (str): Name of the embedding model.
    api_key (str): API key for accessing Google Generative AI.
    Returns:
    retriever: Vector index for text retrieval.
    """
    embeddings = GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL_NAME, google_api_key=GOOGLE_API_KEY)

    db = Chroma.from_documents(docs, embeddings, persist_directory="./db")

    print(len(docs))
    # results = vector_index.search(query_vector, k=0)
    # print(results)
    return db