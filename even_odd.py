
def even_or_odd(number):
    if int(number) % 2 == 0:
        return("the number "+str(number)+" is even")
    if int(number) % 2 == 1:
        return("the number "+str(number)+" is odd")

def main():
    number = input("")
    print(even_or_odd(number))

if __name__ == '__main__':
    main()