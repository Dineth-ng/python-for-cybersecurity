#Readign lines into a list
#very common pattern - load all  lines at once for processing.

with open("ips.txt", "r") as f:
    lines = f.readline() #return a list

ips = [line.strip() for line in lines if line.strip()]
print(ips)  