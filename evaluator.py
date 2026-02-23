#INITIALIZE
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

#INPUT LIST OF TEST CASES
prompts = [
    "Explain artificial intelligence in one sentence.",
    "Explain machine lerning in one sentence.",
    "Explain neural networks in one sentence."
]

#LOOP to collect MODEL RESPONSES for each case
for prompt in prompts:
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

#RUN TEST CASES
    output = response.choices[0].message.content

    word_count = len(output.split())
    
    if word_count > 25:
        result = "FAIL: Too long"
    else: 
        result = "PASS"    

#TEST OUTPUT
    print("\n--- Test Case ---")
    print("PROMPT:")
    print(prompt)

    print("\nMODEL OUTPUT:")
    print(output)

    print("\nEVALUATION")
    print(result)
    print(f"Word count: {word_count}")

