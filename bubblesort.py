def bubblesort(A):
	for iteration in range(0, len(A)):
		for current_index in range(0, len(A)-1):
			next_index = current_index + 1
			if(A[current_index] > A[next_index]):
				A[current_index], A[next_index] = A[next_index], A[current_index]
	print(A)

A = [5, 2, 4, 6, 1, 3]
print(A)
bubblesort(A)