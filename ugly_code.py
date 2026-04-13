a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 7
h = 8
i = 9
j = 10
k = 11
l = 12
m = 13
n = 14
o = 15
p = 16
q = 17
r = 18
s = 19
t = 20
u = 21
v = 22
w = 23
x = 24
y = 25
z = 26

def F(x):
    print (f"my name is: {__name__}")
    return x * 2 + 1 if x % 2 == 0 else x - 3

def G(y):
	return y // 2 if y > 10 else y + 7

def H(z):
	return F(G(z)) + G(F(z))

print(
	F(a), G(b), H(c), F(d), G(e), H(f), F(g), G(h), H(i), F(j), G(k), H(l),
	F(m), G(n), H(o), F(p), G(q), H(r), F(s), G(t), H(u), F(v), G(w), H(x),
	F(y), G(z)
)