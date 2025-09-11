def addition():
    a = 3
    b = 12
    c = a + b
    print("%s plus %d equals to %f." % (a,b,c))


def substraction():
    a = 20
    b = 8
    c = a - b
    print("%s minus %d equals to %f." % (a,b,c))


def multiplication():
    a = 6
    b = 7
    c = a * b
    print("%s multiplied by %d equals to %f." % (a,b,c))


def division():
    a = 55
    b = 11
    c = a / b
    print("%s divided by %d equals to %f." % (a,b,c))


def main():
    print("We are going to calculate different things ... ")
    addition()
    substraction()
    multiplication()
    division()
    print("This is it..")


main()