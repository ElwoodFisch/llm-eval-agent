#INITIALIZE
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

#INPUT TEST CASE
prompt = "Explain how they can resurrect dinosaurs, in one sentence"

#MODEL RESPONSE
response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

#RUN TEST
output = response.choices[0].message.content
word_count = len(output.split())
if word_count > 25:
    result = "FAIL: Too long"
else: 
    result = "PASS"    

#TEST OUTPUT
print("PROMPT:")
print(prompt)

print("\nMODEL OUTPUT:")
print(output)


print("\nEVALUATION")
print(result)
print(f"Word count: {word_count}")

