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
st.write("This app collects the keypoints of the left and right hands to be used in sign language recognition.")

# Add sidebar to choose between live feed and saved video
st.sidebar.title("Choose Mode")
mode = st.sidebar.selectbox(
    "Select Mode",
    ('Live Feed', 'Saved Video')
)

# List of actions
signs = list(SIGNS.keys())

# If live feed is selected
if mode == 'Live Feed':
    st.subheader("Live Feed")

    # Video feed
    webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )

    # Select signs
    if webrtc_ctx.video_processor:
        st.subheader("Select Signs")
        st.selectbox(
            "",
            options=signs,
            key="signs",
            label_visibility="collapsed"
        )

        # Create 


else:
    st.subheader("Upload Video")

    # Video uploader
    st.file_uploader("Upload Video")


    # Select signs
    st.subheader("Select Signs")
    st.selectbox(
            "",
            options=signs,
            key="signs",
            label_visibility="collapsed"
        )
