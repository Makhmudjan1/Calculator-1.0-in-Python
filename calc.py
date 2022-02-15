#calculator 1.0 in python
#created by mackhack

print("Calculator 1.0 in Python")
while True:
    Fnum = float(input("Enter the number 1: "))

    Op = input("+, -, *, /: ")

    Snum = float(input("Enter the number 2: "))

    if Op == "+":
        print("Result: ", (Fnum + Snum))
    elif Op == "-":
        print("Result: ", (Fnum - Snum))
    elif Op == "*":
        print("Result: ", (Fnum * Snum))
    elif Op == "/":
        print("Result: ", (Fnum / Snum))
    else:
        print("data entry error")
    