import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_answer(question, retrieved_chunks):

    context = ""

    for chunk in retrieved_chunks:

        context += f"""
File: {chunk['file']}
Chunk: {chunk['chunk']}

{chunk['content']}

-------------------------
"""

    prompt = f"""
You are an AI assistant helping a developer understand a codebase.

Answer the question using only the provided code context.

If the answer cannot be determined from the provided context,
clearly say that the retrieved code does not contain enough information.

Mention relevant file names when useful.

Question:
{question}

Retrieved code context:
{context}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content