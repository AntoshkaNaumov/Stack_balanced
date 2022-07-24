import unittest
from main import balanced, Stack


class TestFunc(unittest.TestCase):

    def test_balanced(self):
        result = balanced('(((([{}]))))')
        etalon_1 = "сбалансировано"
        self.assertEqual(result, etalon_1)

    def test2_balanced(self):
        result = balanced('}{}')
        etalon_2 = "несбалансировано"
        self.assertEqual(result, etalon_2)

    def test3_balanced(self):
        result = balanced('{{[(])]}}')
        etalon_3 = "несбалансировано"
        self.assertEqual(result, etalon_3)

    def test_class_Stack(self):
        stack = Stack()
        stack.push(1)
        result_2 = stack.peek()
        etalon_4 = 1
        self.assertEqual(result_2, etalon_4)


if __name__ == '__main__':
    unittest.main()
