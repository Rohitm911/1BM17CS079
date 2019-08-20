list=[]
even_li=[]
num=int(input("number of elements you want to insert in a list: "))
for i in range(0,num):
    print("enter the elements of the lists")
    ele=int(input())
    list.append(ele)
print(list)

def even(list):
    for i in list:
        if(i%2==0):
            even_li.append(i)
     
even_(list)
print(even_li)
