fileWriter = open('Assigment 3\\bear.txt', 'a')
lines = ['I\'m hungry. Can we go downstairs and have some breakfast ?\n', 'A cup for Sue, a cup for me\n', 'Sue likes apple juice but I like tea\n', 'I like juice and she likes tea.\n']
for i in lines:
    fileWriter.write(i)
fileReader = open('Assigment 3\\bear.txt', 'r')
print(fileReader.read())