import streamlit as st
from PIL import Image

from algorithms.canny import apply_canny_filter
from algorithms.laplacian import apply_laplacian_filter
from algorithms.sobel import apply_sobel_filter
from styles import detection_page_style


def detection_screen():
    st.markdown(detection_page_style, unsafe_allow_html=True)
    if st.button("<-   Upload another Image"):
        st.session_state.pop('uploaded_file')
        st.rerun()
    st.title("CV: Edge Detection")
    st.set_page_config(
        layout="wide",
    )

    if 'uploaded_file' in st.session_state:
        image = Image.open(st.session_state.uploaded_file)
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(image)

        output_image = None
        with st.sidebar:
            st.header("Edge Detection Algorithms")
            selected_filter = st.selectbox(
                "Select a filter",
                ["None", "Canny", "Sobel", "Laplacian"]
            )
            st.divider()
            if selected_filter == "Canny":
                lower_threshold = st.slider("Lower Threshold", 0, 255, 50)
                upper_threshold = st.slider("Upper Threshold", 0, 255, 150)
                kernel_size = st.slider("Kernel Size", 3, 15, 5, step=2)
                sigma = st.slider("σ", 0.0, 5.0, 1.0)
                output_image = apply_canny_filter(image, lower_threshold, upper_threshold, kernel_size, sigma)

            elif selected_filter == "Sobel":
                kernel_size = st.slider("Kernel Size", 1, 15, 5, step=2)
                direction = st.radio("Gradient Direction", ["X", "Y", "Both"])
                output_image = apply_sobel_filter(image, kernel_size, direction)

            elif selected_filter == "Laplacian":
                kernel_size = st.slider("Kernel Size", 3, 15, 5, step=2)
                output_image = apply_laplacian_filter(image, kernel_size)

            else:
                output_image = None

        with col2:
            if output_image is not None:
                st.subheader(f"Output Image - {selected_filter}")
                st.image(output_image, clamp=True, channels="GRAY")
            else:
                st.subheader(f"Output Image - No Filter")
                st.image(image)