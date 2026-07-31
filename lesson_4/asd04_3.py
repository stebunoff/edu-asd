# Lesson 4
import unittest

# Task 4.1 (methods & tests)
class TestStackSize(unittest.TestCase):

    def test_empty_stack_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_nonempty_stack_size(self):
        stack = Stack()
        values = list(range(1, 101))

        for value in values:
            stack.push(value)

        self.assertEqual(stack.size(), len(values))

class TestStackPush(unittest.TestCase):

    def test_empty_stack_push(self):
        stack = Stack()
        value = 1
        stack.push(value)
        self.assertEqual(stack.size(), 1)
        self.assertIs(stack.peek(), 1)

    def test_nonempty_stack_push(self):
        stack = Stack()
        value = 1
        stack.push(100)
        stack.push(value)
        self.assertEqual(stack.size(), 2)
        self.assertIs(stack.peek(), 1)

class TestStackPop(unittest.TestCase):

    def test_empty_stack_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_one_element_stack_pop(self):
        stack = Stack()
        stack.push(100)
        self.assertEqual(stack.pop(), 100)
        self.assertEqual(stack.size(), 0)

    def test_multiple_elements_stack_pop(self):
        stack = Stack()
        stack.push(100)
        stack.push(10)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.size(), 1)

class TestStackPeek(unittest.TestCase):

    def test_empty_stack_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())

    def test_nonempty_stack_peek(self):
        stack = Stack()
        stack.push(100)
        self.assertEqual(stack.peek(), 100)
        self.assertEqual(stack.size(), 1)

# Task 4.2 (head)
class TestHeadStackSize(unittest.TestCase):

    def test_empty_head_stack_size(self):
        stack = Stack()
        self.assertEqual(stack.size(), 0)

    def test_nonempty_head_stack_size(self):
        stack = Stack()
        values = list(range(1, 101))

        for value in values:
            stack.push(value)

        self.assertEqual(stack.size(), len(values))

class TestHeadStackPush(unittest.TestCase):

    def test_empty_head_stack_push(self):
        stack = Stack()
        value = 1
        stack.push(value)
        self.assertEqual(stack.size(), 1)
        self.assertIs(stack.peek(), 1)

    def test_nonempty_head_stack_push(self):
        stack = Stack()
        value = 1
        stack.push(100)
        stack.push(value)
        self.assertEqual(stack.size(), 2)
        self.assertIs(stack.peek(), 1)

class TestHeadStackPop(unittest.TestCase):

    def test_empty_head_stack_pop(self):
        stack = Stack()
        self.assertIsNone(stack.pop())

    def test_one_element_head_stack_pop(self):
        stack = Stack()
        stack.push(100)
        self.assertEqual(stack.pop(), 100)
        self.assertEqual(stack.size(), 0)

    def test_multiple_elements_head_stack_pop(self):
        stack = Stack()
        stack.push(100)
        stack.push(10)
        self.assertEqual(stack.pop(), 10)
        self.assertEqual(stack.size(), 1)

class TestHeadStackPeek(unittest.TestCase):

    def test_empty_head_stack_peek(self):
        stack = Stack()
        self.assertIsNone(stack.peek())

    def test_nonempty_head_stack_peek(self):
        stack = Stack()
        stack.push(100)
        self.assertEqual(stack.peek(), 100)
        self.assertEqual(stack.size(), 1)

# Task 4.5 (parens balance)
class TestCheckParensBalance(unittest.TestCase):
    def test_empty_string_balance(self):
        self.assertEqual(checkParensBalance(""), "No parenthesis found")

    def test_string_without_parens_balance(self):
        self.assertEqual(checkParensBalance("abc123"), "No parenthesis found")

    def test_balanced_string_balance(self):
        self.assertEqual(checkParensBalance("abc(123)"), "Sequence balanced")

    def test_balanced_twice_string_balance(self):
        self.assertEqual(checkParensBalance("a(bc(123))"), "Sequence balanced")

    def test_opening_paren_string_balance(self):
        self.assertEqual(checkParensBalance("abc123)"), "Sequence unbalanced")

    def test_closing_paren_string_balance(self):
        self.assertEqual(checkParensBalance("ab(c123"), "Sequence unbalanced")

    def test_closing_first_paren_string_balance(self):
        self.assertEqual(checkParensBalance("ab)c123("), "Sequence unbalanced")

    def test_wrong_ordered_parens_string_balance(self):
        self.assertEqual(checkParensBalance("())("), "Sequence unbalanced")

