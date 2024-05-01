# Transfer Learning and Transformers
 
## About this Project

The goal of this project is to utilize a Vision Transformer (ViT) for the purpose of transfer learning with image classification. The classification task was to correctly classify an image of a card to both its suit and rank in a combined classification. This means that there are 52 (excluding Joker) possible classfication classes. Additionally, to understand the performance of our ViT model, we compared the ViT model to a basic model with a CNN architecture.
 
## Dataset & Dependencies

The dataset we used to train and evaluate our model is a Kaggle dataset of images of playing cards of all suits.

We use the following Python/JupyterNotebook libraries in our work: 
* TensorFlow and Keras to create our model architecture.
* Hugging Face ViT for our ViT model.
* Scikit-learn for model evaluation and data processing.
* Seaborn and Matplotlib for data visualization.
* Other essential libraries include NumPy, Pandas, and TensorFlow.

 
## Technical Approach

To create our ViT and base CNN models, we performed the following:

CNN Model -
1. Load our dataset in and split the dataset into train, test, valid
2. Create our CNN model architecture
3. Train model and store per epoch accuracy in a CSV file for later evaluation

ViT Model - 
1. Same as previous step 1
2. Load in our ViT model from Hugging Face with the `google/vit-base-patch32-224-in21k` model
3. Set all attention heads and layers of the ViT to false in order to set the ViT model as our backbone
4. Run the dataset through the ViT model using our `extract_features(dataset, model, processor)` function and extract the features from the bottle neck created
5. Define and create a sequential model to act as the top model for our transfer learning process
6. Train the top model using the extracte features and store per epoch accuracy in a CSV file for later evaluation
7. Perform fine tuning of the model by setting the last layer of the ViT model to trainable
8. Repeat steps 4 and 6 again

Finally, we compared the performance of our base CNN model to both our non-fine-tuned ViT transfer learning model and our fine tuned ViT transfer learning model using the csv files created of our model performances.
 
## Highlights

* ViT
* Transformers
* Transfer Learning
* Convolutional Neural Network
 
## Conclusion

Transferring the ViT transformer then tuning the model produced superior accuracy faster than training a CNN model from scratch on this card sorting task.




