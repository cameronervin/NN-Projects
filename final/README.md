# CS 8321 Final Paper
Note: For line by line explanation of code and implementation, see documentation within Jupyter Notebook and Python files
## Installation and Running
1. Install anaconda
2. Clone the repository and install the required packages:
```python
git clone [https://github.com/cameronervin/NN-Projects/tree/main/final]
cd [NN-Projects/tree/main/final]
pip install -r requirements.txt
```
3. Download the Kaggle dataset at the following url:
   `https://www.kaggle.com/datasets/lexset/synthetic-asl-alphabet`
4. Using `Roboflow.com` hand label each image with the label being the letter (tutorials are available online). Additionally, consider sampling just the `test` split of the data to avoid having to hand label a very large number of images.
5. Augment the data with the following augmentations:
   - resize	   =      640x640
   - flip	   =      horizontal
   - crop	   =      -5\% to +20\%
   - hue	      =      +/- 15 degrees
   - exposure	=      +/- 10\%
   - blur	   =      2.5px
6. Export the data in YOLOv9 format
   
Note: Run `lab4_mediapipe_XGB.ipynb` before running `lab4_YOLOv9.ipynb`. This creates the other dataset necessary to create the second YOLOv9 model.

## Features and Usage
### `lab4_mediapipe_XGB.ipynb`
#### `process_images_with_mediapipe()`
   - Creates a new dataset based on the original hand image dataset with a 2D overlay of the MediaPipe Hand landmarks on top of each image. This dataset maintains the original splits from the original dataset.
      - You must copy the `data.yaml` file over to this new dataset.
      - Additionally, you must create an image subfolder for the images in each split and copy the labels over from the original dataset.
#### `sort_and_move_images()`
   - Creates a new sorted dataset based on the original hand image dataset by sorting each image based on the label from its corresponding `label.txt` file into a subfolder of the same label.
      - Each image is copied over to a new dataset that maintains the same split.
      - For example, all As in the train dataset will be copied into the root/train/A folder, and so on.
      - This will make creating the mediapipe hand output csv files easier since the subfolder label will be used as the label column of the csv file.
#### `create_hand_landmarks_dataset()`
   - Creates csv files for each split which include every x,y,z for all 21 hand landmarks
        - A separate csv file is created for each split.
#### XGBClassifier
   - After the `create_hand_landmarks_dataset()` function has been successfully executed, the XGBClassifier code will initialize and run an XGBoost classifier to predict the label for each image based on the hand landmark data csv.
        - This can be performed on both normalized and unnormalized data to create different classifiers.

### `lab4_YOLOv9.ipynb`
- Creates YOLOv9 models based on the base dataset and the new dataset with the mediapipe hand 2D overlay
     - Creates models from scratch using `yolov9c.yaml` to initialize each model
     - When training model, sets `data=.../dataset/data.yaml`
     - Trains until convergence
     - Calculates F1 score for each epoch based on `results.csv` Ultralytics creates for each model training/validation
          - Utilizes precision and recall columns to find F1 score
- Follow documentation in notebook for greater detail on steps taken within notebook
- Helper functions display results in an aesthetic manner

###  `helpers.py`
- Helper functions to visualize results from YOLOv9 models in `lab4_YOLOv9.ipynb`
#### `images(image_paths)`
- Displays a list of images specified by their paths. Images are arranged in a grid layout.
#### `results(folder_path)`
- Displays a specific result image from a given folder path.
#### `curves(folder_path)`
- Displays performance curves (like F1, PR, P, and R curves) from specified images within a folder.
#### `conf_matrices(folder_path)`
Shows confusion matrices, both regular and normalized, from a specified folder.
#### `labels(folder_path)` 
- Displays images of labels and their correlogram from a folder.
#### `train_batch_predictions(folder_path)`
- Shows training batch predictions by displaying images from a folder.
#### `val_batch_predictions(folder_path)` 
- Displays validation batch predictions, highlighting labels on images.
#### `df(folder_path)` 
- Reads a CSV file into a DataFrame from the specified folder.
