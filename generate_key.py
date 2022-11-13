import argparse
from cryptography.fernet import Fernet


parser = argparse.ArgumentParser(
    prog = 'generate_key',
    description = 'Generate Fernet key using Python Cryptography package.'
)

parser.add_argument(
    'filename',
    help='Destination filename for generated key.'
)

args = parser.parse_args()

key_bytes = Fernet.generate_key()
with open(args.filename, 'wb') as f:
    f.write(key_bytes)
