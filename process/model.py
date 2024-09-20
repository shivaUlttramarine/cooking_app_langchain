import os

######### langchain
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate,ChatPromptTemplate,SystemMessagePromptTemplate,AIMessagePromptTemplate,HumanMessagePromptTemplate
from langchain.schema import HumanMessage, SystemMessage
# import reciept as rcp
from pydantic import BaseModel
import openai
import requests
# os.environ["OPENAI_API_KEY"]= "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"
# openai.api_key = "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"





class reciept():
    ingredients: list[str]  
    instructions: list[str]  
    images_with_descriptions= []


    def __init__(self,ingredients,instructions):
        self.ingredients = ingredients
        self.instructions   = instructions


    def get_images(self):
        return self.images_with_descriptions

    def visualize(self):
        older_lines=' Getting ready to cook.'
        self.images_with_descriptions = []
        step =1
        for line in self.instructions:
            print(f'-----line:{line}')
            # prompt = f"a chef has already done {older_lines}. now picture {line}"
            prompt = f"You are a chef who is cooking a dish. Show a picture where you  {line}"
            print(f'-----image promt:{prompt}')

            # if step <=1:
            image_url = self.func_ai_generate_image(prompt)
            print(f"-----Generated Image URL: {image_url}")
            img_name    = f"step_{step}.png"
            img_address = f"static/images/{img_name}"
            self.images_with_descriptions.append({"filename":img_address,"description":line})
            self.save_image(image_url, img_address)
            step=step+1
    

    def func_ai_generate_image(self,prompt):
        response = openai.Image.create(
            prompt=prompt,
            n=1,  # Number of images to generate
            size="512x512"  # Image size (can be "256x256", "512x512", or "1024x1024")
        )
        # Extract the URL of the generated image
        image_url = response['data'][0]['url']
        return image_url

    def save_image(self,image_url, file_path):
        response = requests.get(image_url)
        with open(file_path, 'wb') as file:
            file.write(response.content)

    def print(self):
        ans = f"ingredients:{self.ingredients} \n  instructions:{self.instructions}"





def func_ai_create_recept(selected_ingredients,selected_cooking_time) -> reciept:
    system_template = "You are an AI recept assitant that is specialized in cooking dishes. Suggust a famiouse dish with any of these ingredients   {ingredients} that are cooked in about {time} minutes or less. "
    system_prompt   = SystemMessagePromptTemplate.from_template(system_template)
    human_prompt    = HumanMessagePromptTemplate.from_template("{reciept_request}")

    chatp_prommpt_template  = ChatPromptTemplate.from_messages([system_prompt,human_prompt])
    chatp_prommpt           = chatp_prommpt_template.format_prompt(ingredients=selected_ingredients ,time=selected_cooking_time,reciept_request="all ingredients and reciept")
    messages                = chatp_prommpt.to_messages()

    print(f'messages:{messages}')
    chat_model = ChatOpenAI(temperature=0)  # Adjust temperature for more/less creative responses

    result = chat_model(messages)
    

    print(f'******* rsutlt:{result}')
    # print(result['choices'][0]['message']['content']) 
    recept      = result.content
    sentences   = recept.split('\n')
    sentences   = [x for x in sentences if x!='']
    print(f'recept:{recept}')
    ingredients = recept.split("Instructions:")[0].replace("Ingredients:", "").strip()
    instructions= recept.split("Instructions:")[1].strip()    
    ingredients = ingredients.split('\n')
    instructions= instructions.split('\n')

    
    # instructions = [   '1. In a large bowl, mix together the grated potatoes and oats.',
    #                 '2. Season the mixture with salt and pepper to taste.',
    #                 '3. Heat some oil in a non-stick skillet over medium heat.',
    #                 '4. Scoop out a spoonful of the potato-oat mixture and place it in the skillet, flattening it with a spatula to form a pancake shape.',
    #                 '5. Cook the pancake for about 3-4 minutes on each side, or until golden brown and crispy.',
    #                 '6. Repeat with the remaining potato-oat mixture, adding more oil to the skillet as needed.',
    #                 '7. Once all the pancakes are cooked, serve hot and enjoy!']
    
    # ingredients = [  '- 2 medium potatoes, peeled and grated',
    #                 '- 1 cup oats',
    #                 '- Salt and pepper to taste',
    #                 '- Oil for frying']
    # print('ingredients')
    # print(ingredients)
    # print('ingredients')
    # print(ingredients)
    return reciept(ingredients=ingredients,instructions=instructions)

