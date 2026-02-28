import hashlib

def calculate_hash(filepath, algorithm="sha256"):
    hash_func = hashlib.new(algorithm)

    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                hash_func.update(chunk)

        return hash_func.hexdigest()

    except Exception:
        return None
def hash_file(filepath, algorithm="sha256"):
    import hashlib

    hash_func = hashlib.new(algorithm)

    with open(filepath, "rb") as f:
        while chunk := f.read(4096):
            hash_func.update(chunk)

    return hash_func.hexdigest()
