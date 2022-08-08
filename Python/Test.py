# Create a function that prints fibanocci series up to nth number

def fib(n):
	""""""
	a, b = 0, 1
	while a < n:
		print(a, end=' ')
		a, b = b, a+b
		
# fib(100)

# A funnction to add two matrixes
def add_matrix(m1, m2):
	""""""
	return [[m1[i][j] + m2[i][j] for j in range(len(m1[0]))] for i in range(len(m1))]


# input for matrixes
m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print(add_matrix(m1, m2))