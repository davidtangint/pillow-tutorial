from PIL import Image

if __name__ == "__main__":
    with Image.open("./images/image_1.jpg") as im:
        print(im.size)
        im.save("./saved-images/blabla_1.jpg")
