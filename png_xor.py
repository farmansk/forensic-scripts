from PIL import Image, ImageChops

# im1 = Image.open('flag.png').convert("1")
# im2 = Image.open('lemur.png').convert("1")
# im3 = ImageChops.logical_xor(im1, im2)

im1 = Image.open('flag.png')
im2 = Image.open('lemur.png')
im3 = ImageChops.add(ImageChops.subtract(im2, im1), ImageChops.subtract(im1, im2))

im3.save('xorred.png')
