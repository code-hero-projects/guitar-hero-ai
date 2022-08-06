from PIL import Image
import numpy as np


def main(filenames):
  for filename in filenames:
    image = np.array(Image.open(filename))
    min_green, min_red, min_blue = 255, 255, 255
    max_green, max_red, max_blue = 0, 0, 0

    for pixels2d in image:
      for pixel in pixels2d:
        red = pixel[0]
        green = pixel[1]
        blue = pixel[2]

        if (red < min_red):
          min_red = red
        elif (red > max_red):
          max_red = red
        
        if (green < min_green):
          min_green = green
        elif (green > max_green):
          max_green = green

        if (blue < min_blue):
          min_blue = blue
        elif (blue > max_blue):
          max_blue = blue
    
    print(f'stats for {filename}')
    print(f'MIN - red:{min_red}, green: {min_green}, blue: {min_blue}')
    print(f'MAX - red:{max_red}, green: {max_green}, blue: {max_blue}')
    print('')

main(['green.png', 'red.png', 'yellow.png', 'blue.png', 'orange.png'])
