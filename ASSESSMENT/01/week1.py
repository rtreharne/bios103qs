from canvasapi import Canvas
import pandas as pd
import random
import numpy as np
from matplotlib import pyplot as plt

# SNAILS

def generate_data(seed=0, save=False, plot=False):

    random.seed(seed)

    m = 2712.3
    b = 1332.2

    # Generate 1000 random x values in the range [2, 10]
    x = np.array([random.gauss(2, 10) for i in range(10000)])

    # Filter our x values less than 2 and greater than 10
    x = x[(x > 2) & (x < 10)]

    y = m * x + b

    # Add random noise to y values
    y = [i + random.gauss(0, 5000) for i in y]

    if plot:
        plt.scatter(x, y)
        plt.xlabel('Snail mass M (g)')
        plt.ylabel('Height L (mm)')
        plt.show()

    df = pd.DataFrame({'Snail mass M (g)': x, 'Height L (mm)': np.cbrt(y)})

    # save data to csv
    if save:
        df.to_csv('week_1_snail_data.csv', index=False)

    return df

def get_or_create_quiz(course, quiz_label):

    pass



if __name__ == "__main__":
    generate_data(seed=0, save=True, plot=True)

    
