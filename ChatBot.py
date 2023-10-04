import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)