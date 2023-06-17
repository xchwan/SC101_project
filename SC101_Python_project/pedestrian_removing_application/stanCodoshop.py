"""
File: stanCodoshop.py
Name: 萬昭宏
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage
import statistics as stat


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    return ((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)**0.5


def remove_outlier(data, threshold=1):
    mean = stat.mean(data)
    std = stat.stdev(data)
    if std:
        z_list = list(map(lambda x: ((x-mean)/std, x), data))
    else:
        z_list = list(map(lambda x: (0, x), data))
    pop_data = []
    for z in z_list:
        if abs(z[0]) < threshold:
            pop_data.append(z[1])
    return pop_data


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    red_pixels = []
    green_pixels = []
    blue_pixels = []

    for pixel in pixels:
        red_pixels.append(pixel.red)
        green_pixels.append(pixel.green)
        blue_pixels.append(pixel.blue)

    red_pixels = remove_outlier(red_pixels)
    green_pixels = remove_outlier(green_pixels)
    blue_pixels = remove_outlier(blue_pixels)

    red_avg = sum(red_pixels)//len(red_pixels)
    green_avg = sum(green_pixels)//len(green_pixels)
    blue_avg = sum(blue_pixels)//len(blue_pixels)

    return [red_avg, green_avg, blue_avg]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_pixel = get_average(pixels)
    # short_pixel_path = float('inf')
    # short_pixel = None
    pixel_list = []
    for pixel in pixels:
        pixel_distance = get_pixel_dist(pixel, avg_pixel[0], avg_pixel[1], avg_pixel[2])
        pixel_list.append((pixel_distance, pixel))
    short_pixel = min(pixel_list, key=lambda x: x[0])[1]
    # for pixel in pixels:
    #     pixel_distance = get_pixel_dist(pixel, avg_pixel[0], avg_pixel[1], avg_pixel[2])
    #     if pixel_distance <= short_pixel_path:
    #         short_pixel = pixel
    #         short_pixel_path = pixel_distance
    return short_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            pixel = result.get_pixel(x, y)
            image_pixel = []
            for image in images:
                image_pixel.append(image.get_pixel(x, y))
            best_pixel = get_best_pixel(image_pixel)
            pixel.red = best_pixel.red
            pixel.green = best_pixel.green
            pixel.blue = best_pixel.blue
    # ----- YOUR CODE ENDS HERE ----- #
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    """
    main function, input image file array return no people photo.
    """
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
