def calcbonus(years,salary):
    if int(years) >= 5:
        newsalary = (salary + (salary / 100 * 5))
        return str(newsalary)
    else:
        return ("You are not eligible for a bonus.")

def main():
    years = int(input("How many years have you worked here?\n"))
    salary = int(input("What is your current salary?\n"))

    print(calcbonus(years,salary))

if __name__ == '__main__':
    main()