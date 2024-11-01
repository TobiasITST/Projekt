import argparse
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt(rsa_cipher, key_arg, file_arg, en_file):
    try:
        with open(file_arg, "rb") as file:
            data_to_encrypt = file.read()
        
        encrypted_data = rsa_cipher.encrypt(data_to_encrypt)
  
        with open(en_file, "wb") as encoded_file:
            encoded_file.write(encrypted_data)
            
        print(f"Encrypted file '{file_arg}' to '{en_file}' with the key from '{key_arg}'")
        
    except ValueError as error:
        print("Error: the message you trying to encrypt is too long")
    
def decrypt(rsa_cipher, key_arg, en_file, de_file):
    
    try:
        with open(en_file, "rb") as file:
            data_to_decrypt = file.read()
         
        decrypted_data = rsa_cipher.decrypt(data_to_decrypt)
        
        with open(de_file, "wb") as decoded_file:
            decoded_file.write(decrypted_data)
            
        print(f"Decrypted file '{en_file}' to '{de_file}' with the key from '{key_arg}'")

    except FileNotFoundError as error:
        print(error)
    except ValueError as error:
        print("Ciphertext has the wrong length, or decryption failed the integrity check (in which case, the decryption key is probably wrong)")
    except TypeError as error:
        print(error)


def main(args = None):
    
    try:
        parser = argparse.ArgumentParser(description="My crypto tool for symmetric data encryption/decryption")          

        parser.add_argument("key", help="Which file containing your key")
        parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose mode")
        parser.add_argument("file", help="Which file to encrypt/decrypt")

        if not args:
            args = parser.parse_args()
        
        with open(args.key, "rb") as key_file:
            public_key = RSA.import_key(key_file.read())

        rsa_cipher = PKCS1_OAEP.new(public_key)
        
        if args.mode == "encrypt":
            
            if args.file.find(".") == -1:
                en_file = args.file + ".enc"
            else:
                
                if args.file.find("\\") == -1 and args.file.find("/") == -1:
                    en_file = args.file.split(".")[-2] + ".enc"
                elif args.file.find("\\") > -1:
                    en_file = args.file.split(".")[-2].split("\\")[-1] + ".enc"
                elif args.file.find("/") > -1:
                    en_file = args.file.split(".")[-2].split("/")[-1] + ".enc"
                    
            encrypt(rsa_cipher, args.key, args.file, en_file) 
            
        elif args.mode == "decrypt":
            
            en_file = args.file
            de_file = input("Which file to save decrytped data?: ")
            decrypt(rsa_cipher, args.key, en_file, de_file)
          
    except FileNotFoundError as error:
        print(error)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    
    main()