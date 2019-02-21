def altsort():
	n=int(input())
	l,r=[],[]
	for i in range(n):
		l.append(int(input()))
	a=0
	for i in range(n):
		m=l[i]
		p=i
		if a==0:
			for j in range(i+1,n):
				if m<l[j] :
					p=j
					m=l[j]
			l[i],l[p]=l[p],l[i]
			a=1
			continue
		if a==1:
			for j in range(i+1,n):
				if m>l[j]:
					p=j
					m=l[j]
			l[i],l[p]=l[p],l[i]
			l[i]=m
			a=0
	print(l)
try:
	altsort()
except:
	print('invalid')
  p
