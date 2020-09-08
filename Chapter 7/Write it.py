#writing files

print("Writing to a file I guess")
text_file = open("write it.txt", "w")
text_file.write("I like to stick dicks in my butt\n")
text_file.write("Lol jk\n")
text_file.write("Some other things\n")
text_file.close()

text_file = open("write it.txt", "r")
for line in text_file:
    print(line)
text_file.close()

print("Creating a file with writelines() function")
text_file = open("write it.txt", "w")
lines = ["Timmy epic beasts\n", "Johnny combo player\n", "Spike the shit"]
text_file.writelines(lines)
text_file.close()

text_file = open("write it.txt", "r")
print(text_file.read())
text_file.close()

