from PIL import Image
from PIL import ImageChops

print("LTH Initialize")

area = (0, 0, 300, 300)
im2 = ImageGrab.grab(area)
im2.save("STANDER.jpg")