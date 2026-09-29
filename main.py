from core.scanner import scan_repository, load_file_content
from core.chunker import chunk_code
from vector_store.db import store_chunks, search
from ai_assistant import generate_answer
import os
import shutil
import subprocess
import tempfile

def prepare_repository(repo_input):
    """
    Accept either a local repository path or a GitHub URL.
    """

    if repo_input.startswith("https://github.com/"):
        temp_dir = tempfile.mkdtemp()

        print("\nCloning GitHub repository...\n")

        subprocess.run(
            ["git", "clone", "--depth", "1", repo_input, temp_dir],
            check=True
        )

        return temp_dir, True

    if os.path.isdir(repo_input):
        return repo_input, False

    print("Invalid repository path or GitHub URL.")
    return None, False

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

    print("\nSearching codebase...")
    print(f"Found {len(results)} relevant code sections.")

    print("\n" + "=" * 60)
    print("GENERATING ANSWER...")
    print("=" * 60)

    answer = generate_answer(question, results)

    print("\nAI Answer:\n")
    print(answer)

    return True


def main():

    repo_input = input("Enter local repository path or GitHub URL: ")

    repo_path, is_temp = prepare_repository(repo_input)

    if not repo_path:
        return

    try:
        success = index_repo(repo_path)

        if not success:
            return

        print("\nAsk questions about your codebase.")
        print("Type 'exit' when you're done.")

        while True:

            if not ask_question():
                print("\nGoodbye!")
                break

    finally:
        if is_temp:
            shutil.rmtree(repo_path, ignore_errors=True)


if __name__ == "__main__":
    main()