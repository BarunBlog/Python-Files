from sys import argv
script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
'''
fp.seek(offset, from_what)
where fp is the file pointer you're working with; offset means how many positions you will move; from_what defines your point of reference:

0: means your reference point is the beginning of the file
1: means your reference point is the current file position
2: means your reference point is the end of the file
if omitted, from_what defaults to 0.
'''

def print_a_line(line_count, f):
    print(line_count, f.readline())
'''
readline() reads one entire line from the file.
fileObject.readline( size );
size − This is the number of bytes to be read from the file.
The fle f is responsible for maintaining the current position in the fle after each readline() call
'''



current_file = open(input_file)
print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
