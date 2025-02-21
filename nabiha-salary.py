import calendar
import random

class Finance:
    def __init__(self, salary, month, savingsPercentage, rentPercentage, electricityPercentage, additionalSavings):
        self.salary = salary
        self.month = month
        self.savingsPercentage = savingsPercentage 
        self.rentPercentage = rentPercentage
        self.electricityPercentage = electricityPercentage
        self.additionalSavings = additionalSavings

        self.savingsAmount = (savingsPercentage * salary) / 100    
        self.rentAmount = (rentPercentage * salary) / 100
        self.electricityAmount = (electricityPercentage * salary) / 100

        self.totalExpenses = self.savingsAmount + self.rentAmount + self.electricityAmount
        self.remainingSalary = salary - self.totalExpenses

    def yearlyExpenses(self):
        return {
            "Yearly Rent": self.rentAmount * 12,
            "Yearly Electricity": self.electricityAmount * 12
        }
    
    def calculateAdditionalSavingsRatio(self):
        if self.savingsAmount > 0:
            return self.additionalSavings / self.savingsAmount
        return 0

    def displayReport(self):
        yearly = self.yearlyExpenses()
        savingsRatio = self.calculateAdditionalSavingsRatio()
        print("\n ========== Monthly Finance Report ========== ")
        print(f"Month: {self.month}")
        print(f"Salary: ${self.salary}")
        print(f"Savings ({self.savingsPercentage}%): ${self.savingsAmount}")
        print(f"Additional Savings: ${self.additionalSavings}")
        print(f"Ratio of Additional Savings to Savings Amount: {savingsRatio:.2f}")
        print(f"Rent ({self.rentPercentage}%): ${self.rentAmount}")
        print(f"Electricity ({self.electricityPercentage}%): ${self.electricityAmount}")
        print("-" * 50)
        print(f"Total Expenses: ${self.totalExpenses}")
        print(f"Remaining Salary: ${self.remainingSalary}")
        print("-" * 50)
        print(f"Estimated Yearly Rent: ${yearly['Yearly Rent']}")
        print(f"Estimated Yearly Electricity: ${yearly['Yearly Electricity']}")
        print(f"Salary Squared: {self.salary ** 2}")
        print("=" * 50, "\n") 


def getFloatInput(number):
    while True:
        try:
            value = float(input(number))
            if value < 0:
                print("Please enter a positive number.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a numeric value.")

def getPercentageInput(category):
    while True:
        value = getFloatInput(f"Enter the percentage allocated to {category}: ")
        if 0 <= value <= 100:
            return value
        print("Percentage must be between 0 and 100.")

def getValidMonth():
    validMonths = list(calendar.month_name)[1:]
    while True:
        monthInput = input("Enter the name of the month: ").strip().capitalize()
        if monthInput in validMonths:
            return monthInput
        print("Invalid month! Please enter a valid month name.")

# Main program
while True:
    print("\n --- Monthly Finance Manager ---")
    
    salary = getFloatInput("Enter your salary for the month: ")
    month = getValidMonth()

    while True:
        savingsPercentage = getPercentageInput("Savings")
        rentPercentage = getPercentageInput("Rent")
        electricityPercentage = getPercentageInput("Electricity")

        totalPercentage = savingsPercentage + rentPercentage + electricityPercentage
        if totalPercentage <= 100:
            break
        print(f"\nError: The total allocated percentage exceeds 100% ({totalPercentage}%). Please adjust the values.\n")
    
    additionalSavings = 50  # ثابت أو يمكن تغييره حسب الحاجة
    financeReport = Finance(salary, month, savingsPercentage, rentPercentage, electricityPercentage, additionalSavings)
    financeReport.displayReport()

    anotherReport = input("Do you want to create another finance report? (yes/no): ").strip().lower()
    if anotherReport != "yes":
        break
