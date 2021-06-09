import os.path


def read_thetas():
    thetafile = "thetas"
    global theta0
    global theta1

    if not os.path.isfile(thetafile):
        print("AAAAAAAAAAAA")
    else:
        f = open(thetafile)
        content = f.read().splitlines()
        theta0 = int(content[0])
        theta1 = int(content[1])
        f.close()


def predict(km):
    return theta0 + theta1 * km

