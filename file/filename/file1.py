'''print(2-3)
print(2.5-6)
print((2+6j)-5)
print((2.5j)-4)
print((3+7j)-(2+4j))
print(2-'don')
a=10
b=('officer👮🏻‍♀️\n')
print(a*b)
a=10
b=20
c=10
print(a==c and not a==b or not a*2==c-10 or not a<b and b+10==c)
print(3%5)
print(5**9.4)
print(a==b)
print(a==c)
print(10*'jon',2*'use',sep='| |')
print("end")
n=input('enter the values: ')
if n>='a' and n<='z':
    print( "n is a alphabets")
else:
    print("n is not alphabet")
n=int(input('enter the values: '))
if n<0 :
    print("n is negative")
n=input('enter the values: ')
if n>='a' and n<='z' or n>='A' and n<='Z':
    print("n is alphabet")
else:
    print("n is not alphabet")
n=int(input('enter the values: '))
# if  n>=10 and n<=50:
#     print("n is between 10 and 50")
if n % 2 != 0 and n % 2 == 0:
    print("This number is neither even nor odd.")
n=(input("enter the value: "))
a=('a','e','i','o','u')
if  (n in a):
   print("a is a vowels")
n=int(input("n: "))
 if n%2==0:
     print("n is even" )
 if n>=-99 and n<=-10 or n>=10 and n<=99 :
    print(f"{n} is single digit only printed")
if n<10:
    print("sucess")
print("Your choose the course")
m=["python full stack","devops","data analysis","data science"]
n=(input("n: "))
if n in m:
    print("you are pyspider student")
else:
    print("you are qspider student")
m=(input("password: "))
if n//2==0 :
    print("n is even")
number = 16
if number > 10 and number % 2 == 0:
    print(f"{number} is even and greater than 10.")
if n>=18 :
    print("vote for eligible candidate")
else:
    print("vote for not eligible candidate")
if n==m :
    print("login successfully")
else:
    print("login failed")


n=int(input("n: "))
if  n>=-9999 and n<=9999:
    if n>=-9 and n<=9 :
        print("n is single digit value")
    elif n>=-99 and n<=99:
        print("n is two digit value")
    elif n>=-999 and  n<=999: 
        print("n is three digit value")
    else:
        print("n is four digit value")
else:
    print("n only 4 digit value printed ")'''


#n=int(input("batter level: "))
# if n<=100 and n>=0:
#     if n<=20:
#         print("low battery level")
#     elif n>=20 and n<=50:
#         print("medium battery level")
#     elif n>=50 and n<=80:
#         print("high battery level")
#     else:
#         print("full battery level")
# else:
#     print("only for bettery level 1 to 100")
# n=int(input("n:"))
# val=n
# for i in range(n):
#     for j in range(n):
#         if i<=j:
#             print(val, end=' ')
#         else:
#             print(' ',end=' ')
#         val-=1
#     print()
#     val=n


# n=input("enter the signal: ")
# if n=='red' or n=='yellow' or n=='green':
#     if n=="red":
#         print("stop")
#     elif n=="yellow":
#         print("caution")
#     else:
#         print("go")
# else:
#     print("invalid signal  colour")
    

# operation=input("operation using for calculate \n + \t - \t*\t/\n option:")
# if operation in ['+','-','*','/']:
#     a=int(input("a: "))
#     b=int(input("b: "))
#     if operation=='+':
#         print(a+b)
#     elif operation=='-':
#         print(a-b)
#     elif operation=='*':
#         print(a*b)
#     else:
#         print(a/b)
# else:
#     print("invalid operation")
# a = int(input("enter the : "))
# b = int(input("enter the : "))
# print(a+b,a-b,a*b,sep="\n")
# n=int (input("n: "))
# for val in range (1,n+1):
#     print('****',end=" ")

# n=input("n: ")
#c=0
# while c<len(n):
#     if c%2==1:
#         print(n[c])
#     c+=1
# n=input("n: ")
# count = 0
# while count < 5:
#     print(n)
#     count += 1  # Increment the counter

# i=1
# while i<11:
#     print(i,end=" ")
#     i+=1

# n=input("n: ")
# i=0
# while i<10 :
#     for i in n:
#         print(" ",end="")
#     print("*",end=" ")
#     i+=1

# i=1
# while i<=10:
#     if i==5 or i==8:
#         i+=1
#         continue
#     print(i)
#     i+=1

# for i in range(2):
#     for j in range(3):
#         print(f"i: {i}, j: {j}")

# n=int(input("n: "))
# m=0
# for i in range(1,n+1):
#     if i%2==0:
#         m+=i
# print(m)

# a=14.073485387953978549
# print(a)
# print(f"{a}")
# print("%d"%a)
# print("%.2f"%a)
# print("%.0f"%a)
# print(round(a,2))
# b=10
# c=20
# print("b value is {} and c value is {}".format(b,c))

# while True:
   
#     match n:
#         case '1':
#             n=int(input("m: "))
#             print("The n value is %c"%n)
#         case 'cancel':
#             break

# for num in range(10,14):
#     for i in range(2,num):
#         if num%i==1:
#             print(num)
#             break

# for i in range(1,11,3):
#     for j in range(1,11,3):
#         if i%2==0:
#             pass
#         print(i)

# l1=[1,2,3]
# l2=[4,5,6,7]
# print(l1)
# l1.extend('tom')
# print(l1)
# l1.append('tom')
# print(l1)
# l1.pop(7)
# c1=l1.pop(6)
# print(l1,c1)
# l1.reverse()
# print(l1)
# l1.sort()
# print(l1)
# l1.sort(reverse=True)
# print(l1)
# l3=l1*4
# print(l3)
l1=[10,20,30,40,90,100,50,60,70,80]
# l1.insert(2,30)
# print(l1)
# l1.pop(2)
# print(l1)
# l1.sort(reverse=True)
# print(l1)
# l1.sort()
# print(l1)
# l1.reverse()
# print(l1)
# l1.remove(10)
# print(l1)
# l1.clear()
# print(l1)
# l1.pop(5)
# print(l1)