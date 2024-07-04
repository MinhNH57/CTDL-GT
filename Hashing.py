import hashlib

data = b"Nguyen Hong Minh"
hash_oject = hashlib.md5(data)
print(hash_oject.hexdigest())