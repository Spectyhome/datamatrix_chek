from pylibdmtx import pylibdmtx
from PIL import Image

image = Image.open('test.png')

decoded = pylibdmtx.decode(image)

if decoded:
    for code in decoded:
        print("Data Matrix content:", code.data.decode('utf-8'))
        print("Error correction level:", "ECC-200 (по умолчанию)")
else:
    print("Data Matrix не распознан")

for code in decoded:
    data = code.data.decode('utf-8')
    print("Data Matrix content:", data)
    print("ASCII codes:", [ord(char) for char in data])
