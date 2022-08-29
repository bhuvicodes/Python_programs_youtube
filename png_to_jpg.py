from PIL import Image
import os

im = Image.open("BHUVI CODES.png")
print("The size of the image before conversion: ",end="")
print(os.path.getsize("BHUVI CODES.png"))

rgb_im = im.convert("RGB")
rgb_im.save("BHUVI CODES.jpg")
print("The size of the image after conversion: ", end="")
print(os.path.getsize("BHUVI CODES.jpg"))
