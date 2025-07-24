
a=1.23
b=1
c=1.2345

print("a: {:>10.1f} b: {:^10} c: {:<10.2f}".format(a,b,c))

d=[1,2,3,4,5]
res=[val**2 for val in d]
print(res)

e=['1','2','3','4','5']
li=map(int,e)
print(list(li))