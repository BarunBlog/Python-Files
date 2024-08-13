
class Stack:

    def __init__(self):
        self.stack = []

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, value):
        self.stack.append(value)

    def pop(self) -> int:
        if self.is_empty():
            print("pop from an empty stack")
            return -1

        return self.stack.pop()

    def peek(self) -> int:
        if self.is_empty():
            print("peek from an empty stack")
            return -1

        return self.stack[-1]

    def display(self):
        for item in self.stack:
            print(item, end=" ")

        print()


def main():
    st = Stack()

    st.push(1)
    st.push(2)

    st.display()

    st.pop()

    print(st.peek())
    print(st.is_empty())

    st.pop()
    st.pop()


if __name__ == "__main__":
    main()
