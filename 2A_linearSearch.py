def search(lis, key):
	print(lis)
	if key in lis:
		return True
	else:
		return False

lis = []

n = int(input("Enter the number of element: "))
while n > 0:
	a = int(input())
	lis.append(a)
	n-=1

b = input("Enter the element to be searched: ")

print(search(lis,int(b)))
