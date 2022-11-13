import argparse
from buffered_encryption.aesgcm import DecryptionIterator


parser = argparse.ArgumentParser(
    prog = 'decrypt_file',
    description = 'Decrypt binary file using provided key.'
)

parser.add_argument(
    'key_file',
    help='Key file.'
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
    key = f.read(32)
    signature = f.read(12)
    iv = f.read(12)
    tag = f.read()

# read encrypted source file
with open(args.source_filename, 'rb') as source_f:
    dec = DecryptionIterator(source_f, key, signature, iv, tag)
    # write encrypted chunks to destination file
    with open(args.destination_filename, 'wb') as destination_f:
        for chunk in dec:
            destination_f.write(chunk)
