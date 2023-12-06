import os 
import shutil
import numpy as np
from config import DATA_PATH

def create_folder(pos, sign):
    sequence = 0
    while os.path.exists(os.path.join(DATA_PATH, pos, sign, str(sequence))):
        sequence += 1

    path = os.path.join(DATA_PATH, pos, sign, str(sequence))
    os.makedirs(path)

    return path

def delete_sequence(path):
    # Delete folder
    shutil.rmtree(path)

def save_keypoints(keypoints, sequence_path, frame):
    npy_path = os.path.join(sequence_path, str(frame))
    try:
        np.save(npy_path, keypoints)
    except:
        print("Error saving keypoints.")
