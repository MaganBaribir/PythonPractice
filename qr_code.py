import qrcode
import os

data = 'https://github.com/MaganBaribir/PythonPractice'

filename = "qrcode.png"

save_directory = "Названия папки где вы хотите сохранить QrCode"

save_path = os.path.join(save_directory, filename)

img = qrcode.make(data)

img.save(save_path)
