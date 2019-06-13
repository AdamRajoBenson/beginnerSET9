p=str(input())
q=list(p)
for i in q:
    if(i.isnumeric()):
        print(i,end="")
    else:
        print("")
