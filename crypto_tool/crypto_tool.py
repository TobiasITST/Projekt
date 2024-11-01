import argparse
import symmetric.symmetric as symmetric
import asymmetric.asymmetric as rsa
    
def main():
    
    try:
        parser = argparse.ArgumentParser(description="My crypto tool for generating key(s) and symmetric/asymmetric data encryption/decryption")
            
        parser.add_argument("key", help="Which file containing your key")
        parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Choose mode")
        parser.add_argument("file", help="Which file to encrypt/decrypt")
        parser.add_argument("type", choices=["symmetric", "RSA"], help="Choose type")

        args = parser.parse_args()
        
        if args.type == "symmetric":
            symmetric.main(args)
        elif args.type == "RSA":
            rsa.main(args)
        
    except Exception as e:
        print("Something went wrong. Try again")      
        print(f"Error: {e}") 
        print("Exiting...")
    
if __name__ == "__main__":
    main()