# System imports
from hashlib import sha3_512
import subprocess

# Packages imports
from PIL import Image


class ExtendedImage(object):
    def __init__(self, img):
        self.img = img
        self.width = img.width
        self.height = img.height

    def encryptimg(self, passkey, pathtosave):
        print("Generating Keys for Encryption....")
        keys = self.keysgen(passkey)
        count = 0
        imgpixels = self.img.load()
        print("Encrypting Image....")
        for i in range(0, self.width):
            for j in range(0, self.height):
                oi = (keys[count] ^ i) % self.width
                oj = (keys[count + 1] ^ j) % self.height

                clr = imgpixels[i, j]
                imgpixels[i, j] = imgpixels[oi, oj]
                imgpixels[oi, oj] = clr

                count += 1
                if count >= (len(keys) - 1):
                    count = 0
        if pathtosave != "":
            print("Saving Image.....")
            self.img.save(pathtosave)

    def decryptimg(self, passkey, pathtosave):
        print("Generating Keys for Decryption....")
        keys = self.keysgen(passkey)
        imgpixels = self.img.load()
        count = ((self.width * self.height) % (len(keys) - 1)) - 1
        print("Decrypting Image....")
        for i in range(self.width - 1, -1, -1):
            for j in range(self.height - 1, -1, -1):
                oi = (keys[count] ^ i) % self.width
                oj = (keys[count + 1] ^ j) % self.height

                clr = imgpixels[i, j]
                imgpixels[i, j] = imgpixels[oi, oj]
                imgpixels[oi, oj] = clr

                count -= 1
                if count <= -1:
                    count = len(keys) - 2
        if pathtosave != '':
            print("Saving Image....")
            self.img.save(pathtosave)

    def show(self):
        self.img.show()

    def keysgen(self, passkey):
        nofkeys = min(4095, max(2047, 2 * (max(self.width, self.height))))
        keysarr = []
        raw = ""
        rawhash = sha3_512(passkey.encode()).hexdigest()
        rawhash = sha3_512(rawhash[0:64].encode()).hexdigest() + \
                sha3_512(rawhash[64:128].encode()).hexdigest()
        for i in range(0, len(rawhash)):
            raw += bin(ord(rawhash[i]))[2:]
        raw = raw[:1601]
        i = count = 0
        rawlen = len(raw)
        keylen = len(bin(max(self.width, self.height)))
        while count < nofkeys:
            end = (i + keylen)
            if end <= (rawlen - 1):
                key = raw[i:end]
            else:
                key = raw[i:rawlen - 1]
                key += raw[0:end - rawlen]
            keysarr.append(int(key, 2) ^ count)
            count += 1
            i = (i + keylen) % rawlen
        return keysarr

    @staticmethod
    def genimg(text, path):
        strlen = len(text)

        arr = text.split(' ')
        maxlen = 0
        for x in arr:
            if len(x) > maxlen:
                maxlen = len(x)

        if strlen <= 72 and maxlen <= 8:
            size = 128
        elif strlen <= 256 and maxlen <= 16:
            size = 288
        elif strlen <= 1280 and maxlen <= 32:
            size = 512
        else:
            size = 1024
        size = str(size)
        subprocess.call(['scripts/image_generator.sh', size, text, path])


if __name__ == "__main__":
    image = ExtendedImage(Image.open("/home/krishna/Desktop/testimages/example.png"))
    image.encryptimg("sdlfkjaldskfja", "/home/krishna/Desktop/encrypted.png")
    image.decryptimg("sdlfkjaldskfja", "/home/krishna/Desktop/decrypted.png")
