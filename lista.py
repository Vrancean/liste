with open('input.txt','r') as f:
    x=list(eval(f.readline()))
print("iniatial: ",x)
y=sorted(x)
print("sortare in ordine crescatoare: ",x)
y.sort(reverse=True)
print("sortare in ordine descrescatoare: ",y)
print("numărul de elemente: ",len(x))
print("elementul maxim: ",max(x))
print("elementul minim:",min(x))
print("Elementul adaugat: ",x+[111])
x[2]=222
print("Inlocuirea elementului doi cu 222 : ",x)
with open('output.txt','w') as f:
    f.write(str(y)+"\n)
