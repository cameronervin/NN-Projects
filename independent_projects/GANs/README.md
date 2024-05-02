# Generative Adversarial Networks
 
## About this Project

The goal of this project was to research Generative Adversarial Networks (GANs) to get a better understandin of how they function and what their purpose is. After gaining some background knowledge on GANs, I wanted to implement vanilla GANs to generate images of dogs.
 
## Dataset & Dependencies

I used the Stanford Dog image data set to train the generator and discriminator for this project.

We use the following Python/JupyterNotebook libraries in our work: 
* TensorFlow and Keras to create our model architecture.
* Seaborn and Matplotlib for data visualization.
* Pillow for showing and loading images
* Other essential libraries include NumPy, Pandas, and TensorFlow.

 
## Technical Approach

To explore circuits and to begin visualizing CNN features and filters, we used TensorFlow's VGG19. Our additional steps in visualizing VGG19 are as follows:

1. Load the dog image dataset
2. Visualize several images from the original dataset using the `plot_images` function to compare our later generated images to 
3. Define and initialize a `Generator()` and `Discriminator()` function which will create the architecture of our generator and discriminator
4. Define and initialize the `GAN` class which is responsible for constructing and training the entire GAN model which also houses the following functions: `generator_loss(self, fake_output)`, `discriminator_loss(self, real_output, fake_output)`, `train_step(self, images)`, and `train(self, dataset, epochs)`.
5. Train the GAN model
6. Generate dog images using our trained generator
7. Visualize to compare to our original dog images
 
## Highlights

* GANs
 
## Conclusion

Althought the generated 'dog' images are not very dog-like. One can see the rough visualization of a dog in the dog images. Had I trained the model for more epochs, the images would only become more dog-like.






