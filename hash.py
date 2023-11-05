import hashlib

def enc(message):
    md5=hashlib.md5()
    md5.update(message.encode('utf-8'))
    return md5.hexdigest()

def enc1(message):
    sha1=hashlib.sha1()
    sha1.update(message.encode('utf-8'))
    return sha1.hexdigest()
message=input("Enter the input string")
print(f"MD5 Hashed String:{enc(message)}")
print(f"SHA-I Hashed String :{enc1(message)}")