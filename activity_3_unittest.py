from turtle import color
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from activity3 import file


def coef(x,y):
    n = np.size(x)
    x_m = np.mean(x)
    y_m = np.mean(y)
    ss_xy = np.sum(y*x) - n*y_m*x_m
    ss_xx = np.sum(x*x) - n*x_m*x_m

    b_1 = ss_xy / ss_xx
    b_0 = y_m - b_1*x_m

    return(b_0, b_1)

def plot_regression_line(x,y,b):
    plt.scatter(x, y, color='m', marker="o", s=30)

    y_pred = b[0]+b[1]*x
    plt.plot(x, y_pred, color="g")

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show()

def main():

    x= file["X"]
    y= file["Y"]

    b = coef(x,y)
    print("Estimated coefficeint:\nb_0 = {} \
        \nb_1 = {}".format(b[0], b[1]))

    plot_regression_line(x, y, b)

if __name__ == "__main__":
    main()
