from dotenv import load_dotenv
load_dotenv(".env.local")
import os
import google.generativeai as genai


# if in lite mode, setup api call
BACKEND_MODE = os.getenv("BACKEND_MODE", "normal")
if BACKEND_MODE == "lite":
    system_prompt = "return a clever comeback to the users roast:"
    genai.configure(api_key= os.getenv("API_KEY"))
    model = genai.GenerativeModel(system_instruction= system_prompt)


def generate_lite(roast:str) -> str:
    output = model.generate_content(roast).text
    return output


def generate(roast:str) -> str:
    return "TODO: make custom model for normal mode"