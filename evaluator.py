#INITIALIZE
from openai import OpenAI
from dotenv import load_dotenv
import csv

load_dotenv()
client = OpenAI()

#READ TEST CASES FROM CSV
rows = []

with open("prompts.csv", newline ="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        rows.append(row)
        print(rows[0])

#CREATE the RESULTS CONTAINER
results = []

#LOOP to collect MODEL RESPONSES for each case
for row in rows:
    prompt = row["prompt"] 

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

    row["output"] = output
    row["word_count"] = word_count
    row["result"] = result

    print("\n--- Test Case ---")
    print("PROMPT:")
    print(prompt)

    print("\nMODEL OUTPUT:")
    print(output)

    print("\nEVALUATION")
    print(result)
    print(f"Word count: {word_count}")

with open("prompts.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["prompt", "output", "word_count", "result"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(rows)

