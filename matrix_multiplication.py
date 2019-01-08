p=input("enter rows of matrix 1")
q=input("enter columns of matrix 1")
a=[[0 for i in range(0 , q)]for j in range(0 , p)]
for i in range(p):
	for j in range(q):
		a[i][j]=input()	
x=input("enter rows of matrix 2")
y=input("enter columns of matrix 2")
b=[[0 for e in range  (0 , y)] for f in range (0 , x)]
result=[[0 for j in range  (0 , y)] for i in range (0 , p)]
for e in range(x):
	for f in range(y):
		b[e][f]=input()		
	
h=0
if (q==x):
	def matrix_mul(a,b):
		for h in range(len(a)):  
   			for l in range(len(b[0])):  
      				for k in range(len(b)):  
           				result[h][l]+=a[h][k]*b[k][l]  
	
		for h in range(len(result)):
   			for l in range(len(result)):
				print (result[h][l],"\t")

		return
	matrix_mul (a,b)
else:
 	print("stop")






