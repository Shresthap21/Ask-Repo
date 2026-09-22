from core.scanner import scan_repository, load_file_content
from core.chunker import chunk_code
from vector_store.db import store_chunks, search
from ai_assistant import generate_answer


def index_repo(repo_path):

    print("\nScanning repository...\n")

    files = scan_repository(repo_path)

    if not files:
        print("No supported code files found.")
        return False

    print(f"Found {len(files)} code files.")

    all_chunks = []

    for file in files:

        content = load_file_content(file)

        chunks = chunk_code(content)

        for chunk_number, chunk in enumerate(chunks, start=1):

            all_chunks.append({
                "file": file,
                "content": chunk,
                "chunk": chunk_number
            })

    print(f"Created {len(all_chunks)} code chunks.")

    store_chunks(all_chunks)

    print("\nRepository indexed successfully!")

    return True


def ask_question():

    question = input("\nAsk about the codebase (or type 'exit'): ")

    if question.lower() == "exit":
        return False

    results = search(question)

    print("\n" + "=" * 60)
    print("RETRIEVED CODE")
    print("=" * 60)

    for i, result in enumerate(results, start=1):

        print(f"\n[{i}] {result['file']} | Chunk {result['chunk']}")
        print("-" * 60)
        print(result["content"][:700])

    print("\n" + "=" * 60)
    print("GENERATING ANSWER...")
    print("=" * 60)

    answer = generate_answer(question, results)

    print("\nAI Answer:\n")
    print(answer)

    return True


def main():

    repo_path = input("Enter repository path: ")

    success = index_repo(repo_path)

    if not success:
        return

    print("\nAsk questions about your codebase.")
    print("Type 'exit' when you're done.")

    while True:

        if not ask_question():
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()