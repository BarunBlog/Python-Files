fw = open('sample.txt','w') ##'w' for writing file
fw.write('Writing some stuff in my text file\n')
fw.write('Barun Bhattacharjee')
fw.close()

fr = open('sample.txt','r') ##'r' for reading file
text = fr.read()
print(text)
fr.close()
