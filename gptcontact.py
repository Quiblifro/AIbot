import openai 
import os
from dotenv import load_dotenv


def get_task(level = 1, theme = []):
    load_dotenv()
    openai.api_key = os.environ.get('GPT_TOKEN')
    model_engine = "text-davinci-003"
    prompt = "Write poem about how cool readers of uproger website"

    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return completion.choices[0].text