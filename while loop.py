num=int(input("Enter a number: "))
if num>1:
    i=2
    while i<(num//2):
        if num%i==0:
            print(f"{num}is not a prime number")
            break
        i=i+1
    else:
        print(f"{num} is prime number")
else:
    print('enter a valid number')