from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()  # используем колоду или двусторонняя очередь

    def pop(self):
        """Метод удаляющий верхний элимент. Стек изменяется. Метод возвращает верхний элимент стека"""
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        self.stack.pop()
        return element

    def push(self, item):
        """Метод добавляющий элимент на верншину стека. Метод ничего не возвращает"""
        self.stack.append(item)

    def is_empty(self):
        """Метод проверки стека на пустоту. Должен возращать True или False"""
        if len(self.stack) == 0:
            return True
        elif len(self.stack) > 0:
            return False

    def peek(self):
        """Метод возращает верхний элимент стека, но не удаляет его. Стек не меняется"""
        if len(self.stack) == 0:
            return None
        element = self.stack[-1]
        return element


def balanced(string):
    stack = Stack()  # создаем экземпляр класса
    balance = True
    index = 0
    while index < len(string) and balance:  # повторяем код пока условие истинно
        symbol = string[index]
        if symbol in "([{":
            stack.push(symbol)  # пополнение стека
        else:
            if stack.is_empty():  # проверка стека на пустоту
                balance = False
            else:
                top = stack.pop()  # удаление элимента из стека
                if not matches(top, symbol):
                    balance = False
        index += 1
    if balance and stack.is_empty():  # проверка стека на пустоту
        return "сбалансировано"
    else:
        return "несбалансировано"


def matches(open_brackets, close):
    """Вспомогательная функция matches, помогающая с соотнесением символов."""
    opens = "([{"
    closers = ")]}"
    return opens.index(open_brackets) == closers.index(close)


if __name__ == '__main__':
    #  сбалансированные
    string_1 = '(((([{}]))))'
    string_2 = '[([])((([[[]]])))]{()}'
    string_3 = '{{[()]}}'
    #  несбалансированные
    string_4 = '}{}'
    string_5 = '{{[(])]}}'
    string_6 = '[[{())}]'

    print(balanced(string_1))
    print(balanced(string_4))
