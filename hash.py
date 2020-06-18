import hashlib
import sys


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
    try:
        with open(file, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except FileNotFoundError:
        return "Invalid Path or File!"


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="Calculate hashes",
        epilog="By default the script generates sha256 hash")
    parser.add_argument("file", action="store",
                        type=str, help="file to hash")
    parser.add_argument("-a", "--algorithm", action="store", nargs="+", default=["sha256"], choices=["sha1", "sha256", "md5"],
                        type=str, help="algorithms to use for hashing", required=False)
    parser.add_argument("-c", "--compare", action="store",
                        help="compare sha1, sha256 and md5 with the provided hash", metavar="HASH")
    data = parser.parse_args()
    # print(data)
    # if data.compare:
    #     data.algorithm = ["sha1", "sha256", "md5"]
    # calculate hash
    file_hash = {}
    print("Calculating Hash...")
    print()
    for algo in data.algorithm:
        file_hash[algo] = hash_it(data.file, algo)
    # printing
    for algo ,c_hash in file_hash.items():
        print(f"{algo}: {c_hash}")
    # compare hash
    if data.compare:
        print()
        if data.compare in file_hash.values():
            print("HASH MATCHED!")
        else:
            print("HASH MATCH FAILED!")