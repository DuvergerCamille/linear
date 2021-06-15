from predict import predict, read_thetas

try:
    msg = int(input("kilometrage ? "))
except:
    print("not a number")
    exit()

theta0, theta1 = read_thetas()
print(str(predict(theta0, theta1, msg)))
