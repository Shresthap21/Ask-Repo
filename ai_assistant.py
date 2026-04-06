import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(question, retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:
        context += f"\nFile: {chunk['file']}\n{chunk['content']}\n"

    prompt = f"""
You are an AI assistant helping understand a codebase.

Use the following code snippets to answer the question.

Question:
{question}

Code:
{context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content