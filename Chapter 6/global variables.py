#global varibles exist

#defining stuff

def read_global():
    print("From inside the function, the value reads as", value)

def shadow_global():
    value = -1
    print("From inside the function, the value reads as", value)

def change_global():
    global value
    value = -10
    print("From inside the function, the value reads as", value)

#main

value = 10
print("in the global scope, the value is", value)
read_global()

print("in the global scope, the value is still", value)
shadow_global()

print("in the global scope, the value is still", value)

change_global()
print("in the global scope, the value is now", value)

input()
