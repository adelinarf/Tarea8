def lejania(C,S):
	maxx = -1
	maxy = -1
	el = None
	for (x,y) in C:
		if x>maxx:
			maxx=x 
			el = tuple([x,y])
		if y>maxy:
			maxy=y 
			el = tuple([x,y])
	index= S.index(el)
	return [maxx*maxy,index]

def costo(i,j,S):
	x = lejania(S[i:j+1],S)
	return x[0]


def pos(i,x,S):
	minimo = 1000
	pos = 1
	for j in range(i+1,len(S)):
		l = lejania(S[i:j],S)
		if l[0]>minimo:
			pos=l[1]
	return pos


def calc(a,b,x,y,S,c,subsequences):
	vals = []
	z = (a+b)//2
	if a>b or x>y:
		return -1
	if a==b or x==y:
		return -1
	subs=[]
	for p in range(x,y):
		if p<z:
			A = c[p-1]+costo(p,z,S)
			subs.append([S[p-1:p],S[p:z+1]])
			vals.append(A)
	c[z] = max(vals)
	index= vals.index(max(vals))
	subsequences[z] = subs[index]
	p= pos(z,x,S)
	calc(a,z-1,x,p,S,c,subsequences)
	calc(z+1,b,p,y,S,c,subsequences)
	return 0


def run(S):
	n=len(S)
	c = [lejania(S[x:x+1],S)[0] for x in range(n)] 
	base = [lejania(S[x:x+1],S)[0] for x in range(n)] 
	unit = lejania(S,S)[0]
	subsequences = [[] for _ in range(n)] 
	calc(1,n,1,n,S,c,subsequences)
	LEJANIA = 0
	PARTICION =[]
	if unit < c[n-1]:
		LEJANIA=unit
		PARTICION=[S[x:x+1] for x in range(n)]
	else:
		LEJANIA=c[n-1]
		PARTICION = subsequences[n-1]

	print("Conjunto:",S)
	print("La particion",PARTICION,"tiene lejania de",LEJANIA)
	return (PARTICION,LEJANIA)


Z = [[(10,2),(3,6),(1,2),(0,5)],[(1,2),(2,3),(3,5),(5,6),(2,4)],[(10,23),(2,3),(6,7),(9,8),(3,4),(5,6),(6,7),(8,7),(8,7),(3,4)],
[(1,3),(20,3),(4,5),(2,3)],[(3,4),(45,67),(5,6),(1,4)],[(45,6),(3,4),(6,7)]]
#Ejemplos de llamadas a la funcion run
for x in Z:
	run(x)
