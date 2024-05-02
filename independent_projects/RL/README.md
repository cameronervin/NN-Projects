# Reinforcement Learning - Cross Entropy to Deep Q Learning
 
## About this Project

The goal of this project was to research different methods of Reinforcement Learning (RL) to gain a better understanding of the different approaches. Lastly, to illustrate this greater understanding, I will implement Deep Q Learning.
 
## Dataset & Dependencies

I use the following Python/JupyterNotebook libraries in my work: 
* PyTorch to create our model architecture.
* Seaborn and Matplotlib for data visualization.
* OpenAI Gymnasium
* Other essential libraries include NumPy and Pandas.

 
## Technical Approach

1. Create the `CartPole-v0` environment and simulate an agent acting randomly within the game
2. Define the `QNetwork(nn.Module)` class which houses the `FullyConnectedModel(nn.Module)` class as well as the following functions: `load_model(self, model_file)` and `load_model_weights(self, weight_file)`
3. Define the `ReplayMemory` class
4. Create our `DQN_Agent` class which will be responsible for training and testing the Deep Q Network Agent
5. Train and evaluate the DQN and illustrate the score of the agent during evaluation

## Highlights

* Deep Q Learning
* PyTorch
* OpenAI Gymnasium
 
## Conclusion

Implementing Deep Q Learning for cart pole is rather straight forward since the game his limited complexity. However, I think it is a great illustration of the classes and functionality required for Deep Q Learning at a larger scale.

Also, the videos of the random and trained agents did not render into the Jupyter Notebook. To see these videos please check out the `results` subfolder.
