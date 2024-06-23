import qrcode
from PIL import Image
data="The prime minister said even during times of anger and accusations, Birla handled the situation with patience.There were times of anger  accusations but you handled these situations patience ran the House wisely,the prime minister said."
qr=qrcode.QRCode(version=1,box_size=10,border=5)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill="black",back_color="white")
image.save("6qr_code.png")
