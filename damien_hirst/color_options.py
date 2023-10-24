import matplotlib.cm as cm
import streamlit as st


def get_color_list(color_style, num_colors):
    if color_style == "Pop Art":
        return ["#03BFAC", "#75DFCA", "#1DBACC", "#ED3192", "#087FBF"]
    elif color_style == "Harmony Hues":
        return ["#EFE0F3", "#325A94", "#EB9759", "#CF0A33", "#924265",
                "#E8D05A", "#ED4569", "#3BAE47", "#7CB6A4", "#3C896E",
                "#75A6D1", "#F94318", "#C791A8", "#F1F8F4", "#758B41",
                "#896CB8", "#B1B519", "#026A4A", "#C9D306", "#2D2A65",
                "#015574", "#B2C7B3", "#403C38", "#4C2F36", "#28A3D2",
                "#2C2359", "#DAAFBB", "#E7ACA3"]
    # Monochromatic 1
    elif color_style == "Mono 1":
        return ["#0000FF", "#1111FF", "#2222FF", "#3333FF", "#4444FF",
                "#5555FF", "#6666FF", "#7777FF", "#8888FF", "#9999FF"]
    # Monochromatic 2
    elif color_style == "Mono 2":
        base_color = st.color_picker("Choose a Base Color", "#0000FF")
        monochromatic_colors = [base_color]
        for i in range(1, 10):
            shade = base_color.replace("#", f"#{i * 1:02X}")
            monochromatic_colors.append(shade)
        return monochromatic_colors
    # Perceptually Uniform Sequential
    elif color_style in ["Viridis", "Plasma", "Inferno", "Magma", "Cividis"]:
        colormap = getattr(cm, color_style.lower())  # Correct the color_style name
        return [colormap(x) for x in np.linspace(0, 1, 25)]
    # Qualitative
    elif color_style in ["Pastel1", "Pastel2", "Paired", "Accent", "Dark2", "Set1", "Set2", "Set3", "tab10", "tab20", "tab20b", "tab20c"]:
        colormap = getattr(cm, color_style)
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]
    # Sequential
    elif color_style in ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd',
                         'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']:
        colormap = getattr(cm, color_style)  # Correct the color_style name
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]
    # Sequential2
    elif color_style in ['binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']:
        colormap = getattr(cm, color_style)  # Correct the color_style name
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]
    # Cyclic
    elif color_style in ['twilight', 'twilight_shifted', 'hsv']:
        colormap = getattr(cm, color_style)  # Correct the color_style name
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]
    # Diverging
    elif color_style in ['PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu', 'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic']:
        colormap = getattr(cm, color_style)  # Correct the color_style name
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]
    # Miscellaneous
    elif color_style in ['flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar']:
        colormap = getattr(cm, color_style)  # Correct the color_style name
        return [colormap(x) for x in np.linspace(0, 1, num_colors)]
        colormap = getattr(cm, color_style)  # Correct the color_style name
    else:
        return []  # Return an empty list if the color style is not recognized
