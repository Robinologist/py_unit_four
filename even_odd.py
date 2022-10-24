
def even_or_odd(number):
    if int(number) % 2 == 0:
        print("the number", number, "is even")
    if int(number) % 2 == 1:
        print("the number", number, "is odd")

def main():
    number = input("")
    even_or_odd(number)

if __name__ == '__main__':
    main()