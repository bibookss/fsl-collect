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

# Define data path
DATA_PATH = os.path.join('data')

# Define number of sequences per action and frames per sequence
NO_SEQUENCES = 30
NO_FRAMES = 30

# Create folders for each sign
for sign in SIGNS.keys():
    for sequence in range(NO_SEQUENCES):
        if not os.path.exists(os.path.join(DATA_PATH, sign, str(sequence))):
            os.makedirs(os.path.join(DATA_PATH, sign, str(sequence)))

    