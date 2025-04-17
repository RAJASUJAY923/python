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

             # This code checks if a number is prime or not. It takes an integer input from the user and checks if it is prime by dividing it with all numbers less than itself. If it is divisible by any of those numbers, it is not prime.