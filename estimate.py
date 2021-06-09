from predict import predict, read_thetas

try:
    msg = int(input("kilometrage ? "))
except:
    print("not a number")
    exit()

read_thetas()
print(str(predict(msg)))
