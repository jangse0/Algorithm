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