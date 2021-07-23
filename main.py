# 1-я задача
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

# 2-я задача
def checkParenth(str):
    stack = Stack()
    opening_symbol = "({["
    closing_simbol = ")}]"
    for c in str:
        if c in opening_symbol:
            stack.push(c)
        elif c in closing_simbol:
            if stack.isEmpty():
                return print("Несбалансированно")
            else:
                stack_pop = stack.pop()
                balance_simbol = opening_symbol[closing_simbol.index(c)]
                if stack_pop != balance_simbol:
                    return print("Несбалансированно")
        else:
            return print("Несбалансированно")
    return print("Сбалансированно")


#checkParenth('[[{())}]')

