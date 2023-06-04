import hashlib
from argparse import ArgumentParser


def hashfile(filename, algorithm):
    hs = None

    match algorithm:
        case 'sha256':
            hs = hashlib.sha256()
        case 'sha512':
            hs = hashlib.sha512()
        case 'md5':
            hs = hashlib.md5()
        case 'sha3_256':
            hs = hashlib.sha3_256()
    
    with open(filename, 'rb') as f:    
        chunk = f.read()
        hs.update(chunk)

    return hs.hexdigest()


def main():
    parser = ArgumentParser()

    parser.add_argument('filename', help='specify a file to get it\'s hash')
    parser.add_argument('-alg', choices=['sha256', 'sha512', 'sha3_256', 'md5'], default='sha256',
                        help='specify an algorithm to perform hashing')
    # Create a namespace of arguments
    arg = parser.parse_args()
    # Get hexdigested hash of the file
    hash = hashfile(arg.filename, arg.alg)
    
    with open("Hashes.txt", 'a+') as file:
        file.write(f"{arg.filename} ({arg.alg}): ")
        file.write(hash)
        file.write('\n')



if __name__ == '__main__':
    main()
