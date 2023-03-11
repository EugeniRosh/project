class Stack:
    def __init__(self):
        self.stack = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_empty():
            raise StopIteration

        result = self.pop()

        return result

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack) == 0:
            return None

        result = self.stack.pop()

        return result

    def is_empty(self):
        if len(self.stack) == 0:
            return True

        return False

    def peek(self):
        if len(self.stack) == 0:
            return None

        result = self.stack[-1]

        return result


def closing_brackets(text):
    stack_text = Stack()
    circle = 0
    square = 0
    braces = 0

    if len(text) % 2 == 1:
        return False

    for i in text:
        stack_text.push(i)

    for brackets in stack_text:
        if brackets == '(':
            circle += 1
        if brackets == ')':
            circle -= 1

        if brackets == '{':
            braces += 1
        if brackets == '}':
            braces -= 1

        if brackets == '[':
            square += 1
        if brackets == ']':
            square -= 1

        if circle == 1 or square == 1 or braces == 1:
            return False

    return circle == square == braces == 0


print(closing_brackets('([]){}'))
