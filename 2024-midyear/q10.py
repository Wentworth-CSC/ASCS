def Calculate(expression: str) -> None:
    # separate the expression in to num1, operator, num2
    for index in range(len(expression)):
        if expression[index] in ["+", "-", "*", "/"]:
            num1: int = int(expression[0:index])
            operator: str = expression[index]
            num2: int = int(expression[index+1::])
            break
    match operator:
        case "+":
            print(num1 + num2)
        case "-":
            print(num1 - num2)
        case "*":
            print(num1 * num2)
        case "/":
            print(num1 / num2)

Calculate ("3+5")
Calculate ("3-5")
Calculate ("3*5")
Calculate ("3/5")

