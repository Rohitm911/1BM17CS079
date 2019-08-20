num=int(input("enter the number to find fibonacci:"))
def fibonacci(num):
    n1=0
    n2=1
    count=0
    if num<=0:
        print("enter a positive integer")
    elif num==1:
        print("Fibonacci sequence upto",num,":")
        print(n1)
    else:
        print("Fibonacci sequence upto",num,":")
    while count<num:
        print(n1,end=' , ')
        sum=n1+n2
        n1=n2
        n2=sum
        count+=1

fibonacci(num)   
