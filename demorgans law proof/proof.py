U = {1,2,3,4,5,6}
A = {1,2}
B = {3,4}
# L.H.S
x = U.difference(A.intersection(B))
# R.H.S
y = U.difference(A).union(U.difference(B))
if x == y:
    print("demorgan's law is true")
else:
    print("demorgan is trash at maths")