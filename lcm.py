p,q=int,input().split()
if(p>q):
    o=p
else:
    o=q
while(1):
    if(o%p==0 and o%q==0):
        print(o)
        break
    o=o+1
