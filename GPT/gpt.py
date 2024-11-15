from IPython.display import Markdown
import textwrap
from Retriever.retriever import *

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


GOOGLE_API_KEY = 'AIzaSyC02h1AJhpEL5whQQBYzdbHdgNStdZU2ko'
EMBEDDING_MODEL_NAME = "models/embedding-001"
DB_PATH = "./chroma_db"
TEMPERATURE = 0.1

def generate_answer(user_prompt, chat_history):
    # llm = ChatGoogleGenerativeAI(model=EMBEDDING_MODEL_NAME, google_api_key=GOOGLE_API_KEY, temperature=TEMPERATURE,convert_system_message_to_human=True)
    docs = retrieve(user_prompt, chat_history)
    model = genai.GenerativeModel(model_name='gemini-1.0-pro')

    docs_str = ""
    for doc in docs:
        docs_str += doc.page_content
    prompt_SS_hard = f'''Ты - менеджер по продажам в компании \"Свобода слова\". 
                    Твоя задача отвечать на вопросы клиента в интересах помании на основании информации указанной в поле КОНТЕКСТ.
                    Если информации в поле КОНТЕКСТ недостаточно честно скажи об этом, не выдумывай ответ.
                    Общайся с клинтом вежливо на русском языке. Вопрос клиента находится в поле ВОПРОС.
                    КОНТЕКСТ: {docs_str}
                    
                    ВОПРОС: {user_prompt}
                    '''
    prompt_SS_light = f'''Ты - менеджер по продажам в компании \"Свобода слова\ Информация о ней есть на сайте https://www.lingvo-svoboda.ru/". 
                    Твоя задача отвечать на вопросы клиента в интересах помании на основании информации указанной в поле КОНТЕКСТ и информации с сайта.
                    Общайся с клинтом вежливо на русском языке. Вопрос клиента находится в поле ВОПРОС.
                    КОНТЕКСТ: {docs_str}
                    
                    ВОПРОС: {user_prompt}
                    '''
    prompt_BIGO_light = f'''
                    Ты - менеджер по продажам в компании \"BIGO-LAND"\ занимающейся продажей конструкторов для детей и взрослых. Информация о ней есть на сайте https://bigo.land/. 
                    Твоя задача отвечать на вопросы клиента в интересах помании на основании информации указанной в поле
                    КОНТЕКСТ и информации с сайта. Общайся коротко и не перегружай клиента информацией. Не забывай задавать вопросы если информации недостаточно.
                    Твоя задача самостоятельно искходя из ИСТОРИИ ЧАТА понять, на каком этапе продажи находится клиент и выбирать соответствующее поведение.
                    Общайся с клиентом вежливо на русском языке. Если у тебя недостаточно информации то честно скажи об этом и не придумывай. Вопрос клиента находится в поле ВОПРОС.
                    История предшествующей переписки с клиентом находится в поле ИСТОРИЯ ЧАТА:
                    
                    КОНТЕКСТ: {docs_str}
                    
                    ИСТОРИЯ ЧАТА: {chat_history}
                    
                    ВОПРОС: {user_prompt}
                    
                    '''

    choosen_prompt = prompt_BIGO_light
    with open("../output.txt", "w", encoding="utf-8") as f:
        print(choosen_prompt, file=f)
    try:
        response = model.generate_content(choosen_prompt)
    except Exception as e:
        print(e)
    to_markdown(response.text)
    res = ""
    for chunk in response:
        res += chunk.text
    return res