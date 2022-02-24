from PIL import Image
from numpy import asarray, reshape

image = Image.open("kingfisher.jpg")
if image.width > 200:
    new_image = image.resize((200, image.height))
    new_image.save(f"{image}_resized.jpg")

pixel_size = [str(i) for i in new_image.size]
print("new_image successfully loaded")
print(f" new_image size : " + " X ".join(pixel_size))
brightness_test = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

pixels = new_image.getdata()
brighness_level = [sum(i) // 3 for i in pixels]
final_new_image = [str(brightness_test[int(i // 3.93)]) * 2   for i in brighness_level]
print(len(brighness_level))

result = reshape(asarray(final_new_image), (-1, 200)).tolist()

for i in range(len(result)):
    for j in range(len(result[1])):
        print(result[i][j], end="")
    print()
    