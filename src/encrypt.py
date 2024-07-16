from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(file_path, "wb") as file:
        file.write(encrypted_data)

def encrypt_all_files(directory):
    key = generate_key()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            encrypt_file(os.path.join(directory, filename), key)

if __name__ == "__main__":
    encrypt_all_files(".")
