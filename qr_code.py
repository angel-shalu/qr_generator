# Here qr ar is working as a alias...we can say as a nick name
import qrcode as qr   
img=qr.make("https://www.linkedin.com/feed/")
img.save("my_linkedin.png")

