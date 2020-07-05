#fibonacci series using matrix exponentiation 
#Auhtor @Mehulupase01

def multiply(x,y):
	if ( len(y) == 2 ):
		a = x[0]*y[0]+x[1]*y[1]
		b = x[2]*y[0]+x[3]*y[1]
		return [a,b]
	a = x[0]*y[0] + x[1]*y[2]
	b = x[0]*y[1] + x[1]*y[3]
	c = x[2]*y[0] + x[3]*y[2]
	d = x[2]*y[1] + x[3]*y[3]
	return [a,b,c,d]
#This function evaluates the matrix raised to power n=x-1
def matpower( x, n ):
	if ( n == 1 ):
		return x
	if ( n%2 == 0 ):
		return matpower( multiply(x, x), n//2 )    #recursive exponentiation
	return multiply(x, matpower( multiply(x, x), n//2 ) )
	
#initial matrices for calculation
A = [1,1,1,0]
v = [1,0]

x =int(input())
print(multiply(matpower(A,x-1),v)[0])
