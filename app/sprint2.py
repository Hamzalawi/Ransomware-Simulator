from cryptography.fernet import Fernet

def gen_key():
    key = Fernet.generate_key()

    with open('key', 'wb') as f:
        f.write(key)

    print("key created")

def encrypt_file(file):
    with open('key', 'rb') as f:
        key = f.read()

    fernet = Fernet(key)
    with open(file, 'rb') as f:
        file_content = f.read()

    encrypted_data = fernet.encrypt(file_content)

    with open(file, 'wb') as f:
        f.write(encrypted_data)

    print(f'succefully encrypted the file: {file}')

def decrypt_file(file):

    with open('key', 'rb') as f:
        key = f.read()

    fernet = Fernet(key)
    with open(file, 'rb') as f:
        encrypted_content = f.read()

    original_data = fernet.decrypt(encrypted_content)

    with open(file, 'wb') as f :
        f.write(original_data)

    print(f'successfully decrypted the file: {file}')

    





if __name__ == "__main__":
    test_file = "secret.txt"
    #gen_key()
    #encrypt_file(test_file)
    decrypt_file(test_file)
