# CryCry
A toolkit for doing basic operations on bits, bytes and cryptography.
Includes helper scripts that do useful things.

Example usage:

```
cc-xor /etc/passwd /etc/hosts|cc-encode --base64

cc-echo Hello World|cc-encode|cc-decode

cc-pkdump privkey.pem
```


## Install
You can install CryCry using pip:

```
pip install git+https://github.com/rugo/crycry.git
```

