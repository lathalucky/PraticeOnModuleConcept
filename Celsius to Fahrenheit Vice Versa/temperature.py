# 1. Create a module named temperature.py that contains functions to convert
# Celsius to Fahrenheit and vice versa. Import and use it in another script.
# Celsius to Fahrenheit(F=(9/5*C)+32)
# Fahrenheit to Celsius(C=5/9*(F-32))
def Cel_Fahrenheit():
    C = float(input("Enter Celsius to convert Fahrenheit:"))
    CelFahrenheit = (9 / 5 * C) + 32
    print("{} to {}".format(C, CelFahrenheit))


def Fahrenheit_Cel():
    F = float(input("Enter Fahrenheit to convert Celsius:"))
    FahrenheitCel = 5 / 9 * (F - 32)
    print("{} to {}".format(F, FahrenheitCel))



