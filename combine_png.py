from PIL import Image, ImageOps
import itertools

# Open your images
image1 = Image.open("C:\\Users\\91954\\Downloads\\crypto-200\\share_0.png")
image2 = Image.open("C:\\Users\\91954\\Downloads\\crypto-200\\share_1.png")
image3 = Image.open("C:\\Users\\91954\\Downloads\\crypto-200\\share_2.png")
image4 = Image.open("C:\\Users\\91954\\Downloads\\crypto-200\\share_3.png")
image5 = Image.open("C:\\Users\\91954\\Downloads\\crypto-200\\share_4.png")

# Create a blank image as the base
width, height = image1.size
result = Image.new("RGBA", (width, height), (0, 0, 0, 0))

# Paste images onto the base
result.paste(image1, (0, 0))
result.paste(image2, (0, 0), image2)
result.paste(image3, (0, 0), image3)
result.paste(image4, (0, 0), image4)
result.paste(image5, (0, 0), image5)
result.save("output_image.png")
