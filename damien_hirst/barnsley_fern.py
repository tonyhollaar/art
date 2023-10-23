import random
import numpy as np

# Source: https://high-python-ext-1-doing-math.readthedocs.io/en/latest/chapter6.html
class BarnsleyFern:
    def __init(self):
        pass

    def transformation_1(self, p):  # Add 'self' as the first parameter
        x = p[0]
        y = p[1]
        x1 = 0.85 * x + 0.04 * y
        y1 = -0.04 * x + 0.85 * y + 1.6
        return x1, y1

    def transformation_2(self, p):  # Add 'self' as the first parameter
        x = p[0]
        y = p[1]
        x1 = 0.2 * x - 0.26 * y
        y1 = 0.23 * x + 0.22 * y + 1.6
        return x1, y1

    def transformation_3(self, p):  # Add 'self' as the first parameter
        x = p[0]
        y = p[1]
        x1 = -0.15 * x + 0.28 * y
        y1 = 0.26 * x + 0.24 * y + 0.44
        return x1, y1

    def transformation_4(self, p):  # Add 'self' as the first parameter
        x = p[0]
        y = p[1]
        x1 = 0
        y1 = 0.16 * y
        return x1, y1

    def get_index(self, probability):  # Add 'self' as the first parameter
        r = random.random()
        c_probability = 0
        sum_probability = []
        for p in probability:
            c_probability += p
            sum_probability.append(c_probability)
        for item, sp in enumerate(sum_probability):
            if r <= sp:
                return item
        return len(probability) - 1

    def transform(self, p, probability):  # Add 'self' as the first parameter
        # List of transformation functions
        transformations = [self.transformation_1, self.transformation_2,
                           self.transformation_3, self.transformation_4]
        # Pick a random transformation function and call it
        tindex = self.get_index(probability)  # Use 'self' to call the get_index method
        t = transformations[tindex]
        x, y = t(p)
        return x, y

    def draw_fern(self, n, color_list):
        x = np.zeros(n + 1)
        y = np.zeros(n + 1)
        probability = [0.85, 0.07, 0.07, 0.01]

        for i in range(1, n + 1):
            tindex = self.get_index(probability)  # Use 'self' to call the get_index method
            x1, y1 = self.transform((x[i - 1], y[i - 1]), probability)  # Use 'self' to call the transform method
            x[i] = x1
            y[i] = y1

        # Generate colors for all points outside the loop
        try:
            colors = np.random.choice(np.array(color_list), n)
        except Exception as e:
            print(f"NumPy choice failed with error: {e}")
            colors = [random.choice(color_list) for _ in range(n)]

        return x[1:], y[1:], colors
