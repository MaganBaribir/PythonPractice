import qrcode
import os

data = '...'

filename = "qrcode.png"

save_directory = "..."

save_path = os.path.join(save_directory, filename)

img = qrcode.make(data)

img.save(save_path)
