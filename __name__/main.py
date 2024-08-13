#import test

print(f"First Module's Name: {__name__}")
print("Always executed\n")

if __name__ == "__main__":
    print("This line of main file is Executed when invoked directly")
else:
    print("This line of main file is executed when this file is imported to another file")


def some_private_data():
    print("\nHere contains some private data")
    print("You can not see these data if you import this file to another file")

if __name__ == '__main__':
    some_private_data()
