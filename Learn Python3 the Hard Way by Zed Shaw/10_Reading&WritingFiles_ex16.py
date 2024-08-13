from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename,'w') #'w' itself truncate the file
#'w' stands for writing permission for the opened file
#'r'	open for reading (default)
#'a'	open for writing, appending to the end of the file if it exists
#'+'	open a disk file for updating (reading and writing)
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1+"\n"+line2+"\n"+line3+"\n")

print("And finally, we close it.")
target.close()
