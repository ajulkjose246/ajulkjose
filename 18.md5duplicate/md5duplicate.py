import hashlib
import os

def calculate_md5(file_path, blocksize=65536):
    md5_hash = hashlib.md5()
    with open(file_path, 'rb') as file:
        for block in iter(lambda: file.read(blocksize), b''):
            md5_hash.update(block)
    return md5_hash.hexdigest()

def find_duplicate_files(directory):
    checksum = {}
    duplicates = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            md5 = calculate_md5(file_path)

            if md5 in checksum:
                duplicates.append((file_path, checksum[md5]))
            else:
                checksum[md5] = file_path

    return duplicates

directory_to_search = r'C:\java\bin\50 ACN'
duplicate_files = find_duplicate_files(directory_to_search)

if duplicate_files:
    print("Duplicate files found:")
    for file1, file2 in duplicate_files:
        print(f"  - {file1} and {file2}")
else:
    print("No duplicate files found.")