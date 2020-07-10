from stack import Stack

_left_brackets = ['(','[','{','<']
_right_brackets = [')',']','}','>']

def is_balanced(input_expression):
    """Returns if the given expression is balanced or not"""
    stack = Stack()
    for expression in input_expression:
        if left_brackets(expression):
            stack.push(expression)

        if right_brackets(expression):
            if stack.is_empty():
                return False
            
            top = stack.pop()
            if not does_brackets_match(top,expression):
                return False

    return stack.is_empty()

def left_brackets(bracket):
    return bracket in _left_brackets

def right_brackets(bracket):
    return bracket in _right_brackets

def does_brackets_match(left,right):
    return _left_brackets.index(left) == _right_brackets.index(right)

if __name__ == "__main__":
    input_expression = "(1+2)"
    print(is_balanced(input_expression))
