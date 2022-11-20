"""
Create QR code using python

import qrcode

data = "www.youtube.com"

img = qrcode.make(data)

img.save('youtube1.png')
----------------------------------------------------
#create QR code using python with different colors of qr code
import qrcode

data = 'Milind Ashok Dhawale'

features = qrcode.QRCode(version= 1,box_size=40,border=5)
features.add_data(data)

features.make(fit = True)

img = features.make_image(fill_color = 'Blue',back_color = 'white')

img.save('img2.png')

"""


