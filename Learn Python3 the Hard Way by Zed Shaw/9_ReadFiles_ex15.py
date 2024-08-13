#from sys import argv

#script, filename = argv
filename = input()
txt = open(filename)

#print(f"\nHere is your python file {script}")
print(f"Here's your text file {filename}:")
print(txt.read())

txt.close()

print("\nType the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()

#Type in terminal like following:
# python ex15.py ex15_sample.txt
