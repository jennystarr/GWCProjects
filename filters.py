# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
filename = Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    pic = Image.open(filename)
    return pic
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(filename):
    filename.show()
# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(filename, flower):
    filename.save(flower)


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
pic = load_img("Cherry1.jpg")
show_img(pic)
save_img(pic, "Cherry1.jpg")
