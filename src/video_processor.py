import av
from detect import process

class VideoProcessor:
    def __init__(self):
        self.keypoints = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        img, self.keypoints = process(img)

        return av.VideoFrame.from_ndarray(img, format="bgr24")
    
    