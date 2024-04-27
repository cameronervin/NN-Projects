# CS 8321 Final Paper
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
   
Note: Run `lab4_mediapipe_XGB.ipynb` before running `lab4_YOLOv9.ipynb`. This creates the other dataset necessary to create both YOLOv9 models.

## Features and Usage
### `lab4_mediapipe_XGB.ipynb`
- Creates a new dataset based on the original hand image dataset with a 2D overlay of the MediaPipe Hand landmarks on top of each image. This dataset maintains the original splits from the original dataset.
   - You must copy the `data.yaml` file over to this new dataset. Additionally, you must create an image subfolder for the images in each split and copy the labels over from the original dataset.
- Creates a 

### `lab4_YOLOv9.ipynb`
- creates YOLOv9 models based on the base 


###  `helpers.py`

