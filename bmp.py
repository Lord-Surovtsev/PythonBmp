import Image

if __name__ == "__main__":
    width = input("width: ")
    height = input("height: ")

    img = Image.new('RGB', (width, height), "black")
    pixels = img.load() # create the pixels map

    red = input("red: ")
    green = input("green: ")
    blue = input("blue: ")

    for j in range(height):
        for i in range(width):
            pixels[i, j] = (red, green, blue)

    show = raw_input("show (y/): ")
    if 'y' == show[0] or 'Y' == show[0]:
        img.show()

    writeToFile = raw_input("write to file (y/): ")
    if 'y' == writeToFile[0] or 'Y' == writeToFile[0]:
        filename = raw_input("filename: ")
        img.save(filename)
