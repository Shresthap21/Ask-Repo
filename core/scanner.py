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

def scan_repository(repo_path):
    code_files = []
    
    for root, dirs, files in os.walk(repo_path):
        if ".git" in root or "node_modules" in root or "__pycache__" in root:
            continue
        
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