import hashlib

data = b"You got Hacked"

print("MD5:", hashlib.md5(data).hexdigest())
print("SHA1:", hashlib.sha1(data).hexdigest())
print("SHA256:", hashlib.sha256(data).hexdigest())



print ("...printing hash again for comparison...")
print(hashlib.sha256(data).hexdigest())