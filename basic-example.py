from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

prompt = ChatPromptTemplate.from_template("tell me a short joke about {topic}")
model = ChatOpenAI()
output_parser = StrOutputParser()

chain = prompt | model | output_parser

# print(chain.invoke({"topic": "ice cream"}))

input = {"topic": "ice cream"}
prompt_value = prompt.invoke(input)

# print(prompt_value)
# messages=[HumanMessage(content='tell me a short joke about ice cream')]

# print(prompt_value.to_messages())
# [HumanMessage(content='tell me a short joke about ice cream')]

# print(prompt_value.to_string())
# Human: tell me a short joke about ice cream

message = model.invoke(prompt_value)

print(message)
print(output_parser.invoke(message))

# you can see the output of any components of a chain by invoking a single component or some sub part of a chain:

prompt.invoke(input)
(prompt | model).invoke(input)