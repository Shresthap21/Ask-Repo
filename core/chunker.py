def chunk_code(content, chunk_size=500, overlap=50):
    """
    Split code into chunks with overlap.
    """

    chunks = []

    start = 0

    while start < len(content):

        end = start + chunk_size

        chunk = content[start:end]

        chunks.append(chunk)

        start += chunk_size - overlap

    return chunks