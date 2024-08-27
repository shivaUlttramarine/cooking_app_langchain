from flask import Flask, render_template, request
######### langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,ChatPromptTemplate,SystemMessagePromptTemplate,AIMessagePromptTemplate,HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage

import os

app = Flask(__name__)

# Initialize the LangChain LLM (make sure to replace with your actual OpenAI API key)
with open('openaikey.txt', 'r') as file:
    api_key = file.read().strip()
f = open('openaikey.txt', 'r')
os.environ["OPENAI_API_KEY"]=f.read()


# def func_ai():
#     system_template = "You are an AI recept assitant that is specialized in {diatery} dishes in {region} kitchen that are cooked in {time} minutes."
#     system_prompt   = SystemMessagePromptTemplate.from_template(system_template)
#     human_prompt    = HumanMessagePromptTemplate.from_template("{reciept_request}")
 
#     chatp_prommpt_template   = ChatPromptTemplate.from_messages([system_prompt,human_prompt])
#     chatp_prommpt   = chatp_prommpt_template.format_prompt(diatery="vegan" , region="iran",time="30",reciept_request="ubergin reciept")
#     messages = chatp_prommpt.to_messages()

#     print(f'messages:{messages}')
#     chat_model = ChatOpenAI(temperature=0)  # Adjust temperature for more/less creative responses

#     result = chat_model(messages)
#     print(result)
#     print(result['choices'][0]['message']['content']) 
#     return result.content


def func_ai():
    return 'hello'
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        # Get the parameters from the form
        param1 = request.form.get('param1')
        param2 = request.form.get('param2')
        
        # Run the LangChain command with the provided parameters
        # prompt = f"{param1} {param2}"  # Customize this prompt as needed
        # result = llm(prompt)
        result = func_ai()
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)