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
            "Incompatible hash algorithm provided. Choose from: sha256 | sha1 | md5")
    try:
        with open(file, 'rb') as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except FileNotFoundError:
        return "Invalid Path or File!"


if __name__ == "__main__":

    import argparse
    parser = argparse.ArgumentParser(
        description="Calculate sha256 hash")
    parser.add_argument("file", action="store",
                        type=str, help="file to hash")
    parser.add_argument("-c", "--compare", action="store",
                        help="compare generated hash with the provided hash", metavar="HASH")
    data = parser.parse_args()
    # calculate hash
    file_hash = hash_it(data.file, "sha256")
    print(f"sha256 of file: {file_hash}")
    # compare hash
    if data.compare:
        if data.compare == file_hash:
            print("HASH MATCHED!")
        else:
            print("HASH MATCH FAILED!")
