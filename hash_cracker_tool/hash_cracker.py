import hashlib
import argparse
import time
from hashid import HashID

def brute_force(user_hash, hash_object):
    """
    Tries to brute force given hash, by creating strings starting from the integer 0.
    
    Args:
        user_hash (string): hash from user
        hash_object (hashlib object): type of inputed algorithm hashlib object  
    
    Returns:
        Nothing
    """

    try:
        number = 0
        start_time = time.time()
        
        while True:     
            
            # Check req bytes to convert 'number' type: int to bytes for hashing
            if number.bit_length() % 8 > 0:
                req_bytes = number.bit_length() // 8 + 1
            else:
                req_bytes = number.bit_length() // 8
                
            byte_number = number.to_bytes(req_bytes, "big")
                            
            number_hash = hash_object(byte_number).hexdigest()
            
            if number_hash == user_hash:
                end = time.time()

                password = byte_number.decode()
                
                print("Hash Cracked!")
                print(f"Hash: {number_hash}")
                print(f"Password: {password}")
                print(f"Words tried: {number}")
                print(f"Time eplased: {round((end - start_time), 2)} seconds")
                
                with open('saved_hashes.txt', 'a+') as saved_file:
                    saved_file.write(f"{password + ":" + number_hash}\n")
                print(f"Cracked password and hash saved to saved_hashes.txt")    
                
                break
            else:
                number = number + 1        
                
    except KeyboardInterrupt:
        end = time.time()
        print("Keyboard interrupt")
        print("Exiting...\n")
        print(f"Words tried: {number}")
        print(f"Time eplased: {round((end - start_time), 2)} seconds")
        # Save number as a startpoint for future brute force?
        
    except UnicodeDecodeError as error:
        print(f"Can't decode byte to string: {error}")    

def check_wordlist(user_hash, hash_object, wordlist):
    """
    Checks inputed hash against worldlist of passwords.
    
    Args:
        user_hash (string): hash from user
        hash_object (hashlib object): type of inputed algorithm hashlib object
        wordlist (string): name of the wordlist file from user  
    
    Returns:
        Nothing
    """
    
    try:
        with open(wordlist, "r") as file:
            password_list = file.read().strip().splitlines()
        
        start = time.time()
        
        for count, pw in enumerate(password_list):
            pw_hash = hash_object(pw.strip().encode()).hexdigest()
            
            if pw_hash == user_hash:
                
                end = time.time()
                
                print("Hash Cracked!")
                print(f"Password: {pw.strip()}")
                print(f"Hash: {pw_hash}")
                print(f"Passwords tried: {count}")
                print(f"Time eplased: {round((end - start), 2)} seconds")
                
                with open('saved_hashes.txt', 'a+') as saved_file:
                    saved_file.write(f"{pw.strip() + ":" + pw_hash}\n")
                print(f"Cracked password and hash saved to saved_hashes.txt")
                
                return

        end = time.time()
        print("No matches found from wordlist")
        print("Try with other wordlist or bruteforce")
        print(f"Time eplased: {round((end - start), 2)} seconds")
    
    except FileNotFoundError as error:
       print(f"File not found error: {error}")
       
    except KeyboardInterrupt:
        end = time.time()
        
        print("\nExiting...")
        print(f"Words tried: {count}")
        print(f"Time eplased: {round((end - start), 2)} seconds")
        # Save count as a startpoint for search?            

def check_hash_type(user_hash):
    """ 
    Checks hash what type of algorithm type. Uses the HashID packet.
        
    Args:
        user_hash (string): hash from user
        
    Returns:
        list: list of possible hash algorithms. if no possible algorithm found return empty list
    """
    
    hashid_object = HashID()
    identified_modes = hashid_object.identifyHash(user_hash)
    
    # Adding identified hash types and check against our 'accepted' types
    hash_types = []

    for mode in identified_modes:
        hash_types.append(mode.name)
    
    if len(hash_types) == 0:
        print("Unknown hash. No possible hash-types found")
        return None
    else:
        return hash_types  


def main():
    try:
        parser = argparse.ArgumentParser(
            prog="Hash Cracker Tool",
            description="My Hash Cracker Tool. Crack with wordlist or bruteforce")
                
        parser.add_argument("hash", help="The Hash to crack")
        parser.add_argument("type", help="Choose an algorithm of md5, sha-1, sha-224, sha-256, sha-384, sha-512")
        parser.add_argument("-w", "--wordlist", help="Crack with wordlist?")
        # parser.add_argument("-t", "--threads", help="Bruteforce with extra threads?")
        
        args = parser.parse_args()

        # valid types exactly as hashID...
        valid_types = ("md5", "sha-1", "sha-224", "sha-256", "sha-384", "sha-512")

        if args.type in valid_types:
            match args.type:
                case "md5":
                    hash_object = hashlib.md5
                case "sha-1":
                    hash_object = hashlib.sha1
                case "sha-224":
                    hash_object = hashlib.sha224
                case "sha-256":
                    hash_object = hashlib.sha256
                case "sha-384":
                    hash_object = hashlib.sha384
                case "sha-512":
                    hash_object = hashlib.sha512
        else:
            print(f"The entered type of algorithm: {args.type}, is not supported")
            print("Exiting...")
            return 
        
        possible_hash_types = check_hash_type(args.hash.strip().lower())

        print("-----------------")
        
        if possible_hash_types:
    
            valid_type = False
            
            for pos_hash in possible_hash_types:
                if pos_hash.lower() == args.type:
                    
                    valid_type = True
                    
                    # Check if hash already in saved_hashes.txt
                    print("Checking in saved_hashes.txt for solution...")
                    with open("saved_hashes.txt", "r") as saved_file:
                        saved_hashes = saved_file.read().strip().splitlines()
                    
                    for saved_hash in saved_hashes:
                        if saved_hash.split(":")[1].strip() == args.hash:
                            print("-----------------")
                            print("Hash already cracked and found in saved_hashes.txt!")
                            print(f"Password: {saved_hash.split(":")[0]}")
                            print("Exiting...")
                            return
                    
                    print("No saved hashes match current hash")
                    print("-----------------")                                  
                    
                    if args.wordlist:
                        print("Proceeding to check hash agains wordlist.txt...")
                        check_wordlist(args.hash.strip().lower(), hash_object, args.wordlist.strip())
                    else:
                        print("Proceeding to brute force hash...")
                        brute_force(args.hash.strip().lower(), hash_object)   
                        
                    print("-----------------")
                    return
                
            if not valid_type:
                
                print(f"Current hash: '{args.hash}'") 
                print(f"Is not compatible with '{args.type}' or at all in this script")
                print(f"Possible hash types identified of inserted hash:")
                
                for pos_hash in possible_hash_types:
                    print(pos_hash)
                    
                print("-----------------")    
                print("Exiting...")
                return           
        else:
            print("Exiting...")
            return     
            
    except Exception as e:
        print(f"Error: {e}")
        print("Exiting...")
    except FileNotFoundError as error:
        print(f"File error: {error}")
        print("Exiting...")


if __name__ == "__main__":
    main()