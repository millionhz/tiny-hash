# Tiny Hash

A script to calculate and compare file hashes.

Compatible with: sha1 | sha256 | md5.

## Usage

### Calculate SHA256

The script will generate a sha256 hash if no argument is provided.

```code
python hash.py ~/user/hashme.exe
Calculating...

sha256: 74bbb177670cf8e7a0ab4166a0b1039525600e55c262f701167e501f184fa953
```

### Calculating MD5 or SHA1

To calculate md5 or sha1 use the optional `--md5` or `--sha1` argument.

```code
python hash.py ~/user/hashme.exe --md5
Calculating...

md5: 337a05f7c8f119a5e86365869d6397c9
```

### Calculating Multiple Hashes

Multiple hashes can be calculated by providing the relevant arguments together.

```code
python hash.py ~/user/hashme.exe --md5 --sha256
Calculating...

md5: fc968c805a9fc2b898ac590632bdc0a8
sha256: 3b3419fbbd7160dfee504ef5f992d8e345b53e7f
```

### Comparing File Hashes

To compare a hash with the generated hash use `-c` argument.

```code
python hash.py ~/user/hashme.exe -c 74bbb177670cf8e7a0ab4166a0b1039525600e55c262f701167e501f184fa953

Calculating...

sha256: 74bbb177670cf8e7a0ab4166a0b1039525600e55c262f701167e501f184fa953

HASH MATCHED!
```

If you are comparing against a md5 or a sha1 hash, specify the hash algorithm with the relevant argument.

```code
python hash.py ~/user/hashme.exe --md5 -c f5381c7879a072e7cd5ff89b0d94cef2
Calculating...

md5: f5381c7879a072e7cd5ff89b0d94cef2

HASH MATCHED!
```

NOTE: If you are comparing sha256 hashes, you don't need to specify the hashing algorithm with `--sha256` as the script generates sha256 hash by default if no argument is provided.

### For more information use -h or --help

```code
usage: hash.py [-h] [--sha1] [--sha256] [--md5] [-c HASH] file

calculate file hashes

positional arguments:
  file                  file to hash

optional arguments:
  -h, --help            show this help message and exit
  --sha1                use sha1 for hashing
  --sha256              use sha256 for hashing
  --md5                 use md5 for hashing
  -c HASH, --compare HASH
                        compare generated file hash with the provided hash

the script generates sha256 hash if no argument is provided
```
