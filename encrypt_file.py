import argparse
import os
from buffered_encryption.aesgcm import EncryptionIterator


parser = argparse.ArgumentParser(
    prog = 'encrypt_file',
    description = 'Encrypt binary file key and generate random encryption key.'
)

parser.add_argument(
    'source_filename',
    help='Source file.'
)
parser.add_argument(
    'destination_filename',
    help='Encrypted destination file.'
)
parser.add_argument(
    'key_filename',
    help='Generated key destination file.'
)

args = parser.parse_args()

key = os.urandom(32)
signature = os.urandom(12)

# read source file
with open(args.source_filename, 'rb') as source_f:
    enc = EncryptionIterator(source_f, key, signature)
    # write encrypted chunks to destination file
    with open(args.destination_filename, 'wb') as destination_f:
        for chunk in enc:
            destination_f.write(chunk)

# create key file
with open(args.key_filename, 'wb') as f:
    f.write(key)
    f.write(signature)
    f.write(enc.iv)
    f.write(enc.tag)
