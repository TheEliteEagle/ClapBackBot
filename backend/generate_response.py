from dotenv import load_dotenv
import os
import google.generativeai as genai


# setup AI model
system_prompt = "return a clever comeback to the users roast:"
load_dotenv(".env.local")
genai.configure(api_key= os.getenv("API_KEY"))
model = genai.GenerativeModel(system_instruction= system_prompt)


def generate(roast:str) -> str:

    # TODO improve using modern methods
    output = model.generate_content(roast).text
    return output