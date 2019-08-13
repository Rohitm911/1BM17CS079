n = int(input("Enter the number of fibonacci Numbers you want to print : "))
fib = [0,1]
i = 2
while (i < n):
    a = fib[i-1] + fib[i - 2]
    fib.append(a)
    i+=1
j = 0
while(j < n):
    print(fib[j])
    j+=1
