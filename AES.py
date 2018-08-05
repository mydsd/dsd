from Crypto.Cipher import AES
import base64
class Crypt():
    def crypt_aes(self,s,key,iv): #AES加密方法
        pad = lambda s:s + (16 -len(s) % 16) *chr(16 - len(s) % 16) #补足16位
        cipher = AES.new(key, AES.MODE_CBC,iv) #实例化
        msg = cipher.encrypt(pad(s)) #加密输入的字符串
        return base64.b64encode(msg) #二次加密
    def descypt_aes(self,s,key,iv): #解密
        cipherX = AES.new(key, AES.MODE_CBC,iv) #实例化
        bytedt = base64.b64decode(s) #base64解码
        y = cipherX.decrypt(bytedt).decode() #AEX解码
        return y
ae = Crypt()
txt1 = ae.crypt_aes("123","1234567812345678","1234567812345678")
txt = ae.descypt_aes("oLtcaF9Aw5GeyKiaFhnVOQ==","1234567812345678","1234567812345678")
print(txt1,txt)
