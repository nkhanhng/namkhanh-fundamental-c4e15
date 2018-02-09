def eval(x,y,op):
    result = 0

    if op == "+":
        result = x + y
    elif op == "-":
        result = x - y
    elif op == "*":
        result = x * y
    elif op == "/":
        result = x // y

    return result

# x = int(input("x = "))
# oper = input("Operation(+,-,*,/): ")
# y = int(input("y = "))
# eval(x,y,oper)

# x = int(input("x = "))
# oper = input("Operation(+,-,*,/): ")
# y = int(input("y = "))
#
# if oper == "+":
#     result = x + y
# elif oper == "-":
#     result = x - y
# elif oper == "*":
#     result = x * y
# elif oper == "/":
#     result = x / y
#
# print("{0} {1} {2} = {3}".format(x,oper,y,result))
