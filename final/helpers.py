import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def images(image_paths):
    num_images = len(image_paths)
    num_rows = math.ceil(num_images / 2)

    # create a figure and a set of subplots
    fig, axs = plt.subplots(num_rows, 2, figsize=(10, num_rows * 5))  # adjust figsize as needed
    axs = axs.ravel()  # flatten the array to simplify indexing

    for i in range(num_rows * 2):
        if i < num_images:
            img = mpimg.imread(image_paths[i])
            axs[i].imshow(img)
        axs[i].axis('off')  # hide axes for all plots

    plt.tight_layout()
    plt.show()

def results(folder_path):
    img = mpimg.imread(folder_path+'/results.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

def curves(folder_path):
    image_paths = [folder_path+'/F1_curve.png',  folder_path+'/PR_curve.png', folder_path+'/P_curve.png', folder_path+'/R_curve.png']
    images(image_paths)

def conf_matrices(folder_path):
    img = mpimg.imread(folder_path+'/confusion_matrix.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

    img = mpimg.imread(folder_path+'/confusion_matrix_normalized.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

def labels(folder_path):
    image_paths = [folder_path+'/labels.jpg', folder_path+'/labels_correlogram.jpg']
    images(image_paths)

def train_batch_predictions(folder_path):
    img = mpimg.imread(folder_path+'/train_batch0.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

    img = mpimg.imread(folder_path+'/train_batch1.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

    img = mpimg.imread(folder_path+'/train_batch2.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

def val_batch_predictions(folder_path):
    img = mpimg.imread(folder_path+'/val_batch0_labels.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

    img = mpimg.imread(folder_path+'/val_batch1_labels.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

    img = mpimg.imread(folder_path+'/val_batch2_labels.png')
    plt.imshow(img)
    plt.axis('off') 
    plt.show()

def df(folder_path):
    return pd.read_csv(folder_path+'/results.csv')