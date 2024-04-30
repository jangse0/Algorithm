coin_l=[500, 100, 50, 10, 5, 1]
cnt=0
price=int(input())
change=1000-price

for i in coin_l:
    cnt+=change//i
    change %=i
    
    if change==0:
        break
        
print(cnt)