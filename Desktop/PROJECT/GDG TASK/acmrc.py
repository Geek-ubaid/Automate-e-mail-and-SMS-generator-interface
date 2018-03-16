c=input()
n=int(input())
a=divmod(26,n)
c=c.lower()
if((ord(c)+abs(a[0]))>122):
    print(chr(ord(c)+abs(a[0])-26),end=" ")
else:
    print(chr(ord(c)+abs(a[0])),end=" ")
        
if((ord(c)+abs(a[1]))>122):
    print(chr(ord(c)+abs(a[1])-26),end=" ")
else:
    print(chr(ord(c)+abs(a[1])),end=" ")


