from predict import predict, read_thetas
from statistics import mean
import os.path
import math
import matplotlib.pyplot as plt

def stdingValues(content):
    tabPrice = []
    tabKm = []
    j = 0
    for line in content:
        j += 1
        if j == 1:
            continue
        [skm, sprice] = line.split(',')
        tabPrice.append(float(sprice) / 1000)
        tabKm.append(float(skm) / 1000)
    return (tabPrice, tabKm)

def training(filename):
    trainingRatio = 0.0001
    if not os.path.isfile(filename):
        print("AAAAAAAAAAAA")
        exit()
    f = open(filename, "r")
    content = f.read().splitlines()
    f.close
    [theta0, theta1] = read_thetas()
    stdValuesPrice, stdValuesKm = stdingValues(content)
    lnt = len(stdValuesPrice)
    while (True):
        sumTheta0, sumTheta1 = 0, 0
        for i in range(0, lnt - 1):
            sumTheta0 += predict(theta0, theta1, stdValuesKm[i]) - stdValuesPrice[i]
            sumTheta1 += (predict(theta0, theta1, stdValuesKm[i]) - stdValuesPrice[i]) * stdValuesKm[i]
        tmp_theta0 = (sumTheta0 / lnt) * trainingRatio
        tmp_theta1 = (sumTheta1 / lnt) * trainingRatio
        if abs(tmp_theta0) < float(0.000001) and abs(tmp_theta1) < float(0.000001):
			return (theta0, theta1, stdValuesKm, stdValuesPrice)
        theta0 = theta0 - tmp_theta0
        theta1 = theta1 - tmp_theta1
    return (theta0, theta1, stdValuesKm, stdValuesPrice)

theta0, theta1, km, price = training("data.csv")
theta0 = theta0 * 1000
kmReal = [x * 1000. for x in km]
priceReal = [x * 1000. for x in price]
f = open("thetas", "w")
f.write(str(theta0) + '\n' + str(theta1) + '\n')
f.close()
plt.plot(kmReal, priceReal, 'o', color='#ff0000')
axeX = [0, 260000]
axeY = [theta0, theta0 + (theta1 * 260000)]
plt.plot(axeX, axeY, linestyle='dashed', color='#00ff00')
plt.show()
