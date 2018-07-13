import matplotlib.pyplot as plt
import numpy as np
import time
import math
import random


def rand(high, low):
    randomNum = random.random()

    return randomNum * (high - low) + low


def generatePoints(num):
    object_NumbersGeneretad = []
    for num in range(num):
        obj = {}
        obj['x'] = rand(0, X_MAX)
        obj['y'] = rand(0, Y_MAX)
        object_NumbersGeneretad.append(obj)

    return object_NumbersGeneretad


def team(point):
    if point['x'] > point['y']:
        return -1
    else:
        return 1


def guess(weights, point):
    sum = point['x'] * weights['x'] + point['y'] * weights['y']
    if sum >= 0:
        team = 1
        return team
    else:
        team = -1
        return team


def train(weights, point, team):
    guessResult = guess(weights, point) # 1
    error = team - guessResult
    learningRate = 0.1
    dici = {
        'x': weights['x'] + point['x'] * error * learningRate,
        'y': weights['y'] + point['y'] * error * learningRate
    }

    return dici


Y_MAX = 400
X_MAX = 400

randomPoints = generatePoints(200)

randomWeights = {
    'x': rand(-1, 1),
    'y': rand(-1, 1)
}

examplesPoints = generatePoints(1000000) # 1000000
examples = []
for point in examplesPoints:
    dici = {
        'point': point,
        'team': team(point)
    }
    examples.append(dici)


trainedWeights = {}
currentWeights = randomWeights
for ex in examples:
    currentWeights = train(currentWeights, ex['point'], ex['team'])
trainedWeights = currentWeights


pointTestTrain = {
    'x': 200,
    'y': 400
}
testTrain = train(randomWeights, pointTestTrain, team(pointTestTrain))
print(testTrain)


### plot
colorBlue = "bo-"
colorGray = "go-"
for randPoint in randomPoints:
    if guess(trainedWeights, randPoint) == -1:
        plt.plot(randPoint['x'], randPoint['y'], "bo-", linewidth=2, markersize=2, label="First")
    else:
        plt.plot(randPoint['x'], randPoint['y'], "go-", linewidth=2, markersize=2, label="First")

## line
mean, cov = [0, 0], [(1, .6), (.6, 1)]
x, y = np.random.multivariate_normal(mean, cov, 100).T
y += x + 1

ax = plt.subplot()
ax.scatter(x, y, c='.3')
ax.set(xlim=(0, 400), ylim=(0, 400))

diag_line, = ax.plot(ax.get_xlim(), ax.get_ylim(), ls="-", c=".3")


def on_change(axes):
    # When this function is called it checks the current
    # values of xlim and ylim and modifies diag_line
    # accordingly.
    x_lims = ax.get_xlim()
    y_lims = ax.get_ylim()
    diag_line.set_data(x_lims, y_lims)


# Connect two callbacks to your axis instance.
# These will call the function "on_change" whenever
# xlim or ylim is changed.
ax.callbacks.connect('xlim_changed', on_change)
ax.callbacks.connect('ylim_changed', on_change)

plt.show()
