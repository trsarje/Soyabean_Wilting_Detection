# Computer Vision Soyabean Wilting Detection

## Motivation:
A growing population and rapid environmental changes mean that crop scientists will play an increasingly important role in ensuring that people and animals are well-fed and healthy. Weather and water stress have a great impact on the drought intolerant soybean varieties, which lead to physiological changes in the plants. This project is aimed to identify the water stress level of the Soybean crop. A mechanized approach integrated with UAV will prove to be an efficient and time effective replacement to the manual surveillance. 

## Project Overview:
* Created a tool to classify given Soyabean crop images in different classes according to wilting of the plant. 
* Pre-processed, augmented around 800 images using OpenCV, TensorFlow. 
* Engineered a transfer learning model using VGG16 as base model.

## Data: 
* The data consiste of ~800 RGB images of Soyabean crop distributed across five classes (0-4).
* Images are resized to 224 X 224 X 3. 
* Images are augmented by flipping, rotating, and by adjusting saturation and brightness. 
![Sample Images](https://github.com/trsarje/Soyabean_Wilting_Detection/blob/master/Images/ClassImg.png)
[Download Model Weights](https://drive.google.com/file/d/1-4z9Op1pfnEo-ZB90bLk-sYVEIL-43QK/view?usp=sharing)
