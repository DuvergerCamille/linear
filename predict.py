import os.path


def read_thetas():
    thetafile = "thetas"

    if not os.path.isfile(thetafile):
        print("AAAAAAAAAAAA")
    else:
        f = open(thetafile)
        content = f.read().splitlines()
        theta0 = float(content[0])
        theta1 = float(content[1])
        f.close()
    return (theta0, theta1)


def predict(theta0, theta1, km):
    return (theta0 + (theta1 * km))

