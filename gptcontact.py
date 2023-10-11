import openai 
import os
from dotenv import load_dotenv


def get_task(level, theme=[]):
    load_dotenv()
    print(level, theme)
    openai.api_key = os.environ.get('GPT_TOKEN')
    
    # Define a default value for condit1

    condit1 = ''
    if level == 1:
        condit1 = f'''составь задачу по python  , для человека только начавшего изучаючать язык,
     задача должна быть не слишком простая. Задача должна обязательно содержать темы: {", ".join(theme)}.
     
     '''
    elif level == 2:
        condit1 = '''составь задачу по python  , для человека хорошо знающего язык, задача должна быть не слишком простая'''
    elif level == 3:
        condit1 = '''составь задачу по python  , используя тонкие нюансы языка, используя встроенные библиотеки python, задача должна быть очень сложной'''
    elif level == 4:
        condit1 = 'составь задачу по python  ,для тех кто знает абсолютно все, в задаче должны использоваться библиотеки, например "Numpy" или "Pillow" или "PyQT" (желательно не их) и дай какое-нибудь усложнение'
    model_engine = "text-davinci-003"
    prompt = f'''{condit1} как ты должен это написать:
    ты сразу пишешь задачу, ***без примеров решения и вступительных слов***
    то что ты напишешь будет сразу отправлено в чат телеграмма ботом, построй свое сообщение правильно. 
    ты не должен писать вначале: "Конечно, вот задача для...." или "Конечно, вот задача:"'''
    print(prompt)
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