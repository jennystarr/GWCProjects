from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("cherry2.jpg")
    #pick one of the filters here
    newImg = jenn_bluepic(myImg)

    newImg.show()

main()
