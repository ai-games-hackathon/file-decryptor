import argparse
from cryptography.fernet import Fernet


parser = argparse.ArgumentParser(
    prog = 'encrypt_file',
    description = 'Encrypt binary file using Fernet key.'
)

parser.add_argument(
    'key_file',
    help='Fernet key file.'
)

parser.add_argument(
    'source_filename',
    help='Source file.'
)
parser.add_argument(
    'destination_filename',
    help='Encrypted destination file.'
)

args = parser.parse_args()

# read key file
with open(args.key_file, 'rb') as f:
    key_bytes = f.read()
    key = Fernet(key_bytes)

# read source file
with open(args.source_filename, 'rb') as f:
    file_bytes = f.read()

# encrypte source file data
encrypted_file_bytes = key.encrypt(file_bytes) 

# write encrypted data to destination file
with open(args.destination_filename, 'wb') as f:
    f.write(encrypted_file_bytes)
