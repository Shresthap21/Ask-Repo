import os

SUPPORTED_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".java",
    ".go",
    ".cpp",
    ".c"
]

EXCLUDED_DIRECTORIES = {
    ".git",
    "node_modules",
    "__pycache__",
    "dist",
    "build",
    ".next",
    "venv",
    ".venv"
}


def scan_repository(repo_path):
    code_files = []

    for root, dirs, files in os.walk(repo_path):

        # Don't scan generated/dependency folders
        dirs[:] = [
            directory
            for directory in dirs
            if directory not in EXCLUDED_DIRECTORIES
        ]

        for file in files:
            if any(file.endswith(ext) for ext in SUPPORTED_EXTENSIONS):
                full_path = os.path.join(root, file)
                code_files.append(full_path)

    return code_files


def load_file_content(file_path):
    """
    Read and return the content of a file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    except Exception:
        return ""