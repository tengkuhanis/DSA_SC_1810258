x = int(input())
n = int(input())
ans = 0
# n months -> loop
for i in range(n): #0 -> n-1
    p = int(input())
    ans = ans+(x-p) #add the amount left of this months 

ans = ans + x    
print(ans)
