from cryptography.fernet import Fernet
import os

def load_key():
    return open("key.key", "rb").read()

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_path, "wb") as file:
        file.write(decrypted_data)

def decrypt_all_files(directory):
    key = load_key()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            decrypt_file(os.path.join(directory, filename), key)

if __name__ == "__main__":
    decrypt_all_files(".")
