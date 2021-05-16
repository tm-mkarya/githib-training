while True:
    try:
        item = input("please enter space seperated like 2 + 3: ")
        operands = item.split(" ")
        first = int(operands[0].rstrip(" ").lstrip(" "))
        second = operands[1].rstrip(" ").lstrip(" ")
        third = int(operands[2].rstrip(" ").lstrip(" ").lstrip("\n"))

        if second == "+":
            print ("answer: {}".format(first + third))
        if second == "/":
            print ("answer: {}".format(first / third))
        if second == "*":
            print ("answer: {}".format(first * third))
        if second == "-":
            print ("answer: {}".format(first - third))
    except Exception as e:
        print("error : {}".format(e))