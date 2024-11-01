# Crypto tool and Key generator
Simple tool to encrypt and decrypt with either symmetric or asymmetric (RSA) algorithms.
Key generator tool for symmetric or asymmetric (RSA) algorithms.

### How to use Key generator
    example > python generate_key.py symmetric

or
    
    example > python generate_key.py RSA -d .\keys\


##### Arguments
| Flag | Description |
| :----------- | :----------- |
|`type`| Choices=`symmetric`, `RSA`. Type of algorithm|
|`-d` or `destination`| Enter the destination(existing) of generated keys|

### Requires
- [Cryptography package](https://cryptography.io/en/stable/)
- [PyCryptodome package](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html)
- run `pip install cryptography pycryptodome`
### Limitations
- Developed and tested on Windows OS
- Key length, or size (in bits) of the RSA defined to 2048 bits

--------------------------------------
<br>

### How to use Crypto tool
    example > python crypto_tool.py secret.key encrypt README.md symmetric
##### Arguments
| Flag | Description |
| :----------- | :----------- |
|`key`| Which file containing your key|
|`mode`| Choices=`encrypt`, `decrypt`. Use the tool to encrypt or decrypt file?|
|`file`| Which file to encrypt/decrypt|
|`type`| Choices=`symmetric`, `RSA`. Type of algorithm|

### Requires
- [Cryptography package](https://cryptography.io/en/stable/)
- [PyCryptodome package](https://pycryptodome.readthedocs.io/en/latest/src/introduction.html)
- run `pip install cryptography pycryptodome`
### Limitations
- Developed and tested on Windows OS
- Maby not so useful tool.
- Kinda wonky with all required arguments