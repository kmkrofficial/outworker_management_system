import base64
from PIL import Image
import io

with open("D:\\Projects\\FMS\\image.jpg", "rb") as image:
    b64string = base64.b64encode(image.read())
print(len(b64string))
f = io.BytesIO(base64.b64decode(b64string))
Image.open(f)
