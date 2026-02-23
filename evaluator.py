#INITIALIZE
from openai import OpenAI
from dotenv import load_dotenv
import csv

load_dotenv()
client = OpenAI()

#READ TEST CASES FROM CSV
prompts = []

with open("prompts.csv", newline ="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        prompts.append(row["prompt"])

#CREATE the RESULTS CONTAINER
results = []

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

    results.append({
        "prompt": prompt,
        "output": output,
        "word_count": word_count,
        "result": result
    })

    print("\n--- Test Case ---")
    print("PROMPT:")
    print(prompt)

    print("\nMODEL OUTPUT:")
    print(output)

    print("\nEVALUATION")
    print(result)
    print(f"Word count: {word_count}")

with open("results.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["prompt", "output", "word_count", "result"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

