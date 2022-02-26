from PIL import Image
from numpy import asarray, reshape
from colorama import Fore, Back, Style


ascii_key = '`^",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


def image_array(image):
    """
    resize the image to a width of 200 pixels.
    convert the image to a one-dimensional array of pixels

    Args:
        image: This is the image passed to the function

    Returns:
        pixel_array: Array of pixels gotten from using the .getdata() method
    """
    if image.width > 200:
        image = image.resize(
            (200, image.height)
        )  
    else:
        image = image
    pixel_array = image.getdata()
    return pixel_array


def get_brightness(pixel_array, algorithm="average"):
    """
    calculate the  brightness of each RGB array by using different formulas

    Args:
        pixel_array: array of pixels returned after converting the image to an array
        algorithm: Formula used to calculate the brighness of a pixel

    Returns:
        brightness_array: array containing averaged pixels
    """
    if algorithm == "average":
        brightness_array = [(max(i) + min(i)) // 2 for i in pixel_array]
    elif algorithm == "luminosity":
        brightness_array = [sum(i) // 3 for i in pixel_array]
    elif algorithm == "lightness":
        brightness_array = [
            (0.21 * i[0] + 0.72 * i[1] + 0.07 * i[2]) for i in pixel_array
        ]
    return brightness_array


def pixels_to_ascii(brightness_array):
    """
    convert the array of pixels to an array of ascii characters
    convert the one-dimensional array to a two-dimensional array using reshape method of numpy

    Args:
        brightness_array: array containing averaged pixels

    Returns:
        result: two-dimensional array of ascii characters
    """
    final_image = [str(ascii_key[int(i // 3.93)]) * 2 for i in brightness_array]
    result = reshape(asarray(final_image), (-1, 200)).tolist()
    return result


def print_ascii(result):
    """
    print the ascii characters on the command line
    
    Args:
        result: two-dimensional array of ascii characters
    """
    for i in range(len(result)):
        for j in range(len(result[1])):
            print(Fore.GREEN + result[i][j], end="")
        print()


image = Image.open("images/re_zebra.jpg")
image_matrix = image_array(image)
brightness = get_brightness(image_matrix, "luminosity")
ascii_array = pixels_to_ascii(brightness)
print_ascii(ascii_array)



##NB: USE CTRL+- RO MINIMIZE YOUR COMMANDLINE FONT TILL EACH ROW SPANS ONE LINE
