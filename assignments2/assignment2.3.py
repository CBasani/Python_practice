for x in range(1,31):
    if (x % 3) == 0:
        if (x % 5) == 0:
            print(f"{x} can be divided by 3 and 5.")
        else:
            print(f"{x} can only be divided by 3.")
