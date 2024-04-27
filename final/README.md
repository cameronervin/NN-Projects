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
7. You are now ready to use the cloned repository
   
## Implementation Manual
### `lab4_YOLOv9.ipynb`
- creates 

### `lab4_mediapipe_XGB.ipynb`


###  `helpers.py`

