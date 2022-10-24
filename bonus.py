def calcbonus(years,salary):
    if int(years) <= 5:
        print("You are not eligible for a bonus.")
    else:
        newsalary = (salary + (salary/100*5))
        print(newsalary)

def main():
    years = int(input("How many years have you worked here?\n"))
    salary = int(input("What is your current salary?\n"))

    calcbonus(years,salary)

if __name__ == '__main__':
    main()