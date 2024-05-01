# CNN Visualization - Circuits
 
## About this Project

The goal of this project is to explore the concept of 'circuits' within convolutional neural networks as a means to extablish a level of interpretability of the output/inner-workings of CNN models.
 
## Dataset & Dependencies

We used a mini ImageNet dataset from Kaggle to evaluate our CNN model and to help visualize what the model was doing.

We use the following Python/JupyterNotebook libraries in our work: 
* TensorFlow and Keras to create our model architecture.
* Scikit-learn for model evaluation and data processing.
* Seaborn and Matplotlib for data visualization.
* Other essential libraries include NumPy, Pandas, and TensorFlow.

 
## Technical Approach

To explore circuits and to begin visualizing CNN features and filters, we used TensorFlow's VGG19. Our additional steps in visualizing VGG19 are as follows:

1. Load VGG19 in from TensorFlow
2. Ensure VGG19 is working properly using our `show_vgg_working(input_image)` function
3. Select a multi-channel filter from a layer to visualize
4. Optimally excite this feature with gradient ascent to see what kind of image the feature detects
5. Send various images through the feature using our mini ImageNet dataset and see which of the images most excites the feature
6. Analyze our optimally excited image as well as the optimally exciting classes to form a hypothesis about what our chosen feature is doing
7. To understand the entire circuit, extract the input activation to our feature and choose the 10 with the strongest weights (positive or negative)
8. Visualize the optimally exciting image for each of these input filters to understand how they might influence our chosen feature
9. Define properties of our circuit and relate back to our original hypothesis
 
## Highlights

* Circuits
* Interpretability
* VGG19
* OpenAI Mircroscope
 
## Conclusion

Hypothesis:

Therefore, after examining the image that optimally excites our feature both through Microscope and our own optimization as well as finding which classes and individual images most activate our feature, we believe that our feature especially picks up on circular objects/ components in images.

Analysis:

Our visualizations and further analysis support our hypothesis. We have determined that our circuit is comprised of different curve detectors that create a pure, pose invariant circular object detecting feature with feature 8. When examining our most excitatory filters, we found that there are different families of filters that detect curves and circular centers, and ovals that could be circles. Additionally, our most inhibitory filters excluded curves with oval like features which were not actually circular. In conclusion, our visualizations support our hypothesis that our feature detects circular components in images.





