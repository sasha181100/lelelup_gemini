# from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import RecursiveUrlLoader
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from Retriever.retriever import *
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import GoogleDriveLoader
from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Chroma
import os

GOOGLE_API_KEY = 'AIzaSyC02h1AJhpEL5whQQBYzdbHdgNStdZU2ko'
EMBEDDING_MODEL_NAME = "models/embedding-001"

# def load_pdf(pdf_path):
#     """
#     Loads a PDF document and splits it into pages.
#     Args:
#     pdf_path (str): Path to the PDF file.
#     Returns:
#     loader
#     """
#     pdf_loader = PyPDFLoader(pdf_path)
#     return pdf_loader


def load_txt(file_path):
    txt_loader = TextLoader(file_path)
    return txt_loader


def load_url(url):
    url_loader = RecursiveUrlLoader(url)
    return url_loader

def get_documents(type, file_name):

    if type == "pdf":
        loader = PyPDFLoader(file_name)
    elif type == "txt":
        loader = TextLoader(file_name, encoding="UTF-8")
    elif type == "url":
        loader = WebBaseLoader(file_name)
    return loader.load()
    # text_loader_kwargs = {'autodetect_encoding': True}
    # loader = DirectoryLoader('/', glob="**/*.pdf", loader_cls=PyPDFLoader, loader_kwargs=text_loader_kwargs)
    # docs = loader.load()
    #
    # text_splitter = SemanticChunker(GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL_NAME, google_api_key=GOOGLE_API_KEY))
def split_and_save(type, file_name):
    documents = get_documents(type, file_name)
    # text_splitter = RecursiveCharacterTextSplitter(separators=["#", "\n\n",],)
    text_splitter = CharacterTextSplitter(separator="\n\n", chunk_size=1024, chunk_overlap=256, is_separator_regex=False)
    docs = text_splitter.split_documents(documents)
    print(len(docs))
    create_db(docs)






