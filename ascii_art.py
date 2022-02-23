from PIL import Image


#loading image and printing its dimensions
im = Image.open("melons.jpg")
pixel_size = [str(i) for i in im.size]
print("image successfully loaded !")
print("Image size : " + " x ".join(pixel_size))

new_image = im.resize((400,200))
new_image.save('melons-resize.jpg')

#converting pixels into an array of tuples
#temp = np.asarray(im)

#for i in temp:
#    pixel_array = [[j[0],j[1],j[2]] for j in i] 


#creating a list of brightness of the pixel


#mapping the brightness to ascii characters
brightness_test = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

def printAscii():
    pixel_array = new_image.getdata()
    brightness_list = [sum(i) // 3 for i in pixel_array]
    final_image = [brightness_test[int(i // 3.93)]  for i in brightness_list]
    print("".join(final_image))
printAscii()