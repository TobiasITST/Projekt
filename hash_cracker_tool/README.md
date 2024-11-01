# Hash Cracker Tool
This is a tool to crack password hexadecimal hashes.
Supports hash algorithms md5, sha-1, sha-224, sha-256, sha-384 and sha-512.

Utilizes the ´hashlib´ module from python standard library.

Bonus script '[hash_generator.py](#hash-generator)' created for generating hashes from user input. See below

### How to use Hash Cracker Tool
    example > python hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 md5 wordlist.txt
    
or

    example > python hash_cracker.py 40bd001563085fc35165329ea1ff5c5ecbdbbeef sha-1

##### Arguments
| Flag | Description |
| :----------- | :----------- |
|`hash`| Given hash|
|`algorithm`| Choices=`md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`. Algorithms to crack hash|
|`wordlist`| `wordlist.txt` for example|

### Requires
- [HashID](https://pypi.org/project/hashID/)
- run `pip install hashid`

### Limitations
- Developed and tested on Windows OS
- Can't crack other than UTF-8 encoded hashed passwords
- Bruteforce is not optimal for 'words' larger than 3 characters
- Tried to implement multithreading or multiprocessing, could find a working solution.

-----------------------------------
<br>

## Hash generator
Generates hash of inputed string and type of hash algorithm
### How to use Hash generator
    example > python hash_generator.py sha-1 password
##### Arguments
| Flag | Description |
| :----------- | :----------- |
|`algorithm`| Choices=`md5`, `sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha-512`. Algorithms to hash the text|
|`string`| Text to hash|

### Limitations
- Developed and tested on Windows OS
