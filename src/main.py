import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from config import SIGNS, NO_FRAMES
from detect import process
from collect import create_folder, save_keypoints, delete_sequence
import queue
import av

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

# Create thread-safe queue for video processor
results_queue = queue.Queue()

# Callback function for processing video frames
def video_callback(frame):
    image = frame.to_ndarray(format="bgr24")
    image, keypoints = process(image)

    results_queue.put(keypoints)

    return av.VideoFrame.from_ndarray(image, format="bgr24")

st.title("Filipino Sign Language Data Collector")
st.write("This app collects the keypoints of the left and right hands to be used in sign language recognition.")

st.sidebar.title("Menu")
st.sidebar.subheader("Select mode")
mode = st.sidebar.selectbox(
    "",
    ('Live Feed', 'Saved Video'),
    label_visibility="collapsed"
)

parts_of_speech = list(SIGNS.keys())
st.sidebar.subheader("Choose part of speech")
selected_pos = st.sidebar.selectbox(
            "",
            options=parts_of_speech,
            key="part_of_speech",
            label_visibility="collapsed"
        )

if selected_pos:
    signs = list(SIGNS[selected_pos].values())
    st.sidebar.subheader("Choose sign")
    selected_sign = st.sidebar.selectbox(
        "",
        options=signs,
        key="sign",
        label_visibility="collapsed"
    )

if mode == 'Live Feed':
    st.subheader("Live Feed")

    webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_frame_callback=video_callback,
        async_processing=True,
        desired_playing_state=True
    )

    start = st.sidebar.button("Start Recording")
    if webrtc_ctx.state.playing and start:        
        progress_text = "Operation in progress. Please wait."
        status = st.sidebar.progress(0, text=progress_text)

        sequence_path = create_folder(selected_pos, selected_sign)
        for i in range(NO_FRAMES):
            keypoints = results_queue.get()
            save_keypoints(keypoints, sequence_path, i)
            status.progress((i+1)/NO_FRAMES, text=progress_text)

        status.empty()        
        st.sidebar.caption("Keypoints for " + selected_sign + " is saved in " + sequence_path)

        retake = st.sidebar.button("Retake Video", on_click=delete_sequence, args=(sequence_path,))

else:
    st.subheader("Upload Video")
    st.caption("Not yet supported.")