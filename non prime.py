num = input()
res=""
for digit in num:
    num=int(digit)
    if num>1:
        for i in range(2,(num//2)+1):
            if num%i==0:
                res=res+str(num)+" "   
                break
if res!="":
    print(f"Prime numbers are: {res}",end="")
else:
    print("there is no prime number")

            
