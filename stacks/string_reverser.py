from stack import Stack


def reverse_string(my_string):
    """Return the input string in reverse order"""
    stack = Stack()
    for i in my_string:
        stack.push(i)
    reversed_string = ''
    while(not stack.is_empty()):
        reversed_string += stack.peek()
        stack.pop()
    return reversed_string


def main():
    my_string = input("Enter any string you want to reverse: ")
    reversed_string = reverse_string(my_string)
    print(f"The reversed string is: {reversed_string}")


if __name__ == "__main__":
    main()
