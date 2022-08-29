from PIL import Image
img = Image.open("BHUVI CODES.jpg")
img = img.convert("1")
img.save("black_and_white.jpg")
img.show()
