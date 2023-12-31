import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from io import BytesIO
from my_fonts import font_style, my_text_header, my_text_paragraph
from barnsley_fern import BarnsleyFern
from color_options import get_color_list

st.set_page_config(
    page_title="Dotty",
    layout="centered",
    page_icon="🟣",
    initial_sidebar_state="expanded"
)


def vertical_spacer(n):
    for i in range(n):
        st.write("")


# SETUP DIFFERENT FONT STYLES
st.markdown(font_style, unsafe_allow_html=True)


class DotPainter:
    """
    DotPainter class for creating customizable dot paintings.

    This class allows users to create dot paintings with various shapes, colors,
    and styles. It provides options for selecting the dot size, gap size, canvas shape,
    color styles, and more.

    Attributes:
        color_list (list): A list of colors based on the selected color style.
    """

    def __init__(self):
        """
        Initialize the DotPainter class.

        This method sets up the initial parameters for creating dot paintings.
        """
        with st.sidebar:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image('https://raw.githubusercontent.com/tonyhollaar/art/main/damien_hirst/images/dotty_logo.svg', width=250)  # logo

        my_text_header('CREATE YOUR SPOT PAINTING', my_font_family='Oswald')

        # add some newlines for added space between header and dot painting
        vertical_spacer(2)
        self.color_list = []
        self.n = 1000  # Default value for Barnsley Fern Shape

    def create_dot_painting(self, dot_size, gap_size, canvas_size, canvas_shape, shape, dpi, figsize_ratio=1.0,
                            image_format="SVG"):
        """
        Create a dot painting with the specified parameters.

        Args:
            dot_size (int): The size of each dot in the painting.
            gap_size (int): The gap size between dots.
            canvas_size (int): The size of the canvas where dots will be painted.
            canvas_shape (str): The shape of the canvas.
            shape (str): The shape of individual dots (e.g., circle, square).
            dpi (int): The resolution for JPEG images.
            figsize_ratio (float): The ratio to adjust the figure size.
            image_format (str): The image format for saving (SVG or JPEG).

        This method creates a dot painting based on the specified parameters and displays it in the Streamlit app.
        """
        n = self.n  # Access n from the class attribute for Barnsley Fern Shape

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

        if canvas_shape == "square":
            for row in range(rows):
                for col in range(cols):
                    x = col * gap_size
                    y = row * gap_size
                    color = random.choice(self.color_list)
                    ax.scatter(x, y, c=[color], s=dot_size, marker=marker)

        elif canvas_shape == "circle1":
            # Calculate the number of dots to evenly distribute within the circle
            circle_radius = min(canvas_size, canvas_size) / 2
            num_circles = int(circle_radius / gap_size)  # Number of circles to draw
            num_dots_per_circle = 50  # Increase the number of dots for a fuller circle

            for i in range(num_circles):
                radius = (i + 1) * gap_size  # Increase the radius for each circle
                theta = np.linspace(0, 2 * np.pi, num_dots_per_circle)
                x = radius * np.cos(theta) + canvas_size / 2
                y = radius * np.sin(theta) + canvas_size / 2

                colors = [random.choice(self.color_list) for _ in range(num_dots_per_circle)]
                ax.scatter(x, y, c=colors, s=dot_size, marker=marker)  # Use 'o' for a circle

        elif canvas_shape == "circle2":
            # Calculate the number of dots to evenly distribute within the circle
            circle_radius = min(canvas_size, canvas_size) / 2

            # Calculate the number of circles based on the gap size
            num_circles = int(circle_radius / gap_size)  # Number of circles to draw

            # Create a figure and axis
            fig, ax = plt.subplots(figsize=(canvas_size / 100 * figsize_ratio, canvas_size / 100 * figsize_ratio))
            ax.set_aspect('equal')
            ax.axis('off')

            # Add a single dot in the center
            ax.scatter(canvas_size / 2, canvas_size / 2, c=[random.choice(self.color_list)], s=dot_size, marker=marker)

            for i in range(num_circles):
                radius = (i + 1) * gap_size
                n = 7 * (i + 1)  # 6 dots in each circle
                theta = np.linspace(0, 2 * np.pi, n)
                x = radius * np.cos(theta) + canvas_size / 2
                y = radius * np.sin(theta) + canvas_size / 2
                colors = [random.choice(self.color_list) for _ in range(n)]
                ax.scatter(x, y, c=colors, s=dot_size, marker=marker)

        elif canvas_shape == "golden ratio":
            # Adjust the number of dots based on gap_size
            num_dots = int(2 * np.pi * (canvas_size / 2) / gap_size)
            # phi = (1 + np.sqrt(5)) / 2  # Golden ratio

            fig, ax = plt.subplots(figsize=(canvas_size / 100 * figsize_ratio, canvas_size / 100 * figsize_ratio))
            ax.set_aspect('equal')
            ax.axis('off')

            angles = np.linspace(0, 2 * np.pi * num_dots, num_dots)
            radii = np.sqrt(1.0 * np.arange(num_dots)) / np.sqrt(num_dots)
            x = radii * np.cos(angles) * canvas_size / 2 + canvas_size / 2
            y = radii * np.sin(angles) * canvas_size / 2 + canvas_size / 2

            colors = [random.choice(self.color_list) for _ in range(num_dots)]
            ax.scatter(x, y, c=colors, s=dot_size, marker=marker)

        if canvas_shape == "barnsley fern":
            # load bar
            my_bar = st.progress(0, text="Operation in progress. Please wait.")

            blf = BarnsleyFern()
            color_list = self.color_list
            x, y, colors = blf.draw_fern(n, color_list)
            fig, ax = plt.subplots(figsize=(5, 5))
            ax.axis('off')

            for i in range(n):
                color = colors[i]
                ax.scatter(x[i], y[i], s=1, c=color)

                # load bar show progress to user
                my_bar.progress((i / n), text=f"fern in progress: {int((i / n) * 100)+1}%")

            # clear load bar
            my_bar.empty()

        if image_format == "SVG":
            # Create an SVG image
            buffer = BytesIO()
            plt.savefig(buffer, format="svg", bbox_inches='tight')  # Use 'tight' to remove excess white space
            buffer.seek(0)
            svg_content = f'''<div style="text-align: center; ">{buffer.getvalue().decode()}</div>'''
            st.markdown(svg_content, unsafe_allow_html=True)
        else:
            # Create a JPEG image
            buffer = BytesIO()
            plt.savefig(buffer, format="jpeg", bbox_inches='tight', dpi=dpi)  # Use 'tight' to remove excess white space
            buffer.seek(0)
            st.image(buffer)

        with st.sidebar:
            with st.columns([1, 10, 1])[1]:
                if image_format == "SVG":
                    st.download_button(
                        label=f"Download Image (SVG)",
                        data=buffer,
                        file_name=f"dot_painting.svg",
                        mime="image/svg+xml",
                        key="svg_download_button",
                        use_container_width=True)
                else:
                    st.download_button(
                        label=f"Download Image (JPEG)",
                        data=buffer,
                        file_name=f"dot_painting.jpeg",
                        mime="image/jpeg",
                        key="jpeg_download_button",
                        use_container_width=True)

    def run(self):
        """
        Run the DotPainter app.

        This method runs the Streamlit app for creating dot paintings and allows users to customize their paintings.
        """
        with st.sidebar:
            my_text_header('palette', my_font_family='Oswald')
            col1, col2, col3, col4 = st.columns([1, 5, 5, 1])
            with col2:
                color_style = st.selectbox("Select Color Style:",
                                           ["Pop Art", "Harmony Hues",
                                            "Mono 1", "Mono 2",
                                            "Viridis", "Plasma", "Inferno", "Magma", "Cividis",
                                            "Pastel1", "Pastel2", "Paired", "Accent", "Dark2",
                                            "Set1", "Set2", "Set3", "tab10", "tab20", "tab20b", "tab20c",
                                            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
                                            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper',
                                            'twilight', 'twilight_shifted', 'hsv',
                                            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
                                            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar'])
                dot_size = st.slider("Dot Size", 5, 800, 800)
                gap_size = st.slider("Gap Size", 10, 50, 24)
                num_colors = st.slider("Number of Colors", 1, 25, 10)

                # Call the get_color_list function to set self.color_list based on the selected color_style
                self.color_list = get_color_list(color_style, num_colors)

            with col3:
                shape = st.selectbox("Dot Shape", ["circle", "square", "triangle", "pentagon", "hexagon", "diamond"])
                canvas_shape = st.selectbox("Shape", ["square", "circle1", "circle2", "golden ratio", "barnsley fern"], index=0)
                canvas_size = st.slider("Canvas Size", 70, 800, 228)
                figsize_ratio = st.slider("Figsize Ratio", 0.1, 10.0, 3.33)

            with col2:
                if canvas_shape == "barnsley fern":
                    n = st.slider('Number of points in the Fern', 100, 10000, 1000)  # Barnsley Fern Shape

            # =============================================================================
            # Download
            # =============================================================================
            my_text_header('download', my_font_family='Oswald')

            col1, col2, col3 = st.columns([1, 10, 1])
            with col2:
                image_format = st.selectbox("Image Format", ["SVG", "JPEG"], index=0)
            if image_format == "JPEG":
                with col2:
                    dpi = st.selectbox("Resolution (DPI)", [100, 200, 300], index=2)
            else:
                dpi = 300

        self.create_dot_painting(dot_size, gap_size, canvas_size, canvas_shape, shape, dpi, figsize_ratio, image_format)


if __name__ == "__main__":
    dot_painter = DotPainter()
    dot_painter.run()
