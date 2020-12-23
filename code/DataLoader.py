import numpy as np
import pandas as pd
import cv2
import os
import glob


def load_data(x):  # flag 1 for training data, 0 for testing data
    drct = r"../github/data/TrainData/"             # Train data directory

    imgL = []
    if x:
        df = pd.read_csv(
            '../github/data/TrainAnnotations.csv')  # Train annotation CSV
        for i in range(len(df.annotation)):
            name = str(df.file_name[i])             # read the file name from the annotation csv
            path = drct + name
            img = cv2.imread(path)                  # Read the corresponding image
            img = cv2.resize(img, (224, 224))       # Resize all images to (224, 224)
            imgL.append(img)

        data = np.array(imgL)                       # Convert list of images to numpy array
        clas = df.annotation.values
        return data, clas                           # Return images and class labels

    else:
        img_dir = "../github/data/TestData"         # Enter Directory of test images
        data_path = os.path.join(img_dir, '*g')
        files = glob.glob(data_path)
        data = []
        for f1 in files:
            img = cv2.imread(f1)                    # Read the image in the test directory
            img = cv2.resize(img, (224, 224))       # Resize the image
            data.append(img)
        data = np.array(data)
        return data                                 # Return the array of test images