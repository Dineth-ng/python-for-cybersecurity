#Reading a file with Python
# use open() with 'r' mode. the with statement auto-closes the file-always use with statement when working with files

#read entire file as string
with open("log.txt", "r") as f:
    content = f.read()
    print(content)


#read line by line (Better for larger files)
with open("log.txt", "r") as f:
    for line in f:
        print(line.strip()) #.strip() remove \n
