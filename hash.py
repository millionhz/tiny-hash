import hashlib


def hash_it(file, algorithm):
    '''
    Returns hash of the file provided

    Valid algorithms: sha1 | sha256 | md5
    '''
    if algorithm == "sha256":
        hasher = hashlib.sha256()
    elif algorithm == "sha1":
        hasher = hashlib.sha1()
    elif algorithm == "md5":
        hasher = hashlib.md5()
    else:
        raise Exception(
            "Incompatible hash algorithm used. Choose from: sha256 | sha1 | md5")
    with open(file, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="calculate file hashes",
        epilog="the script generates sha256 hash if no argument is provided")
    parser.add_argument("file", action="store",
                        type=str, help="file to hash")
    parser.add_argument("--sha1", action="append_const", const="sha1",
                        dest="algorithm", help="use sha1 for hashing")
    parser.add_argument("--sha256", action="append_const", const="sha256",
                        dest="algorithm", help="use sha256 for hashing")
    parser.add_argument("--md5", action="append_const", const="md5",
                        dest="algorithm", help="use md5 for hashing")
    parser.add_argument("-c", "--compare", action="store",
                        help="compare generated file hash with the provided hash", metavar="HASH")
    data = parser.parse_args()
    # print(data)

    if not data.algorithm:
        data.algorithm = ["sha256"]

    file_hash = {}
    print("Calculating...")
    print()
    for algo in data.algorithm:
        file_hash[algo] = hash_it(data.file, algo)
    # printing
    for algo, c_hash in file_hash.items():
        print(f"{algo}: {c_hash}")
    # compare hash
    if data.compare:
        print()
        if data.compare in file_hash.values():
            print("HASH MATCHED!")
        else:
            print("HASH MATCH FAILED!")