# Task 4.6 (brackets balance)
class TestCheckParensBalance(unittest.TestCase):
    def test_empty_string_balance(self):
        self.assertEqual(checkBracketsBalance(""), "Sequence balanced")

    def test_string_without_parens_balance(self):
        self.assertEqual(checkBracketsBalance("abc123"), "Sequence balanced")

    def test_balanced_string_balance(self):
        self.assertEqual(checkBracketsBalance("abc(123)"), "Sequence balanced")

    def test_balanced_twice_string_balance(self):
        self.assertEqual(checkBracketsBalance("a(bc(123))"), "Sequence balanced")

    def test_opening_paren_string_balance(self):
        self.assertEqual(checkBracketsBalance("abc123)"), "Sequence unbalanced")

    def test_closing_paren_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab(c123"), "Sequence unbalanced")

    def test_closing_first_paren_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab)c123("), "Sequence unbalanced")

    def test_wrong_ordered_parens_string_balance(self):
        self.assertEqual(checkBracketsBalance("())("), "Sequence unbalanced")

    def test_squares_balanced_string_balance(self):
        self.assertEqual(checkBracketsBalance("abc[123]"), "Sequence balanced")

    def test_squares_balanced_twice_string_balance(self):
        self.assertEqual(checkBracketsBalance("a[bc[123]]"), "Sequence balanced")

    def test_opening_square_string_balance(self):
        self.assertEqual(checkBracketsBalance("abc123]"), "Sequence unbalanced")

    def test_closing_square_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab[c123"), "Sequence unbalanced")

    def test_closing_first_square_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab]c123["), "Sequence unbalanced")

    def test_wrong_ordered_squares_string_balance(self):
        self.assertEqual(checkBracketsBalance("[]]["), "Sequence unbalanced")

    def test_curlys_balanced_string_balance(self):
        self.assertEqual(checkBracketsBalance("abc{123}"), "Sequence balanced")

    def test_curlys_balanced_twice_string_balance(self):
        self.assertEqual(checkBracketsBalance("a{bc{123}}"), "Sequence balanced")

    def test_opening_curly_string_balance(self):
        self.assertEqual(checkBracketsBalance("abc123}"), "Sequence unbalanced")

    def test_closing_curly_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab{c123"), "Sequence unbalanced")

    def test_closing_first_curly_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab}c123{"), "Sequence unbalanced")

    def test_wrong_ordered_curlys_string_balance(self):
        self.assertEqual(checkBracketsBalance("{}}{"), "Sequence unbalanced")

    def test_multiple_brackets_balanced_string_balance(self):
        self.assertEqual(checkBracketsBalance("ab[ca]{123}gp(ye)"), "Sequence balanced")

    def test_wrong_multiple_brackets_string_balance(self):
        self.assertEqual(checkBracketsBalance("([)]"), "Sequence unbalanced")

# Task 4.7 (min)
class TestMinStack(unittest.TestCase):
    def test_empty_min_stack_peek_min(self):
        stack = StackWithMin()
        self.assertIsNone(stack.peekMin())

    def test_nonempty_min_stack_peek_min(self):
        stack = StackWithMin()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.peekMin(), 1)

    def test_nonempty_reversed_min_stack_peek_min(self):
        stack = StackWithMin()
        stack.push(2)
        self.assertEqual(stack.peekMin(), 2)
        stack.push(1)
        self.assertEqual(stack.peekMin(), 1)

    def test_nonempty_same_value_min_stack_peek_min(self):
        stack = StackWithMin()
        stack.push(2)
        stack.push(2)
        stack.pop()
        self.assertEqual(stack.peekMin(), 2)

    def test_nonempty_after_pop_min_stack_peek_min(self):
        stack = StackWithMin()
        stack.push(4)
        stack.push(3)
        stack.push(1)
        stack.pop()
        self.assertEqual(stack.peekMin(), 3)

    def test_nonempty_after_pop_not_min_min_stack_peek_min(self):
        stack = StackWithMin()
        stack.push(4)
        stack.push(1)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.peekMin(), 1)

    def test_nonempty_after_pop_all_min_stack_peek_min(self):
        stack = StackWithMin()
        stack.push(4)
        stack.push(1)
        stack.pop()
        stack.pop()
        self.assertIsNone(stack.peekMin())

# Task 4.8 (average)
class TestStackWithAvg(unittest.TestCase):
    def test_empty_stack_with_avg(self):
        stack = StackWithAvg()
        self.assertIsNone(stack.avg())

    def test_one_element_stack_with_avg(self):
        stack = StackWithAvg()
        stack.push(2)
        self.assertEqual(stack.avg(), 2)

    def test_multiple_elements_stack_with_avg(self):
        stack = StackWithAvg()
        stack.push(2)
        stack.push(4)
        self.assertEqual(stack.avg(), 3)

    def test_empty_stack_after_pop_stack_with_avg(self):
        stack = StackWithAvg()
        stack.push(2)
        stack.pop()
        self.assertIsNone(stack.avg())

    def test_nonempty_stack_after_pop_stack_with_avg(self):
        stack = StackWithAvg()
        stack.push(2)
        stack.push(3)
        stack.pop()
        self.assertEqual(stack.avg(), 2)

    def test_negative_stack_with_avg(self):
        stack = StackWithAvg()
        stack.push(-2)
        self.assertEqual(stack.avg(), -2)

    def test_fraction_stack_with_avg(self):
        stack = StackWithAvg()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.avg(), 3 / 2)

# Task 4.9 (postfix)
class TestPostfixStack(unittest.TestCase):
    def test_empty_expression(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("")

    def test_invalid_equal_expression(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("1 = 2")

    def test_invalid_addition_expression(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("1 + 2")

    def test_invalid_multiply_expression(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("1 * 2")

    def test_addition_expression(self):
        stack = PostfixStack()
        self.assertEqual(stack.calculateExpression("1 2 +"), 3)

    def test_multiply_expression(self):
        stack = PostfixStack()
        self.assertEqual(stack.calculateExpression("3 3 *"), 9)

    def test_multiple_operators_expression(self):
        stack = PostfixStack()
        self.assertEqual(stack.calculateExpression("1 2 + 3 3 * *"), 27)

    def test_equal_operator_operators_expression(self):
        stack = PostfixStack()
        self.assertEqual(stack.calculateExpression("8 2 + 5 * 9 + ="), 59)

    def test_single_number(self):
        stack = PostfixStack()
        self.assertEqual(stack.calculateExpression("7"), 7)

    def test_spaces_only(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("   ")

    def test_not_enough_operands(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("1 +")

    def test_too_many_operands(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("1 2")

    def test_unknown_operation(self):
        stack = PostfixStack()
        with self.assertRaises(ValueError):
            stack.calculateExpression("1 2 -")

    def test_repeated_calculation(self):
        stack = PostfixStack()
        self.assertEqual(stack.calculateExpression("1 2 +"), 3)
        self.assertEqual(stack.calculateExpression("3 4 *"), 12)


