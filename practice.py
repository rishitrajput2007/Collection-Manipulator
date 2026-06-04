# l=[1,2,3,5,4]
# m=len(l)
# print(m)
#
#
# n=max(l)
# print(n)
#
#
# a=sorted(l)
# print(a)
#
#
# b=sum(l)
# print(b)
#
#
# c=type(l)
# print(c)


# def Rishit(n):
#
#         product = 1
#         for i in range(n, 0, -1):
#
#             product *= i
#         print(product)
#
#
# Rishit(5)



# def square():
#     m = [i * i for i in l]
#     return m
#
# l=[1,2,3,4,5]
# print(square())



# def cube():
#     m=[x**3 for x in l]
#     return m
#
# l=[1,2,3,4,5,6]
# print(cube())



# def calculate(*args):
#     s=0
#     product=1
#     m=len(args)
#     for i in range(m,0,-1):
#         s+=i
#         product*=i
#
#     return s,product
#
#
#
#
#
# su,p=calculate(10,20,30,40,50)
# print(su,p)



# def name(*names):
#     if len(names)==0:
#         print("Student name not found")
#     else:
#
#         for i in names:
#             print(i)
#
# name("rishit","ronit","rahul")
#


# def calculate(**kwargs):
#     print(kwargs)
#
# calculate(name="Rishit",age=19,city="Ahmedabad")


# def calculate(**kwargs):
#     total=0
#     for key,value in kwargs.items():
#         pr=value["price"]
#         quan=value["quantity"]
#         total+=pr*quan
#     print(total)
#
#
#
# calculate(apple={"price": 50, "quantity": 2},
#     mango={"price": 30, "quantity": 3},
#     banana={"price": 10, "quantity": 5})





# def factorial(n):
#     if n==0:
#         return 1
#     elif n<=0:
#         return "Invalid Input"
#     else:
#         return n*factorial(n-1)
#
# a=factorial(-1)
# print(a)

# def fibonaci(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonaci(n-1)+fibonaci(n-2)
#
#
# a=fibonaci(5)
# print(a)


# def name(n):
#     m=len(n)
#     for i in range(m-1,-1,-1):
#         print(n[i],end=" ")
#
#
# n=input("Enter the name: ")
# name(n)



# def calculate(n):
#     sum=0
#     if n<10:
#         return n
#     else:
#         while n>0:
#             rem=n%10
#             sum+=rem
#             n=n//10
#
#     return calculate(sum)
# n=int(input())
# a=calculate(n)
# print(a)

# def calculate(m,n):
#
#     for i in range(m,n+1):
#         count=0
#         for j in range(1,i+1):
#             if(i % j == 0):
#                 count+=1
#
#         if(count==2):
#             print(f"{i} is prime")
#
#         else:
#             print(f"{i} is not prime")
#
#
#
# calculate(2,6)
#
# number=[1,2,3,4,5,6,7,8,9]
# a=list(map(lambda x: x**2,number))
# print(a)


# num=[1,2,3,4,5,6,7,8,9]
# res=filter(lambda x: x%2!=0,num)
# print(list(res))




# l=[10,20,30,40,50]
# sum=0
# for i in range(len(l)):
#     sum+=l[i]
#
# print(sum)
#
# l.insert(2,22)
# print(l)
#
#
# l.remove(22)
# print(l)
#
# l[2]=20
# print(l)
#
# for i in range(len(l)):
#     if l[i]==40:
#         print(f"The index is {i}")
#
# m=[80,90,70,40]
# c=l+m
# print(c)



# l=[]
# n=int(input())
# sum=0
# count=0
# for i in range(n):
#     l.append(int(input()))
#     count+=1
#     sum+=l[i]
#
# print(count)
# print(sum/count)
#
#


# l=[]
# m=[]
# c=[]
# n=int(input())
#
# for i in range(n):
#     l.append(int(input()))
#
#
#
# for i in range(n):
#     m.append(int(input()))
#
# for i in range(n):
#     c.append(l[i] + m[i])
#     print(c[i])



# arr=[1,2,3,4,5,6,7,8,9,10]
# for i in arr:
#     print(2*i)



# n=int(input())
# arr=[1,22,33,44,10]
#
# if n in arr:
#     print("Found")
# else:
#     print("Not Found")
#
# found=0
#
# for i in range(len(arr)):
#     if arr[i]==n:
#         print(f"found at index {i}")
#         found=1
#         break
#
# if found==0:
#     print("Not found")






# arr=[]
# even=[]
# odd=[]
# n=int(input())
# for i in range(n):
#     arr.append(int(input()))
#
# for i in range(n):
#     if arr[i] % 2 == 0:
#         even.append(arr[i])
#
# print(even)
#
#
# for i in range(n):
#     if arr[i] % 2 == 1:
#         odd.append(arr[i])
#
# print(*odd)
#


# l=[2,4,5,6,1,3,5,7,5,32,2,2,6]
# m=len(l)
# print(l[:5])
# print(l[::2])
# print(l[0])
# print(l[-1])
# print(l[m//2])


# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
#
# for i in matrix:
#     for j in i:
#         print(j,end=" ")
#     print()

# matrix=[
#     [1,2,3],
#     [4,5,6]
# ]
# for i in range(3):
#     for j in range(2):
#         # print(matrix[j][i],end=" ")
#         print(i,j)


matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sum=0
a=matrix[0][0]
b=matrix[0][0]
for i in matrix:
    for j in i:
        sum+=j
        if a<=j:
            a=j
        elif b>=j:
            b=j


print(a)
print(b)



print(sum)


l=[2,4,5,56,77,88,1,45]
l.sort()
print(l)

t=(2,5,6,7,8,9,0,10)








