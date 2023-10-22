import streamlit as st
from video_processor import VideoProcessor
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from config import SIGNS

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# Header
st.title("Filipino Sign Language Data Collector")

# Instructions
st.write("This app collects the keypoints of the hand in the video feed.")
st.write("To begin, select signs from the sidebar and press the Start button below.")

# List of actions
signs = ['hello', 'what\'s your name', 'how are you', 'i\'m fine', 'thank you', 'good bye']
st.multiselect(
    "Signs",
    options=signs,
    default=signs,
    key="signs",
)

# Video feed
webrtc_ctx = webrtc_streamer(
    key="WYH",
    mode=WebRtcMode.SENDRECV,
    rtc_configuration=RTC_CONFIGURATION,
    media_stream_constraints={"video": True, "audio": False},
    video_processor_factory=VideoProcessor,
    async_processing=True,
)

# keypoints_placeholder = st.empty()
# if st.button("Get Keypoints"):
#     if webrtc_ctx.video_processor.keypoints is not None:
#         keypoints_list = webrtc_ctx.video_processor.keypoints.tolist() 
#         st.write("Keypoints as a list:", keypoints_list)
#         keypoints_str = str(keypoints_list) 
#         keypoints_placeholder.code("Keypoints:", keypoints_str)  
#     else:
#         keypoints_placeholder.write("No keypoints found.")
