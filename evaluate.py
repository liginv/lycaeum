from sys import argv

postfix = argv[1]

print(f"The espression is : {postfix} {type(postfix)}")


def evaluate(expression):
    stack = []
    for i in expression:
        # print(i)
        if i.isdigit():
            stack.append(i)
        else:
            operand_One = int(stack.pop())
            operator = i
            operand_Two = int(stack.pop())

            operators = {'+': operand_One + operand_Two,
                         '-': operand_One - operand_Two,
                         '*': operand_One * operand_Two,
                         '/': operand_One / operand_Two
                         }

            if operators[i]:
                stack.append(operators[i])
            else:
                print(f"Wrong expression{i}!")

    print(f"{stack}")

evaluate(postfix)