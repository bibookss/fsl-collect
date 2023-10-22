import streamlit as st
from video_processor import VideoProcessor
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from config import SIGNS


def switch_to_sendrecv_mode(key):
    webrtc_streamer(key, mode=WebRtcMode.SENDRECV, rtc_configuration=RTC_CONFIGURATION)


RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# Header
st.title("Filipino Sign Language Data Collector")

# Instructions
st.write("This app collects the keypoints of the left and right hands to be used in sign language recognition.")

# Add sidebar to choose between live feed and saved video
st.sidebar.title("Choose Mode")
mode = st.sidebar.selectbox(
    "Select Mode",
    ('Live Feed', 'Saved Video')
)

# List of actions
signs = list(SIGNS.keys())
st.sidebar.subheader("Choose Sign")
st.sidebar.selectbox(
            "",
            options=signs,
            key="signs",
            label_visibility="collapsed"
        )

# If live feed is selected
if mode == 'Live Feed':
    st.subheader("Live Feed")
    
    # Video feed
    # TO DO: Explore video callback attribute
    webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
        desired_playing_state=True
    )

else:
    st.subheader("Upload Video")

    # Video uploader
    st.file_uploader("Upload Video")
