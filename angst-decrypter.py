import sys, base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

if len(sys.argv) <3 :
    print(f"Usage: {sys.argv[0]} encrypted.ext.angst decrypted.ext key")
    exit(1)

key = base64.b64decode(sys.argv[3])

def decrypt(ciphertext):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return decrypted

with open(sys.argv[1],"rb") as encrypted:
    contents = decrypt(encrypted.read())
with open(sys.argv[2],"wb") as decrypted:
    decrypted.write(contents)
