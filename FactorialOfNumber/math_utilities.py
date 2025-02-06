# function for calculating the factorial of a number
def factorial(n):
    fact = 1
    if n < 0:
        print("please Enter a valid number")
    else:
        for i in range(1, n + 1):
            fact *= i
        return fact

# user_input=int(input("Enter your number to find the factorial:"))
# result=factorial(user_input)
# print(result)
