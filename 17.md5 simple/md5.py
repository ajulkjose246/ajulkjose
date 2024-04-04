import hashlib

def calculate_md5(file_path):
    """
    Calculate the MD5 checksum for a file.
    """
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


file_path = r"D:\43\server.py"

md5_checksum = calculate_md5(file_path)
print("MD5 checksum:", md5_checksum)