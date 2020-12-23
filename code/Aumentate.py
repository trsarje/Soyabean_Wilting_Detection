import numpy as np
import tensorflow as tf


def augment(image_arr, d):
    # image_arr: array of the class to augment
    # d: number of images to augment
    aug_list = np.ndarray(image_arr.shape[1:])
    aug_list = np.expand_dims(aug_list, axis=0)

    for i in range(d // 4):
        image = image_arr[i]                              # Read the image
        flipped = tf.image.flip_left_right(image)         # Flip the image across vertical axis
        saturated = tf.image.adjust_saturation(image, 2)  # Add color saturation to the image
        bright = tf.image.adjust_brightness(image, 0.1)   # Add brightness to the image
        rotated = tf.image.rot90(image)                   # Rotate the image 90 dec right

        aug_list = np.vstack((aug_list, np.expand_dims(flipped, axis=0)))
        aug_list = np.vstack((aug_list, np.expand_dims(saturated, axis=0)))
        aug_list = np.vstack((aug_list, np.expand_dims(bright, axis=0)))
        aug_list = np.vstack((aug_list, np.expand_dims(rotated, axis=0)))

    return aug_list