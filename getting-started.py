from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain.prompts.chat import ChatPromptTemplate

llm = OpenAI()
chat_model = ChatOpenAI()

template = "You are a helpful assistant that translates {input_language} to {output_language}."
human_template = "{text}"

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", template),
    ("human", human_template),
])

chat_prompt.format_messages(input_language="English", output_language="French", text="I love programming.")

# text = "What would be a good company name for a company that makes colorful socks?"
# messages = [HumanMessage(content=text)]

# print(llm.invoke(text))
# print(chat_model.invoke(messages))