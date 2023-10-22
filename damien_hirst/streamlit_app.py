import streamlit as st
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from io import BytesIO
from my_fonts import font_style, my_text_header, my_text_paragraph

st.set_page_config(
    page_title="Dotty",
    layout="centered",
    page_icon="🟣",
    initial_sidebar_state="expanded"
)

# SETUP DIFFERENT FONT STYLES
st.markdown(font_style, unsafe_allow_html=True)


class DotPainter:
    def __init__(self):
        with st.sidebar:
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.image('./images/dotty_logo.svg', width=250)  # logo
        my_text_header('CREATE YOUR SPOT PAINTING', my_font_family='Oswald')
        my_text_paragraph("Inspired by Damien Hirst")
        self.color_list = []

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
                ax.scatter(x, y, c=[color], s=dot_size, marker=marker)

        if image_format == "SVG":
            # Create an SVG image
            buffer = BytesIO()
            plt.savefig(buffer, format="svg", bbox_inches='tight')  # Use 'tight' to remove excess white space
            buffer.seek(0)

            svg_content = f'''<div style="text-align:center;">{buffer.getvalue().decode()}</div>'''
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

            # =============================================================================
            # COLOR STYLES
            # =============================================================================
            col1, col2, col3, col4 = st.columns([1, 5, 5, 1])

            with col2:
                # Create a selectbox in the sidebar to choose the color style
                color_style = st.selectbox("Select Color Style:",
                                           ["Pop Art", "Harmony Hues", "Mono 1", "Mono 2", "Viridis", "Plasma", "Inferno",
                                            "Magma", "Cividis","Pastel1", "Pastel2", "Paired", "Accent", "Dark2", "Set1",
                                            "Set2", "Set3", "tab10", "tab20", "tab20b", "tab20c"])
                dot_size = st.slider("Dot Size", 5, 800, 800)
                gap_size = st.slider("Gap Size", 10, 50, 24)

            # Set color_list based on the user's selection
            if color_style == "Pop Art":
                self.color_list = ["#03BFAC", "#75DFCA", "#1DBACC", "#ED3192", "#087FBF"]

            elif color_style == "Harmony Hues":
                self.color_list = ["#EFE0F3", "#325A94", "#EB9759", "#CF0A33", "#924265",
                                   "#E8D05A", "#ED4569", "#3BAE47", "#7CB6A4", "#3C896E",
                                   "#75A6D1", "#F94318", "#C791A8", "#F1F8F4", "#758B41",
                                   "#896CB8", "#B1B519", "#026A4A", "#C9D306", "#2D2A65",
                                   "#015574", "#B2C7B3", "#403C38", "#4C2F36", "#28A3D2",
                                   "#2C2359", "#DAAFBB", "#E7ACA3"]

            elif color_style == "Mono 1":
                self.color_list = ["#0000FF", "#1111FF", "#2222FF", "#3333FF", "#4444FF",
                                   "#5555FF", "#6666FF", "#7777FF", "#8888FF", "#9999FF"]

            elif color_style == "Mono 2":
                # Create a color picker to select the base color
                with col2:
                    base_color = st.color_picker("Choose a Base Color", "#0000FF")

                # Define a list of monochromatic colors based on the selected base color
                monochromatic_colors = [base_color]
                for i in range(1, 10):  # Generate 10 shades of the base color
                    shade = base_color.replace("#", f"#{i * 1:02X}")
                    monochromatic_colors.append(shade)

                self.color_list = monochromatic_colors

            ####################################################################################
            # Perceptually Uniform Sequential
            ####################################################################################

            elif color_style == "Viridis":
                # Use the 'viridis' color map from Matplotlib
                self.color_list = [cm.viridis(x) for x in np.linspace(0, 1, 25)]

            elif color_style == "Plasma":
                # Use the 'viridis' color map from Matplotlib
                self.color_list = [cm.plasma(x) for x in np.linspace(0, 1, 25)]

            elif color_style == "Inferno":
                # Use the 'viridis' color map from Matplotlib
                self.color_list = [cm.inferno(x) for x in np.linspace(0, 1, 25)]

            elif color_style == "Magma":
                # Use the 'viridis' color map from Matplotlib
                self.color_list = [cm.magma(x) for x in np.linspace(0, 1, 25)]

            elif color_style == "Cividis":
                # Use the 'viridis' color map from Matplotlib
                self.color_list = [cm.cividis(x) for x in np.linspace(0, 1, 25)]

            ####################################################################################
            # Qualitative colormaps
            ####################################################################################
            elif color_style in ["Pastel1", "Pastel2", "Paired", "Accent", "Dark2", "Set1", "Set2", "Set3", "tab10",
                                 "tab20", "tab20b", "tab20c"]:
                # Define the number of colors you want from the selected colormap
                with col3:
                    num_colors = st.slider("Number of Colors", 1, 25, 10)

                # Extract the colors by creating a list of evenly spaced values between 0 and 1
                colormap = getattr(cm, color_style)
                style_colors = [colormap(x) for x in np.linspace(0, 1, num_colors)]

                # Assign the extracted colors to self.color_list
                self.color_list = style_colors

            with col3:
                shape = st.selectbox("Shape", ["circle", "square", "triangle", "pentagon", "hexagon", "diamond"])
                canvas_size = st.slider("Canvas Size", 70, 800, 228)
                figsize_ratio = st.slider("Figsize Ratio", 0.1, 10.0, 3.33)

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

        self.create_dot_painting(dot_size, gap_size, canvas_size, shape, dpi, figsize_ratio, image_format)


if __name__ == "__main__":
    dot_painter = DotPainter()
    dot_painter.run()
