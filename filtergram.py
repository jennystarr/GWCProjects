from filters import*

def obamicon(pic):
    pixel = list(pic.getdata())
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

    new_img = []

    for p in pixel:
        intensity = p[0] + p[1] + p[2]

    #colorpixels = list(pic.getdata())
    #list_length = len(colorpixels)

    if intensity < 182:
        new_img.append(darkBlue)
    elif intensity >= 182 and intensity < 364:
        new_img.append(red)
    elif intensity >= 364 and intensity < 546:
        new_img.append(lightBlue)
    elif intensity >= 546:
        new_img.append(yellow)

    new_image = Image.new("RGB", (1000,669), p)
    new_image.putdata(new_img)
    pic = load_img("Cherry1.jpg")
    show_img(pic)
    save_img(pic, "Cherry2.jpg")
    return new_image
#load_img("Cherry1.jpg")
#show_img(pic)
#obamicon(pic)
#save_img(pic, "Cherry2.jpg")
#save_img(pic, "myflower.jpg")


#pic = load_img("flower.jpg")
#show_img(pic)
