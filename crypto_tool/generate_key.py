import argparse
from cryptography.fernet import Fernet
from Crypto.PublicKey import RSA

def rsa(destination):
    try:
        key = RSA.generate(2048)
        
        private_key = key.export_key()
        
        file_name = destination + "RSA_private_key.pem"
        
        with open(file_name, "wb") as private_file:
            private_file.write(private_key)
        print(f"Generated RSA private key saved to {file_name}")

        
        public_key = key.publickey().export_key()
        
        file_name = destination + "RSA_public_key.pem"
        
        with open(file_name, "wb") as public_file:
            public_file.write(public_key)
        print(f"Generated RSA public key saved to {file_name}")    
            
    except FileNotFoundError as error:
        print(error)

        
def sym(destination):
    try:  
        key = Fernet.generate_key() 
        file_name = destination + "secret.key"
        
        with open(file_name, "wb") as key_file:
            key_file.write(key)
        print(f"Generated key saved to {file_name}")
        
    except FileNotFoundError as error:
        print(error)
    
    
def main():
    try:
        parser = argparse.ArgumentParser(description="My symmetric/RSA key(s) generator")          
        
        parser.add_argument("type", choices=["symmetric", "RSA"], help="Choose type of algorithm")
        parser.add_argument("-d", "--destination", help="Destination of generated keys?")
        
        args = parser.parse_args()
        
        if not args.destination:
            args.destination = ""
        
        if args.type == "symmetric":
            sym(args.destination)
        elif args.type == "RSA":
            rsa(args.destination)
        
    except FileNotFoundError as error:
        print(error)
    except TypeError as error:
        print(error)
    except ValueError as error:
        print(error)
    
          
if __name__ == "__main__":
    main()