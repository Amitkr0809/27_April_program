a = "123"
print(a.isdigit())

b = "12.34"
print(b.isdigit())

c = "thundersoft2"
print(c.isdigit())

d = "thundersoft"
print(d.strip("t"))

e = "Thundersoft"
print(e.lower())

f = "ThunDER Soft"
print(f.lower())

g = "thundersoft"
print(g.upper())

h = "ThUnder"
print(h.upper())

i = "hello python"
print(i.startswith("h"))

j = "python"
print(j.startswith("t"))

k = "hello raj"
print(k.endswith("raj"))

l = "welcome"
print(l.endswith("o"))

m ="thunder soft"
print(m.replace(" ","_"))

n = "welcome to thundersoft"
print(n.replace("o","O"))
print(n.replace("e","E"))
