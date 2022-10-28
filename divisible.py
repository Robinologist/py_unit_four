def is_divisible(num1, num2):
    remainder=num1%num2
    if remainder==0:
        return True
    else:
        return False

def main():

    # Get the two pieces of input from the user.
    num = int(input("What is the first number? "))
    num2 = int(input("What is the second number? "))

    if is_divisible(num, num2):
        print(num, "is cleanly divisible by", num2)
    else:
        print(num, "is not cleanly divisible by", num2)


if __name__ == '__main__':
    main()
