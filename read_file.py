open("text.txt").read().split()

text = f.read()  # text is now a big string
f.close()  # done reading the file
lines = text.split('\n')  # split text into a list of strings that were separated
# by the newline character '\n' in text
for line in lines:
    print(line)

print('##########################')

#use readlines, which returns a list of all the lines (as strings)
#in the file
f = open('mytextfile.txt')
lines = f.readlines()
f.close()

for line in lines:
    print(line, end="")  #the last character of every line returned by readlines
    #will be a newline character, don't need another
    #newline