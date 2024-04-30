n=int(input())

for _ in range(n):
    stack=[]
    str=input()
    
    for i in str:
        if i=="(":
            stack.append(i)
        else:
            if len(stack)!=0 and stack[-1]=="(":
                stack.pop()
            else:
                stack.append(i)
                break
    if len(stack)==0:
        print("YES")
    else:
        print("NO")