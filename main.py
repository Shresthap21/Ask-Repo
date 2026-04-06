from core.scanner import scan_repository, load_file_content
from core.chunker import chunk_code
from vector_store.db import store_chunks, search
from ai_assistant import generate_answer


def index_repo(repo_path):

    files = scan_repository(repo_path)

    all_chunks = []

    for file in files:

        content = load_file_content(file)

        chunks = chunk_code(content)

        for chunk in chunks:
            all_chunks.append({
                "file": file,
                "content": chunk
            })

    print("Total chunks:", len(all_chunks))

    store_chunks(all_chunks)


def ask_question():

    question = input("\nAsk about the codebase: ")

    results = search(question)

    answer = generate_answer(question, results)

    print("\nAI Answer:\n")
    print(answer)


def main():

    repo_path = input("Enter repository path: ")

    index_repo(repo_path)

    while True:
        ask_question()


if __name__ == "__main__":
    main()