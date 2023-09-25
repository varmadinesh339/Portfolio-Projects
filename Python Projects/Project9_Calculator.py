



def Add(n1,n2):
    return n1+n2

def Substract(n1,n2):
    if n1 > n2:
        return n1-n2
    elif n1 < n2:
        return n2-n1

def Divide(n1,n2):
    if n2 != 0:
        return n1/n2
    else:
        return "Division by zero"
def Multiply(n1,n2):
    return n1*n2

operations = {
    "+": Add,
    "-": Substract,
    "*": Multiply,
    "/": Divide
}

num1 = float(input("Please Enter your First Number "))
print("""
+
-
*
/
""")
choice = input("Please Choose Your Operation ")
num2 = float(input("Please Enter Your Second Number "))

function = operations[choice]

result = function(num1,num2)

print(f"{num1} {choice} {num2} = {result}")

