for x in range(1,31):
    if ((x % 3) == 0) and ((x % 5) == 0):
            print(f"{x} is FizzBuzz.")
    elif (x % 3) == 0:
        print(f"{x} is Fizz.")
    elif (x % 5) == 0:
        print(f"{x} is Buzz.")
