import math
from PIL import Image

def reflect(image, background_color='#ffffff', reflection_size=0.5):
    flipped = image.transpose(Image.FLIP_TOP_BOTTOM)
    reflection_height = int(reflection_size * image.size[1])
    mask = Image.new('L', (1, image.size[1]))
    for y in xrange(reflection_height):
        # S-curve fade
        fade_amount = 1 / ( 1 + pow(math.e, -((float(reflection_height - y) / reflection_height) * 7 - 4)))
        mask.putpixel((0, y), fade_amount * 255)
    resized_mask = mask.resize(image.size)
    background = Image.new('RGB', image.size, background_color)
    reflection = Image.composite(flipped, background, resized_mask)
    cropped_reflection = reflection.crop((0, 0, image.size[0], reflection_height))
    result = Image.new('RGB', (image.size[0], image.size[1] + reflection_height), background_color)
    result.paste(image, (0, 0))
    result.paste(cropped_reflection, (0, image.size[1]))
    return result

if __name__ == "__main__":
    image = Image.open("example.jpg")
    new_image = reflect(image, reflection_size=0.2)
    new_image.show()