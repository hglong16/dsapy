from dsapy.libs.stack import Stack

if __name__ == "__main__":
    stack = Stack[int]()

    stack.push(5)
    stack.push(6)
    stack.push(7)
    e = stack.pop()
    print(e)

    print(stack)
