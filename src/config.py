import os

# Define signs and their corresponding labels
SIGNS = {
    'hello': 0,
    'what\'s your name': 1,
    'how are you': 2,
    'i\'m fine': 3,
    'thank you': 4,
    'good bye': 5
}

# Define data path to be outside of the src folder
DATA_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data')

# Define number of frames per video
NO_FRAMES = 30

# Create folders for each sign
for sign in SIGNS.keys():
    if not os.path.exists(os.path.join(DATA_PATH, sign)):
        os.makedirs(os.path.join(DATA_PATH, sign))