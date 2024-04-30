while True:
    s = input()
    stack=[]
    if s=='.':
        break
        
    for i in s:
        if i=="(" or i=="[":
            stack.append(i)
        if i==")" or i=="]":
            if len(stack)!=0:
                if (stack[-1]=="(" and i==")") or (stack[-1]=="[" and i=="]"):
                    stack.pop()
                else:
                    stack.append(i)
                    break
            else:
                stack.append(i)
                break

    if len(stack) == 0 :
        print('yes')
    else:
        print('no')
    stack.clear()
         