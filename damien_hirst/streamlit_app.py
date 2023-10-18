import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
from io import BytesIO
from my_fonts import font_style, my_text_header, my_text_paragraph

st.set_page_config(
    page_title="Dotties",
    layout="centered",
    page_icon="🟣",
    initial_sidebar_state="expanded"
)

# SETUP DIFFERENT FONT STYLES
st.markdown(font_style, unsafe_allow_html=True)

class DotPainter:
    def __init__(self):
        my_text_header('CREATE YOUR SPOT PAINTING', my_font_family='Oswald')
        my_text_paragraph("Inspired by Damien Hirst")
        self.color_list = [(239, 240, 243), (50, 90, 148), (235, 151, 89), (207, 10, 51), (146, 66, 99),
                          (232, 208, 90), (237, 69, 105), (59, 174, 71), (124, 182, 164), (60, 137, 110),
                          (117, 166, 209), (249, 67, 24), (199, 145, 168), (241, 248, 244), (117, 89, 65),
                          (137, 108, 184), (177, 181, 9), (2, 106, 74), (201, 211, 6), (45, 42, 101),
                          (1, 85, 116), (178, 199, 179), (64, 60, 56), (76, 47, 54), (40, 163, 210),
                          (44, 35, 89), (218, 175, 187), (231, 172, 163)]

    def create_dot_painting(self, dot_size, gap_size, canvas_size, shape, dpi, figsize_ratio=1.0, image_format="SVG"):
        # Calculate the actual figsize using the given ratio
        figsize = canvas_size / 100 * figsize_ratio

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(figsize, figsize))

        # Set the aspect ratio to be equal so the dots are round
        ax.set_aspect('equal')

        # Turn off the axis
        ax.axis('off')

        # Calculate the number of rows and columns in the grid based on canvas size and gap size
        rows = int(canvas_size / gap_size)
        cols = int(canvas_size / gap_size)

        # Define the marker shape based on the selected shape
        shape_to_marker = {
            "circle": 'o',
            "square": 's',
            "triangle": '^',
            "pentagon": 'p',
            "hexagon": 'H',
            "diamond": 'D'
        }
        marker = shape_to_marker.get(shape, 'o')  # Default to circle if shape is not recognized

        for row in range(rows):
            for col in range(cols):
                x = col * gap_size
                y = row * gap_size
                color = random.choice(self.color_list)
                color = tuple(component / 255 for component in color)
                ax.scatter(x, y, c=[color], s=dot_size, marker=marker)

        # Display the dot painting
        # st.pyplot(fig)

        if image_format == "SVG":
            # Create an SVG image
            buffer = BytesIO()
            plt.savefig(buffer, format="svg", bbox_inches='tight')  # Use 'tight' to remove excess white space
            buffer.seek(0)

            svg_content = f'''<div style="text-align: center;">{buffer.getvalue().decode()}</div>'''
            st.markdown(svg_content, unsafe_allow_html=True)
        else:
            # Create a JPEG image
            buffer = BytesIO()
            plt.savefig(buffer, format="jpeg", bbox_inches='tight', dpi=dpi)  # Use 'tight' to remove excess white space
            buffer.seek(0)

            st.image(buffer)

        with st.sidebar:
            my_text_header('download', my_font_family='Oswald')

            with st.columns([1, 50, 1])[1]:
                if image_format == "SVG":
                    st.download_button(
                        label=f"Download Image (SVG)",
                        data=buffer,
                        file_name=f"dot_painting.svg",
                        mime="image/svg+xml",
                        key="svg_download_button",
                        use_container_width=True
                    )
                else:
                    st.download_button(
                        label=f"Download Image (JPEG)",
                        data=buffer,
                        file_name=f"dot_painting.jpeg",
                        mime="image/jpeg",
                        key="jpeg_download_button",
                        use_container_width=True
                    )

    def run(self):
        with st.sidebar:
            my_text_header('palette', my_font_family='Oswald')
        dot_size = st.sidebar.slider("Dot Size", 5, 800, 800)
        gap_size = st.sidebar.slider("Gap Size", 10, 50, 24)
        canvas_size = st.sidebar.slider("Canvas Size", 70, 800, 228)
        shape = st.sidebar.selectbox("Dot Shape", ["circle", "square", "triangle", "pentagon", "hexagon", "diamond"])
        dpi = st.sidebar.selectbox("Resolution (DPI)", [100, 200, 300], index=2)
        figsize_ratio = st.sidebar.slider("Figsize Ratio", 0.1, 10.0, 3.33)

        image_format = st.sidebar.selectbox("Image Format", ["SVG", "JPEG"], index=0)

        self.create_dot_painting(dot_size, gap_size, canvas_size, shape, dpi, figsize_ratio, image_format)

if __name__ == "__main__":
    dot_painter = DotPainter()
    dot_painter.run()
