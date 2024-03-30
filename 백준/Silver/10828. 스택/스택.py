import sys
stack=[]
n=int(sys.stdin.readline())
i=0
while i<n:
    a = sys.stdin.readline().split()
    i+=1
    if a[0]=='push':
        stack.append(int(a[1]))
        continue
    
    if a[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
        continue
    
    if a[0]=='size':
        print(len(stack))
        continue
    
    if a[0]=='empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
        continue
        
    if a[0]=='top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
