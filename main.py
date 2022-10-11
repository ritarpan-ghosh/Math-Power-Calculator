def powerCal(a, b):
    return a ** b

if __name__ == "__main__":
    
    num = int(input("Enter the base number: "))
    power = int(input("Enter the power number: "))

    ans = powerCal(num, power)
    print(f"{num} to the power {power} is {ans}")

    quit = input("Type 'q' to quit: ")
    if quit=='q':
        exit()
    else:
        quit = input("I said, Type 'q' to quit: ")