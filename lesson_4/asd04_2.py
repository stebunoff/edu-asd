# Lesson 4
class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.size():
            return None
        
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if not self.size():
            return None

        return self.stack[-1]

# Task 4.5 (parens balance)
def checkParensBalance(string):
    stack = Stack()

    for item in string:
        stack.push(item)

    balance = 0
    changes = 0

    while stack.size() > 0:
        item = stack.pop()

        if item == ")":
            balance += 1
            changes += 1

        if item == "(":
            balance -= 1
            changes += 1

        if balance < 0:
            return "Sequence unbalanced"

    if changes == 0:
        return "No parenthesis found"

    if balance != 0:
        return "Sequence unbalanced"

    return "Sequence balanced"

# Task 4.6 (brackets balance)
def checkBracketsBalance(string):
    opening = { "(", "[", "{" }
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    stack = Stack()

    for item in string:
        if item in opening:
            stack.push(item)
            continue

        if item not in pairs:
            continue

        if stack.size() == 0:
            return "Sequence unbalanced"

        if stack.pop() != pairs[item]:
            return "Sequence unbalanced"

    if stack.size() != 0:
        return "Sequence unbalanced"

    return "Sequence balanced"

# Task 4.7 (min)
class MinStack:
    def __init__(self):
        self.stack = []
    
    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.size():
            return None
        
        return self.stack.pop()

    def peek(self):
        if not self.size():
            return None

        return self.stack[-1]

class StackWithMin:
    def __init__(self):
        self.stack = []
        self.minStack = MinStack()

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.size():
            return None
        
        value = self.stack.pop()
        if value == self.minStack.peek():
            self.minStack.pop()

        return value

    def push(self, value):
        self.stack.append(value)

        minValue = self.minStack.peek()
        if minValue is None or value <= minValue:
            self.minStack.push(value)

    def peek(self):
        if not self.size():
            return None

        return self.stack[-1]

    def peekMin(self):
        if not self.size():
            return None

        return self.minStack.peek()

# Task 4.8 (average)
class StackWithAvg:
    def __init__(self):
        self.stack = []
        self.sum = 0

    def size(self):
        return len(self.stack)

    def pop(self):
        if not self.size():
            return None
        
        value = self.stack.pop()
        self.sum -= value
        return value

    def push(self, value):
        self.stack.append(value)
        self.sum += value

    def peek(self):
        if not self.size():
            return None

        return self.stack[-1]

    # Time complexity O(1)
    # Space complexity O(1)
    def avg(self):
        if not self.size():
            return None

        return self.sum / self.size()

# Task 4.9 (postfix)
class PostfixStack:
    def __init__(self):
        self.stack = []

    def calculateExpression(self, expression):
        expression = self.tokenize(expression)

        if not len(expression):
            raise ValueError("Invalid expression")

        self.clear()

        for index, element in enumerate(expression):
            if isinstance(element, int):
                self.push(element)
                continue

            if element == "=" and index != len(expression) - 1:
                raise ValueError("'=' must be the last element")

            if element == "=":
                break

            if element not in {"+", "*"}:
                raise ValueError(f"Unknown operation: {element}")

            right = self.pop()
            left = self.pop()

            if element == "+":
                self.push(right + left)
                continue

            if element == "*":
                self.push(right * left)
                continue

        if self.size() != 1:
            raise ValueError("Invalid expression")

        return self.pop()

    def tokenize(self, expression):
        tokens = []
        for token in expression.split():
            if token.isdigit():
                tokens.append(int(token))
                continue

            tokens.append(token)

        return tokens

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.size():
            raise ValueError("Invalid expression")

        return self.stack.pop()

рефлексия
2.9: Решение соответствует эталонному.
2.10: Эталонное решение лучше моего по памяти (работает за О(1)).
Чтобы реализовать эталонное решение, мне потребуется переделать метод len (хранить длину в отдельном поле), так как в текущей реализации len зациклится, если в списке уже есть цикл.
Ещё почитал про методы поиска циклов и наткнулся на алгоритм "Черепаха и заяц" Флойда, который как и эталонное решение выполняется за О(1). Запомнил его на будущее.
2.11 Попытался реализовать вместо пузырьковой сортировки сортировку слиянием, запутался в указателях и в итоге не успел сдать доп. задачу. Учту на будущее, что лучше предложить более простое решение, чем не успеть совсем.
2.12 Задачу удалось решить, когда в голове появились приёмы:
- указатели можно хранить в отдельном массиве;
- циклы можно вкладывать в циклы (путал с вложенными друг в друга if);
2.13 Мне импонирует решение через Dummy-узел, так как более явно считывается логика расстановки указателей. Если использовать флаги, то очень легко допустить ошибку, запутавшись в указателях + уже через несколько дней детали вылетают из головы и требуется заново разбираться, как работает код.


