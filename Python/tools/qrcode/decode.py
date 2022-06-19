from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('D:/Backup/Work/DevOps/Python/Scripts/Python/qrcode/myqrcode.png')

result = decode(img)

print(result)