import os.path


def read_thetas():
    thetafile = "thetas"
    global theta0
    global theta1

    if not os.path.isfile(thetafile):
        print("AAAAAAAAAAAA")
    else:
        with open(thetafile) as f:
            content = f.read().splitlines()
            theta0 = int(content[0])
            theta1 = int(content[1])


def predict(km):
    return theta0 + theta1 * km

try:
    msg = int(input("kilometrage ? "))
except:
    print("not a number")
    exit()

read_thetas()
print("prix:" + str(predict(msg)))
