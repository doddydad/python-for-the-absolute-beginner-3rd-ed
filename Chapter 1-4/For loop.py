word = input("You're a nerd \n Harry:")
print("\n here's each letter of your word:")
x = 0
while x<len(word):
    print(word[x], end="  ")
    x+=1
input()

# alternatively
#
#word = input("input word here:")
#print("here's each letter of your word")
#for letter in word:
#    print(letter)
#
#input()
#
