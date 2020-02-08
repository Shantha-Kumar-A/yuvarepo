def compute_gcd(x,y):
	while(y):
		print(x,y)
		x,y = y,x % y
	return x

if __name__ == '__main__':
	print(compute_gcd(105,60))