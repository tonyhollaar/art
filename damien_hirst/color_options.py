import matplotlib.cm as cm

class ColorOptions:
    def __init__(self):
        pass

    @staticmethod
    def get_pop_art_colors():
        return ["#03BFAC", "#75DFCA", "#1DBACC", "#ED3192", "#087FBF"]

    @staticmethod
    def get_harmony_hues_colors():
        return ["#EFE0F3", "#325A94", "#EB9759", "#CF0A33", "#924265",
                "#E8D05A", "#ED4569", "#3BAE47", "#7CB6A4", "#3C896E",
                "#75A6D1", "#F94318", "#C791A8", "#F1F8F4", "#758B41",
                "#896CB8", "#B1B519", "#026A4A", "#C9D306", "#2D2A65",
                "#015574", "#B2C7B3", "#403C38", "#4C2F36", "#28A3D2",
                "#2C2359", "#DAAFBB", "#E7ACA3"]

    @staticmethod
    def get_mono1_colors():
        return ["#0000FF", "#1111FF", "#2222FF", "#3333FF", "#4444FF",
                "#5555FF", "#6666FF", "#7777FF", "#8888FF", "#9999FF"]

    @staticmethod
    def get_mono2_colors(base_color="#0000FF"):
        # Define a list of monochromatic colors based on the selected base color
        monochromatic_colors = [base_color]
        for i in range(1, 10):  # Generate 10 shades of the base color
            shade = base_color.replace("#", f"#{i * 1:02X}")
            monochromatic_colors.append(shade)
        return monochromatic_colors

    # Add similar methods for other color styles

    @staticmethod
    def get_colormap_colors(colormap_name, num_colors):
        colormap = getattr(cm, colormap_name)
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]