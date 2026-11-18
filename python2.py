'''s='Good Morning good Afternoon'
print(s[-14:-22-1:-2])
print(s[-17:-21-1:-2])
s=int(input("enter number:"))
print(s)
if s%2==0:
    print("even")
else:
    print("odd")'''


'''ch=input('enter ch:')
if 'A' <=ch<='Z':
    print(True)
else:
    print(False)
     
ch=input('enter char:')   
if 'a'<=ch<='z':
        print(True)
else:
        print(False)'''

'''num=int(input("enter num:"))
if 10<=num<=99:
    print(True)
else:
    print(False)

if 100<=num<=999:
        print(True)
else:
        print(False)'''
'''num1=int(input("enter num:"))
num2=int(input("enter num:"))
if num1<=num2:
    print(num1)
elif num2<=num1:
    print(num2)
else:
    print(not num1)'''


'''a=int(input("enter:"))
b=int(input("enter:"))
if a>b:
    print(f'{a} is greater')
elif b>a:
    print(f'{b} is greater')
else:
    print(f'{a,b} both are equal')'''


''''ch=(input('enter:'))
if 'A'<=ch<='Z':
    print('it is upper')
elif 'a'<=ch<='z':
    print('is lower')
elif 1<=int(ch)<=9:
    print('is num')
else:
    print("special charecgter")'''


' check the given charecter is vowel'
'''ch=input('enter:')
if ch.isalpha():
    if ch in 'aeiouAEIOU':
        print('vowel')
    else:
        print('consonant')
else:
    print('not a alphabet')'''

'list length is even or not and print it'
'''l=eval(input('enter list:'))
if type(l)==list:
    
    if len(l)%2==0:
        print('list even')
    else:
        print("odd")
else:
    print('not a list')'''

'loop'
'''i=1
while i<=5:
     print('hello')
     i+=1'''

' print list elements using while loop'
'''s=[1,2,3]
i=0
while i<len(s):
     print(s[i])
     i+=1'''

''''s=eval(input('enter a list:'))
i=0
while i<len(s):
    print(s[i])
    i+=1'''
'''n=int(input('enter:'))
rev=0
while n>0:
    ld=n%10
    n=n//10
    rev=rev*10+ld
print(rev)'''

'for loop'
'''for i in range(1,5):
    print('hello')'''

'convert uppercase to lowercase'

'''s=input('enter:')
out=''
for i in s:
    if 'A'<=i<='z':
        out=out+chr(ord(i)+32)
    else:
        out+=i
print(out)'''

'convert upper convert to lower or lower to upper or if num or special char print as it is'

'''
s=input('enter:')
out=''
for i in s:
    if "A"<=i<="z":
         out+=chr(ord(i)+32)
    elif "a"<=i<="z":
         out+=chr(ord(i)-32)
    else:
        out+=i
print(out)

'dictionary'
s=[12,10,'hello','Good',5j,'Bye']
out={}
for i in s:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)'''


'''s=input("enter:")\\uper lower
out=''
for i in s:
    if "A"<=i<="Z":
         out+=chr(ord(i)+32)
    elif "a"<=i<="z":
         out+=chr(ord(i)-32)
    else:
        out+=i
print(out)'''

'''for i in range(1,6): \\nested for loop
    for j in range(1,6):
        print('*',end='')
    print()'''

'''def convert(s):
    s=input('enter:')
    out=''
    for i in s:
        if 'A'<=i<='z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    
    return out
print(convert(input('enter:')))
'''

'''def convert(s):
    s=input('enter:')
    out=''
    for i in s:
        if 'A'<=i<='z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    
    print(out)
print(convert(input('enter:')))'''

'''def convert():
    s=input('enter:')
    out=''
    for i in s:
        if 'A'<=i<='z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    
    print(out)
convert()'''

'''def convert():
    s=input('enter:')
    out=''
    for i in s:
        if 'A'<=i<='z':
            out=out+chr(ord(i)+32)
        else:
            out+=i
    return out
    
print(convert())'''


