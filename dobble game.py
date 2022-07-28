import string
import random
n=int(input("ENTER THE NUMBER OF SYMBOLS"))
s=list(string.ascii_letters)
c1=[0]*n
c2=[0]*n
fp1=random.randrange(n)
fp2=random.randrange(n)
cs=random.choice(s)
s.remove(cs)
c1[fp1]=c2[fp2]=cs
for i in range(n):
    if i!=fp1:
        csn=random.choice(s)
        c1[i]=csn
        s.remove(csn)
    if i!=fp2:
        csn=random.choice(s)
        c2[i]=csn
        s.remove(csn)
print(c1)
print(c2)
ch=input("Enter the common symbol ")
if ch==cs:
    print("Identified")
else:
    print("Try again")
    
    
