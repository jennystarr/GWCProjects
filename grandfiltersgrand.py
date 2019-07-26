from grandfilters import *

def main():
    #change "file_name_here with your image link"
    myImg = load_img("Cherry2.jpg")
    #pick one of the filters here
    newImg = jenn_bluepic(myImg)

    newImg.show()

main()
