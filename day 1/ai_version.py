import os
import openai
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

openai.api_type = "azure"
openai.api_base = "https://policycon-ai-operations.openai.azure.com/"
openai.api_version = "2023-09-15-preview"


def generateBandName():
    print("Band Name Generator, Get a name for your band")
    city_name = input("Enter the name of your city: ")
    pet_name = input("Enter the name of your pet: ")

    input_text = f"Generate a nickname for a musician based on his city: {city_name} and pet name: {pet_name}"

    client = AzureOpenAI(
        azure_endpoint="https://policycon-ai-operations.openai.azure.com/",
        api_key=os.getenv("AI_KEY"),
        api_version="2024-02-15-preview"
    )
    # Use OpenAI's text model to generate the summary
    response = client.chat.completions.create(

        messages=[
            {
                "role": "user",
                "content": f"{input_text}",
            }
        ],
        model="policy_review_integrations"
    )
    print("Your music nickname should be: ", response.choices[0].message.content)


generateBandName()
