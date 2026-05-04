a = []
for i in range(100):
    a.append(i * 3)
print(a)

# x = [a for b in c]
# a = i * 3
# b = i 
# c = range(100)
x = [i * 3 for i in range(100) ]
print(x)

#z = [a for b in c if d]
# a = i * 3
# b = i 
# c = range(100)
# d =
z = [i for i in range(21) if i % 2 == 0]
print(z)

s = "ciao a tutti, oggi c'è una bellissima giornata e siamo il 10 aprile"
s1 = s.split()

print(s1)

lw = [len(i) for i in s1]
print(lw)

cw = [i.capitalize() for i in s1]
print(cw)

u = "ciao a tutti, oggi c'è una bellissima giornata e siamo il 10 aprile"

ow = [ "e" if len(i) % 2 == 0 else "o" for i in u if i.isalpha() ]
print(ow)
