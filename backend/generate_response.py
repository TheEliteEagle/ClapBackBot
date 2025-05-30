from transformers import pipeline

model = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B", device=0)
SYSTEM_PROMPT = "return a clever comeback to the users roast"

def generate(roast:str) -> str:

    output = model(f"{SYSTEM_PROMPT} User roast: {roast} Comeback:")

    return output[-1]["generated_text"].split("Comeback:", 1)[1].strip()