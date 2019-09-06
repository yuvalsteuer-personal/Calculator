from calculator.calculator import calculate


def main():
    expression = ""
    while(expression != "exit()"):
        expression = input(">> ")
        if expression == 'exit()':
            exit(0)
        try:
            print(calculate(expression))
        except Exception as e:
            print(str(e))

main()

