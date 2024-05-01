n = int(input())
l = list(map(int, input().split()))
stack = []
order = 1
 
while l:
    if l[0] == order:
        l.pop(0)
        order += 1
    else:
        stack.append(l.pop(0))
 
    while stack:
        if stack[-1] == order:
            stack.pop()
            order += 1
        else:
            break

if len(stack)==0:
    print("Nice")
else:
    print("Sad")
'''
n=int(input())
l=list(map(int, input().split()))
stack=[]
order=1

while order<=n:
    if (len(l)!=0) and l[0]==order:
        l.pop(0)
        order+=1
        continue
    elif len(stack)!=0 and stack[-1]==order:
        stack.pop()
        order+=1
        continue
    else:
        stack.append(l[0])
        l.pop(0)

if len(stack)==0 and len(l)==0:
    print("Nice")
else:
    print("Sad")
'''
