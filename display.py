from PIL import Image

def show(fp):
    with open(fp, "rb") as f:
        arr = list(f.read())
        imwidth = arr[0]
        imheight = round(((len(arr)/3)-1)/imwidth)

        print(imheight, imwidth)

        img = Image.new("RGB", (imwidth, imheight))

        col = 0
        row = 0
        pixval = []
        for i in range(len(arr)):
            if not (i==0):
                pixval.append(arr[i])

                if len(pixval)>2:
                    img.putpixel((col, row), (pixval[0], pixval[1], pixval[2]))
                    pixval = []

                    col += 1
                    if col == imwidth:
                        col = 0
                        row += 1
            

            
        
        img.show()

show("sample.ldeif")