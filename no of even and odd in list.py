
n = int(input("Enter number of elements : "))
lst = []
for i in range(0, n):
	ele = int(input())

	lst.append(ele) # adding the element
	
print(lst)



even_count, odd_count = 0, 0


for num in lst:
	
	
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1
		
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)