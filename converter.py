'''
LDEIF (Low Definition Experimental Image Format)
as the name suggests is an experimental image
format created using Python. It's about 30%
the storage efficiency of PNG, which I think is
acceptable considering this is only the first
version.
'''

def process(filename, output):
    dat = bytes()

    from PIL import Image

    img = Image.open(filename)
    img = img.convert("RGB")

    if img.width > 255: # The image cannot be over 255 pixels wide.
        img = img.resize([255, 255])

    # Includes how many bytes there will be that specify the width of the image
    dat += bytes([img.width])

    # Adds a byte for each r, g and b value per pixel
    for y in range(img.height):
        for x in range(img.width):
            r, g, b = img.getpixel((x, y))
            dat += bytes([r])
            dat += bytes([g])
            dat += bytes([b])
    
    img.close()


    with open(output, "wb") as f:
        f.write(dat)

process("sample.png", "sample.ldeif")