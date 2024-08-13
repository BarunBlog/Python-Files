import main

print(f"Second Module's Name: {__name__}")

if __name__ == "__main__":
    print("This line of test file is Executed when invoked directly")
else:
    print("This line of test file is Executed when this file is imported to another file")
