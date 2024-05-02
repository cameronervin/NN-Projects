# EDA and Statistical Modeling
 
## About this Project

The goal of this project was to experiment using some advanced visualization and Exploratory Data Analysis techniques using Python Pandas. Understanding a dataset as well as the statistics behind data is a crucial part of data science and machine learning, so I wanted to take a little bit of a deeper dive into EDA and visualizations.
 
## Dataset & Dependencies

I used the Starship Titanic dataset found on Kaggle for this project.

I use the following Python/JupyterNotebook libraries in my work: 
* Seaborn and Matplotlib for data visualization.
* LazyPredict and lightlgmb for creating the classification models
* Other essential libraries include NumPy, Pandas, SkLearn.
* `eda_helpers.py`

 
## Technical Approach

1. Load the dataset in
2. Use `head()`, `describe()` and other methods to get an understanding of the data at a high level
3. Get an overview of the dataset statistically
4. Visualize the column and row wise null values
5. Visualize the distributions of the categorical and continuous variables
6. Visualize the correlation of different features using a correlation matrix
7. Preprocess the data with imputing missing values and encoding the categorical features
8. Use LazyPredict and LightLGBM to create classifcation models
9. Take the top 15 performing models and visualize their performance
 
## Highlights

* EDA
* Data visualization
 
## Conclusion

I was able to create some very visually appealing visualizations using the techniques I discovered for this project. LazyPredict and LighLGBM are also useful tools for creating many different classification models to find the best performing classification.

Several of the visualizations did not load into the JupyterNotebook. All of the visualizations can be foud in the `visualizations` subfolder.
