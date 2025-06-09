import streamlit as st
from utils.analyze import analyze_frame
from PIL import Image
import cv2

st.set_page_config(page_title="Real-Time Webcam Analytics", layout="centered")

st.title("🎥 Webcam Snapshot Analyzer")
st.caption("Note: Webcam video streaming is not supported on Streamlit Cloud. This app uses snapshots.")

uploaded_image = st.camera_input("Take a snapshot")

if uploaded_image:
    face_status, centered_status, gaze_status, analyzed_img = analyze_frame(uploaded_image)

    st.subheader("🧠 Analysis Results")
    st.write("**Face Status:**", face_status)
    st.write("**Centered:**", centered_status)
    st.write("**Gaze Detection:**", gaze_status)

    st.image(cv2.cvtColor(analyzed_img, cv2.COLOR_BGR2RGB), caption="Analyzed Frame", use_column_width=True)
