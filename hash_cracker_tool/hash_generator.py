import hashlib
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="Hash generator",
        description="My Hash Hash generator + extra information")                
    parser.add_argument("type", help="Choose an algorithm of md5, sha-1, sha-224, sha-256, sha-384, sha-512")
    parser.add_argument("string", help="String to hash")
    args = parser.parse_args()

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

        print("--------------------------")

        plain = args.string
        print(f"plain: {plain}")

        plain_bytes = plain.encode()
        print(f"plain in byte: {plain_bytes}")

        plain_int = int.from_bytes(plain.encode())
        print(f"plain in int: {plain_int}")

        print("--------------------------")

        nhash = hash_object(plain.encode()).hexdigest()
        print(f"hash: {nhash}")

        print("--------------------------")

        print(f"plaint int bit length: {plain_int.bit_length()}")
        print(f"bit length / 8: {((plain_int.bit_length()) / 8)}")
        print(f"bit length // 8: {(plain_int.bit_length()) // 8}")
        print(f"bit length % 8: {(plain_int.bit_length()) % 8}")

        print("--------------------------")

        if (plain_int.bit_length() % 8) > 0:
            req_bits = plain_int.bit_length() // 8 + 1
        else:

            req_bits = plain_int.bit_length() // 8
        
        print("Required bytes for 'int.to_bytes()' funtion")    
        print(f"req bytes: {req_bits}")
        print("--------------------------")

    else:
        print(f"The entered type of algorithm: {args.type}, is not supported")
        print("Exiting...")
        

if __name__ == "__main__":
    main()