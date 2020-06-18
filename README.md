# Tiny Hash

A script to calculate and compare file hashes.

Compatible with: sha1 | sha256 | md5.

## Usage

### Calculate SHA256

By default the script will generate a sha256 when a file is provided.

```code
python hash.py ~/user/hashme.exe
Calculating Hash...

sha256: 74bbb177670cf8e7a0ab4166a0b1039525600e55c262f701167e501f184fa953
```

### Calculating MD5

To calculate md5 or sha1 use the optional `-a` argument.

NOTE: You can only choose sha1, sha256 or md5 algorithms for now.

```code
python hash.py ~/user/hashme.exe -a md5
Calculating Hash...

md5: 337a05f7c8f119a5e86365869d6397c9
```

### Calculating Multiple Hashes

The `-a` argument can take multiple values in case you want to generate more than one hash.

```code
python hash.py ~/user/hashme.exe -a md5 sha1
Calculating Hash...

md5: fc968c805a9fc2b898ac590632bdc0a8
sha1: 3b3419fbbd7160dfee504ef5f992d8e345b53e7f
```

### Comparing File Hashes

To compare a hash with the generated hash use `-c` argument.

```code
python hash.py ~/user/hashme.exe -c 74bbb177670cf8e7a0ab4166a0b1039525600e55c262f701167e501f184fa953

Calculating Hash...

sha256: 74bbb177670cf8e7a0ab4166a0b1039525600e55c262f701167e501f184fa953

HASH MATCHED!
```

If you are comparing against a md5 hash or a sha1 hash, specify the hash algorithm with the `-a` argument.

NOTE: You didn't have to specify sha256 in the above example as the script generates sha256 hash by default.

```code
python hash.py ~/user/hashme.exe -a md5 -c f5381c7879a072e7cd5ff89b0d94cef2
Calculating Hash...

md5: f5381c7879a072e7cd5ff89b0d94cef2

HASH MATCHED!
```

### For more information use --help

```code
python hash.py --help
usage: hash.py [-h] [-a  [...]] [-c HASH] file

calculate file hashes

positional arguments:
  file                  file to hash

optional arguments:
  -h, --help            show this help message and exit
  -a  [ ...], --algorithm  [ ...]
                        algorithms to use for hashing a file (choose from 'sha1', 'sha256', 'md5')
  -c HASH, --compare HASH
                        compare file hash with the provided hash

by default the script generates sha256 hash
```
