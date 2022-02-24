from PIL import Image
from numpy import asarray, reshape

image = Image.open("kingfisher.jpg")

#check the width to ensure it is no more than 200
## 200 lines are the limit of what the commandline can print without distorting the image
if image.width > 200:
    new_image = image.resize((200, image.height)) ## resize the image to 200 px in width
    new_image.save(f"{image}_resized.jpg") 

pixel_size = [str(i) for i in new_image.size]
print("new_image successfully loaded")
print(f" new_image size : " + " X ".join(pixel_size))

# the ascii string used to rank pixels from dimmest to brightest
brightness_test = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

pixels = new_image.getdata() #get the pixels of the image in form of a single dimensional array
#pixels are in lists of three, i.e R G B. 
# average the three colors to get the brightness of the pixel 
brighness_level = [sum(i) // 3 for i in pixels]

#substitute the average of the pixels with their equivalent from the ascii string
#print the character substituted twice to avoid getting a squashed image
final_new_image = [str(brightness_test[int(i // 3.93)]) * 2   for i in brighness_level]

#convert the one dimensional list to 2-d to ensure the columns are 200. 
# not to exceed the sweet spot of the command line printing
result = reshape(asarray(final_new_image), (-1, 200)).tolist()

#print the image
##NB: USE CTRL+- RO MINIMIZE YOUR COMMANDLINE FONT TILL EACH ROW SPANS ONE LINE
for i in range(len(result)):
    for j in range(len(result[1])):
        print(result[i][j], end="")
    print()
    