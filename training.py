from predict import predict, read_thetas
import os.path

def training(filename):
    trainingRatio = 1
    if not os.path.isfile(filename):
        print("AAAAAAAAAAAA")
        exit()
    f = open(filename, "r")
    content = f.read().splitlines()
    f.close
    sumTheta0 = 0
    sumTheta1 = 0
    i = 0
    read_thetas()
    for line in content:
        i += 1
        if i == 1:
            continue
        [km, price] = line.split(',')
        km = int(km)
        price = int(price)
        sumTheta0 += predict(km) - price
        sumTheta1 += (predict(km) - price) * km
    theta0 = sumTheta0 / (i - 1) * trainingRatio
    theta1 = sumTheta1 / (i - 1) * trainingRatio
    print(str(theta0) + ", " + str(theta1))
    f = open("thetas", "w")
    f.write(str(theta0) + '\n' + str(theta1) + '\n')
    f.close()

training("data.csv")
