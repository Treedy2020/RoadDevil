import openai

default_system_message = "You are a grooming assistant, you always plan and organize grooming for people according to their requirements, return your results in markdown."

OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY
openai.Model.list()


def get_answer(user_message, system_message=default_system_message):
    message =[{'role':'system', 'content': system_message},
            {'role':'user', 'content': user_message}]
    
    advice_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= message,
        )
    
    return advice_response['choices'][0]['message']['content']
        