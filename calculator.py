# 2 + 4 = 6
# 4 /2 = 2

while True:
    item = input("please enter your number and operation: ")

    operation = item.split(" ")
    if operation.__len__() != 3:
        print("please enter three words only")
        exit()
    else:
        first = int(operation[0].strip(" "))
        second = operation[1].strip(" ")
        third = int(operation[2].rstrip("\n"))

    if second == "+":
        print ("answer : {}".format(first + third))
    if second == "-":
        print ("answer : {}".format(first - third))
    if second == "/":
        print ("answer : {}".format(first / third))