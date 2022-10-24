from base64 import b64encode
from Crypto.PublicKey import RSA
from base64 import b64decode,b64encode

private_key = RSA.generate(2048)
pubkey = private_key.publickey()


private_key = b64encode((private_key.exportKey('DER')) ).decode("utf-8")
pubkey = b64encode(pubkey.exportKey()).decode("utf-8")

print(private_key)


# msg = "test"
# keyDER = b64decode(private_key)
# key = RSA.importKey(keyDER)
# # cipher = Cipher_PKCS1_v1_5.new(keyPub)
# # cipher_text = cipher.encrypt(msg.encode())
# # emsg = b64encode(cipher_text)
# # key = RSA.import_key(private_key)
# print(key)


with open("data/keys/PUK.txt", "a") as f:
    f.write(pubkey)
    f.close()

with open("data/keys/PRK.txt", "a") as f:
    f.write(private_key)
    f.close()
