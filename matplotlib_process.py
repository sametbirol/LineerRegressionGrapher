import numpy as np
import matplotlib.pyplot as plt


def polyfit_process(xval, yval, xlabel, ylabel):
    x = xval.split(',')
    y = yval.split(',')
    x = np.asarray(x, dtype="f")
    y = np.asarray(y, dtype="f")

    m, b = np.polyfit(x, y, 1)

    plt.plot(x, y, 'o', x, m*x+b, '--')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()
    return m, b
