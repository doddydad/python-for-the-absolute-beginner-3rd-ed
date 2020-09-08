#stain remover
remove = input("Enter a word you hate: ")
new_message = ""
message = input("Enter a message: ")

for letter in message:
    if letter.lower() not in remove.lower():
        new_message += letter

print("having cleansed the heresy, your message is: ", new_message)
input()
