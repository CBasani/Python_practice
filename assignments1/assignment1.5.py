x = int(input("Pick a number: "))
y = int(input("Pick one more number: "))

if x > y:
    print(f"The first number ({x}) is larger than the second number ({y}).")
elif x < y:
    print(f"The first number ({x}) is smaller than the second number ({y}).")
else:
    print(f"Numbers {x} and {y} are equal.")
    