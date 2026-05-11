#Basic try/ Except
#wrap risk code. if it fials, except catches the error so your program doesn't crash

try:
    with open("missiong.txt" , "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File Not Found!")
except PermissionError:
    print("No permission to read this file")