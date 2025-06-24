class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"Popped: {removed}")
        else:
            print("Stack is empty! Cannot pop.")

    def peek(self):
        if not self.is_empty():
            print(f"Top element: {self.stack[-1]}")
        else:
            print("Stack is empty! No top element.")

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Current Stack:", self.stack)

s = Stack()

while True:
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        item = input("Enter item to push: ")
        s.push(item)
    elif choice == "2":
        s.pop()
    elif choice == "3":
        s.peek()
    elif choice == "4":
        s.display()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")


