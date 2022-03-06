import numpy as np
from PIL import Image

from keys.KeyBound import KeyBound


def save_image(image_data, filename: str):
  image = Image.fromarray(image_data)
  image.save(filename)

def get_image_from_file(filename: str):
  return Image.open(filename)

def get_image_from_file_to_array(filename: str):
  return np.array(get_image_from_file(filename))

def get_image_in_range(image, key_bound: KeyBound):
  pixels_rows = []

  for pixel_line in image:
    rows_to_append = pixel_line[key_bound.start:key_bound.end]
    pixels_rows.append(rows_to_append)

  return np.array(pixels_rows)
