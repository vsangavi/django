import random
#generating random numbers
r=random.randint(1,100)
ct=0
while(ct<10):
   n=int(input("enter the number"))
   if n==r:
     print("found the number in",ct,"attempts")
     break
   if n>r:
     print("guessed number is greater")
     ct+=1;
   if n<r:
     print("guessed number is lesser")
     ct+=1
if ct>10:
    print("your trial is above 10")
    
