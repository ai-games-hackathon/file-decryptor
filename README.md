# file-decryptor
Simple python command line wrapper around [buffered-encryption package](https://pypi.org/project/buffered-encryption/).
Use this code to decrypt data prepared for AI Games 2022 hackathon.

## Requirements
Use the below command to install the buffered-encryption package.
    
    pip install buffered-encryption

**Note:** You should use at least Python 3.6

## Usage
Use the below command inside the repository directory to decrypt the data file.

    python decrypt_file.py key.key file.zip.encrypted file.zip

* `key.key` is the key provided by organizers.
* `file.zip.encrypted` is the encrypted data file provided by organizers.
* `file.zip` is the destination file for decrypted data.
