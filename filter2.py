from filters import*

def bluepic(flowerz):
    pixel = list(pic.getdata())
    navy = (0,0,128)
    royalblue = (65,105,225)
    bluex = (0, 0, 225)
    lightskyblue = (112,150,158)

    colorpixels = list(pic.getdata())
    list_length = len(colorpixels)

    new_look = []

    for p in pixel:
        intensity = p[0] + p[1] + p[2]


        if intensity < 190:
            new_look.append(navy)
        elif intensity >= 190 and intensity < 300:
            new_look.append(royalblue)
        elif intensity >= 300 and intensity < 500:
            new_look.append(bluex)
        elif intensity >= 500:
            new_look.append(lightskyblue)

    filternew = pic.putdata(colorpixels)
    def save_img(pic, filternew):
        pic.save(filternew)
    save_img (pic, "Cherry2.jpg")
    newpic = load_img("Cherry2.jpg")
    show_img(newpic)

pic = load_img("Cherry1.jpg")
show_img(pic)
bluepic(pic)
