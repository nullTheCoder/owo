import random

f = open("input.txt", "r")

endLines = []

for line in f.readlines():
    ir = random.randint(0, 3)
    if ir == 0:
        a = "§d§lOwO§r"
    if ir == 1:
        a = "§d§lUwU§r"
    if ir == 2:
        a = "§d§lOWO§r"
    if ir == 3:
        a = "§d§lUWU§r"
        
    if "=" in line:
        x = line.split("=")
        y = x[1].replace("r", "w").replace("t", "h")
        res = x[0] + "=" + y.rstrip("\n") + " " + a
        
    else:
        res = line
    
    endLines.append(res)

f.close()

f = open("en_US.lang", "w")

for x in endLines:
    f.write(x + "\n")
