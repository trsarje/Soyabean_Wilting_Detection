# Computer Vision Soyabean Wilting Detection

## Motivation:
A growing population and rapid environmental changes mean that crop scientists will play an increasingly important role in ensuring that people and animals are well-fed and healthy. Weather and water stress have a great impact on the drought intolerant soybean varieties, which lead to physiological changes in the plants. This project is aimed to identify the water stress level of the Soybean crop. A mechanized approach integrated with UAV will prove to be an efficient and time effective replacement to the manual surveillance. 

## Project Overview:
* Created a tool to classify given Soyabean crop images in different classes according to wilting of the plant. 
* Pre-processed, augmented around 400 images using OpenCV, TensorFlow. 
* Engineered a transfer learning model using VGG16 as base model.

![Model architecture](https://github.com/trsarje/Soyabean_Wilting_Detection/blob/master/Images/Modelpng.png)

## Data: 
* The data consiste of ~1600 RGB images of Soyabean crop distributed across five classes (0-4).
* Resized images to 224 X 224 X 3. 
* Splitted ~200 images in validation and ~1400 for training. 
* Augmented train images by flipping, rotating, and by adjusting saturation and brightness. 

![Sample Images](https://github.com/trsarje/Soyabean_Wilting_Detection/blob/master/Images/ClassImg.png)

## Model:
* A transfer learning model is used with VGG16 as base. VGG16 is initialised with "Imagenet" weights.
* Following base model custom layers are added. 
* Trained model weights can be downloaded using the [link](https://drive.google.com/file/d/1-4z9Op1pfnEo-ZB90bLk-sYVEIL-43QK/view?usp=sharing).

## Evaluation:
* The model is trained to achieve ~80% validation accuracy. 
* Test code is available to check the model prediction on new test data. 
![Training graph](https://github.com/trsarje/Soyabean_Wilting_Detection/blob/master/Images/acc.png)


