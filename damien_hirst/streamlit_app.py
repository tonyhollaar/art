import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
from io import BytesIO

class DotPainter:
    """
    DotPainter is a Streamlit application for creating customizable spot paintings inspired by Damien Hirst.

    This class allows users to configure various parameters such as dot size, gap size, canvas size, dot shape, and resolution.

    Methods:
        create_dot_painting: Generates and displays the spot painting based on user-defined settings.
        run: Runs the Streamlit application, allowing users to interact with and customize the spot painting.
    """
    def __init__(self):
        # Streamlit app title
        st.title("Create your Spot Painting")
        st.subheader("Inspiration from Damien Hirst")

        # Define the color palette
        self.color_list = [(239, 240, 243), (50, 90, 148), (235, 151, 89), (207, 10, 51), (146, 66, 99),
                          (232, 208, 90), (237, 69, 105), (59, 174, 71), (124, 182, 164), (60, 137, 110),
                          (117, 166, 209), (249, 67, 24), (199, 145, 168), (241, 248, 244), (117, 89, 65),
                          (137, 108, 184), (177, 181, 9), (2, 106, 74), (201, 211, 6), (45, 42, 101),
                          (1, 85, 116), (178, 199, 179), (64, 60, 56), (76, 47, 54), (40, 163, 210),
                          (44, 35, 89), (218, 175, 187), (231, 172, 163)]

    def create_dot_painting(self, dot_size, gap_size, canvas_size, shape, dpi):
        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(canvas_size / 100, canvas_size / 100))

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
        st.pyplot(fig)

        # Add a download button to save the figure as an image with the selected DPI
        buffer = BytesIO()
        plt.savefig(buffer, format="png", dpi=dpi)

        with st.sidebar:
            st.divider()
            st.title('Download')

            with st.columns([1, 50, 1])[1]:
                st.download_button(
                    label=f"Download Image (DPI={dpi})",
                    data=buffer,
                    file_name=f"dot_painting_{dpi}dpi.png",
                    mime="image/png",
                    use_container_width=True
                )

    def run(self):
        # Sidebar with user inputs
        st.sidebar.header("Customization Options")
        dot_size = st.sidebar.slider("Dot Size", 5, 50, 15)
        gap_size = st.sidebar.slider("Gap Size", 10, 50, 30)
        canvas_size = st.sidebar.slider("Canvas Size", 200, 800, 400)
        shape = st.sidebar.selectbox("Dot Shape", ["circle", "square", "triangle", "pentagon", "hexagon", "diamond"])
        dpi = st.sidebar.selectbox("Resolution (DPI)", [100, 200, 300], index=2)

        self.create_dot_painting(dot_size, gap_size, canvas_size, shape, dpi)

if __name__ == "__main__":
    dot_painter = DotPainter()
    dot_painter.run()
