from openai import OpenAI
client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a text book"},
    {"role": "user", "content": "Tell me what is RAG in AI?"},
  ]
)

message = response.choices[0].message.content
print(message)