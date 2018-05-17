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
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

# An example:
# uses a stack to reverse a string.


def revstring(mystr):
    result = ''
    s = Stack()
    for c in mystr:
        s.push(c)
    while not s.isEmpty():
        result += s.pop()
    return result


def main():
    mystrs = ['apple', 'x', '12345']
    for s in mystrs:
        print(s, "\t-> ", revstring(s))


if __name__ == '__main__':
    main()
