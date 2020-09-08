#Read it
# shows extracting from files

print("Opening and closing the file")

text_file = open("read it.txt", "r")

text_file.close()

print("\nReading characters from a file\n")

text_file = open("read it.txt", "r")
print(text_file.read(1))
print(text_file.read(5))
text_file.close()

print("\nReading entire file at once")
text_file = open("read it.txt", "r")
print(text_file.read())
text_file.close()

#if this finishes a line, next command will go to next line
print("\nReading characters from a line")       
text_file = open("read it.txt", "r")
print(text_file.readline(1))
print(text_file.readline(5))
text_file.close()

print("\nReading one line at a time")
text_file = open("read it.txt", "r")
print(text_file.readline())
print(text_file.readline())
print(text_file.readline())
text_file.close()

print("\nSome shit with lists")
text_file = open("read it.txt", "r")
lines = text_file.readlines()
print(lines)
print(len(lines))
for line in lines:
    print(line)
text_file.close()

print("\nLoops I guess")
text_file = open("read it.txt", "r")
for line in text_file:
    print(line)
text_file.close()
input()
