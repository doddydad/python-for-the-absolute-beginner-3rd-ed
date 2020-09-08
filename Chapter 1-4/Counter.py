#counter

START_POINT = int(input("Where do you want to start counting from?:"))
END_POINT = int(input("Where do you want to finish counting?:"))
INCREMENT = int(input("By how much should this count each time?:"))

for i in range(START_POINT, END_POINT+1, INCREMENT):
    print(i, end = "  ")
input()

