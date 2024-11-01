import argparse
import cryptography.fernet

def encrypt(cipher_suite, key_arg, file_arg, en_file):
    
    with open(file_arg, "rb") as file:
        data_to_encrypt = file.read()
    
    encrypted_data = cipher_suite.encrypt(data_to_encrypt)
        
    with open(en_file, "wb") as encoded_file:
        encoded_file.write(encrypted_data)
        
    print(f"Encrypted file '{file_arg}' to '{en_file}' with the key from '{key_arg}'")

   
def decrypt(cipher_suite, key_arg, en_file, de_file):
    try:
        with open(en_file, "rb") as file:
            data_to_decrypt = file.read()
         
        decrypted_data = cipher_suite.decrypt(data_to_decrypt)
        
        with open(de_file, "wb") as decoded_file:
            decoded_file.write(decrypted_data)
            
        print(f"Decrypted file '{en_file}' to '{de_file}' with the key from '{key_arg}'")

    except FileNotFoundError as error:
        print(error)
    except cryptography.fernet.InvalidToken as error:
            print("Invalid Token Error: A token may be invalid for a number of reasons: it is older than the ttl, it is malformed, or it does not have a valid signature.")
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
            key = key_file.read()

        cipher_suite = cryptography.fernet.Fernet(key)
        
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
                    
            encrypt(cipher_suite, args.key, args.file, en_file) 
            
        elif args.mode == "decrypt":
            
            en_file = args.file
            de_file = input("Which file to save decrytped data?: ")
            decrypt(cipher_suite, args.key, en_file, de_file)
          
    except FileNotFoundError as error:
        print(error)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
        
if __name__ == "__main__":
    main()
