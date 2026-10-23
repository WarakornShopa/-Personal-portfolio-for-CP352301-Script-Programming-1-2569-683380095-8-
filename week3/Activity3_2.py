print("----------A square of asterisks----------")
for a in range(1,6):
    for b in range(1,6):
        print("*",end="")
    print("")

print("")

print("----------A right-angled triangle of asterisks----------")
for c in range(1,6):
    for d in range(1,c+1):
        print("*",end="")
    print("")

print("")

print("----------An inverted right-angled triangle----------")
for e in range(6,1,-1):
    for f in range(e,1,-1):
        print("*",end="")
    print("")

print("")

print("---------- pyramid----------")
for g in range(1,6):
    for h in range(g,5):
        print(" ",end="")
    for i in range(0,((g-1)*2)+1):
        print("*",end="")
    for h in range(g,5):
        print(" ",end="")
    print("")