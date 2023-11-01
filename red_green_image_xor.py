from PIL import Image

flag = Image.open('encoded.png')

lsb = []

b = ""

pixels = list(flag.getdata())

for c,p in enumerate(pixels):

    b+=bin(p[1]^p[0])[-1]
    
    if len(b) == 8:
        lsb.append(int(b, 2))
        b=""
    if c == 240:
        break
        
for char in (lsb):
    print(chr(char), end="")
# XOR red with green and append the least significant bit to b
# If b is 8 bits, empty it's value in 'lsb' list
# For each bytes in lsb[], print its ascii value