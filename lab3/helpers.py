import os
import json
import shutil
import seaborn as sns
import numpy as np
from tabulate import tabulate
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image

def rename(dataset_directory, json_file_path):
    with open(json_file_path, 'r') as json_file:
        class_index = json.load(json_file)

    # Function to move contents from source to destination
    def move_contents(src, dst):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                move_contents(s, d)  # Recursive call for directories
            else:
                if not os.path.exists(dst):
                    os.makedirs(dst)
                shutil.move(s, d)

    # Iterate over the class index and rename each folder
    for _, (imagenet_id, class_label) in class_index.items():
        original_folder_path = os.path.join(dataset_directory, imagenet_id)
        new_folder_path = os.path.join(dataset_directory, class_label)

        # Check if the original folder exists
        if os.path.exists(original_folder_path):
            if os.path.exists(new_folder_path):
                # Move contents if the target directory already exists
                move_contents(original_folder_path, new_folder_path)
                os.rmdir(original_folder_path)  # Remove the now-empty original directory
            else:
                # Rename the folder to its new name (class label)
                os.rename(original_folder_path, new_folder_path)
        else:
            continue

def display_top_images(root_path, results):
    for value in results.values():
        folder_path = os.path.join(root_path, value[0])

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        # Start a new figure for each class with a row of subplots
        plt.figure(figsize=(15, 3))  # Adjust the figure size as needed

        # Display the first 5 images, or fewer if not available
        for i, image_file in enumerate(image_files[:5]):
            image_path = os.path.join(folder_path, image_file)
            image = plt.imread(image_path)

            # Create a subplot for each image in a row
            plt.subplot(1, 5, i+1)  # Arguments are (rows, columns, index)
            plt.imshow(image)
            plt.axis('off')  # Hide the axis
            plt.title(f"{value[0]} Image {i+1}")  # Optionally customize title

        plt.show()  # Show all the plots for the current class together

def display_top_images(root_path, results):
    # Determine the total number of subplots needed
    total_rows = len(results)
    images_per_row = 4  # Assuming you want to display up to 5 images per category

    # Start a new figure outside the loop
    fig, axs = plt.subplots(total_rows, images_per_row, figsize=(15, 3 * total_rows))
    
    for row_index, row in enumerate(results):
        name = row[0]
        folder_path = os.path.join(root_path, name)

        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

        for i in range(images_per_row):
            if i < len(image_files):  # Display the image if it exists
                image_path = os.path.join(folder_path, image_files[i])
                image = plt.imread(image_path)

                if total_rows > 1:
                    ax = axs[row_index, i]
                else:
                    ax = axs[i]
                
                ax.imshow(image)
                ax.set_title(f"{name} Image {i+1}")  # Optionally customize title
            else:  # Make the subplot invisible if no image is available
                if total_rows > 1:
                    axs[row_index, i].axis('off')
                    axs[row_index, i].set_xticks([])
                    axs[row_index, i].set_yticks([])
                    for spine in axs[row_index, i].spines.values():  # Optionally, make the borders invisible
                        spine.set_visible(False)
                else:
                    axs[i].axis('off')
                    axs[i].set_xticks([])
                    axs[i].set_yticks([])
                    for spine in axs[i].spines.values():
                        spine.set_visible(False)

            ax.axis('off')  # Hide the axis for all subplots

    plt.tight_layout()
    plt.show()

def print_table(data):
    # Define the table headers
    headers = ['Class', 'Avg Activation']
    # Print the table
    print(tabulate(data, headers=headers, tablefmt='grid'))

def display_images(root_path, image_list):
    # Set up the figure size
    plt.figure(figsize=(20, 6))  # Adjusted for 2 rows
    
    # Ensure that we have 10 subplots (2 rows x 5 columns)
    for i, (folder, image_name, array) in enumerate(image_list):  # Limit to the first 10 images
        # Construct the full path to the image file
        image_path = os.path.join(root_path, folder, image_name)
        
        # Load the image using PIL (Pillow)
        image = Image.open(image_path)
        
        # Calculate row and column index
        row = i // 5  # Integer division to get row index
        col = i % 5   # Remainder to get column index
        
        # Create a subplot for each image in a 2x5 grid
        plt.subplot(2, 5, i + 1)
        plt.imshow(image)
        plt.axis('off')  # Remove the axis
        plt.title(f"{image_name}")  # Set the title of the subplot to the image name
    
    plt.tight_layout()
    plt.show()

def visualize_matrix_seaborn(channel, matrix, ax):
    # normalize matrix values between -1 and 1 for color intensity mapping
    max_val = np.max(np.abs(matrix))
    norm_matrix = matrix / max_val if max_val != 0 else matrix
    
    # custom color palette
    cmap = sns.diverging_palette(240, 0, as_cmap=True)
    
    # plotting with seaborn heatmap on the provided axis
    sns.heatmap(norm_matrix, cmap=cmap, center=0, annot=True, fmt=".2f", ax=ax)
    ax.set_title(f'Visualization of Filter {channel}')
