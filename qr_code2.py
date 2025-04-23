import qrcode
from PIL import Image

# Advance version to make QR as u want ...
# According to your need u can change the color size etc...
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)
qr.add_data("https://github.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="white")
img.save("GitHub.png")