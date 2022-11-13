import argparse
from cryptography.fernet import Fernet


parser = argparse.ArgumentParser(
    prog = 'decrypt_file',
    description = 'Decrypt binary file using Fernet key.'
)

parser.add_argument(
    'key_file',
    help='Fernet key file.'
)

parser.add_argument(
    'source_filename',
    help='Encrypted source file.'
)
parser.add_argument(
    'destination_filename',
    help='Decrypted destination file.'
)

args = parser.parse_args()

# read key file
with open(args.key_file, 'rb') as f:
    key_bytes = f.read()
    key = Fernet(key_bytes)

# read source file
with open(args.source_filename, 'rb') as f:
    encrypted_file_bytes = f.read()

# encrypte source file data
file_bytes = key.decrypt(encrypted_file_bytes) 

# write encrypted data to destination file
with open(args.destination_filename, 'wb') as f:
    f.write(file_bytes)
