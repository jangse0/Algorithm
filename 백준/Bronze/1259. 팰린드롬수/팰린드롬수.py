while True:
    n=input()
    l=len(n)
    
    if n=='0':
        break
        
    if l==1:
        print("yes")
        continue

    for i in range(l//2):
        if n[i]!=n[l-i-1]:
            print('no')
            break
        elif (i + 1)==(l//2):
            print('yes')