#write (create file if not exists)
with open("output.txt", "w") as f:
    f.write("Scan Startd\n")

#i did first read the log.txt file and line by line save,
# the variable after line by line write the new output1.txt
with open("log.txt", "r") as f:
    for line in f:
        with open("output1.txt" , "a") as f1:
            f1.write(line)
        
    print("Done!")