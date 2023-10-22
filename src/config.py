import os
import json

# Open json file
with open(os.path.join(os.path.dirname(__file__), 'signs.json')) as f:
    SIGNS = json.load(f)

# Define data path to be outside of the src folder
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

# Define number of frames per video
NO_FRAMES = 30

# Create folders for each sign
for sign in SIGNS.keys():
    if not os.path.exists(os.path.join(DATA_PATH, sign)):
        os.makedirs(os.path.join(DATA_PATH, sign))