#!/usr/bin/python
import random


def make_terrain_data(n_points=1000):
    # make the toy data set
    grade = [0] * n_points
    bumpy = [0] * n_points
    error = [0] * n_points
    y = [0] * n_points

    random.seed(7)
    for i in range(n_points):
        grade[i] = random.random()
        bumpy[i] = random.random()
        error[i] = random.random()
        if grade[i] > 0.8 or bumpy[i] > 0.8:
            y[i] = 1.0
        else:
            y[i] = round(grade[i]*bumpy[i] + 0.3 + 0.1*error[i])

    # split into train/test sets
    x = [[gg, ss] for gg, ss in zip(grade, bumpy)]
    split = int(0.75*n_points)
    x_train = x[0:split]
    x_test = x[split:]
    y_train = y[0:split]
    y_test = y[split:]

    return x_train, y_train, x_test, y_test
