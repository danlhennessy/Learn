import qrcode

#Required: pip install qrcode, pip install pillow


data = "https://github.com/danlhennessy/"

img = qrcode.make(data)

img.save('D:/Backup/Work/DevOps/Python/Scripts/Python/qrcode/myqrcode.png')