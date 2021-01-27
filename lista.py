with open('input.txt', 'r') as f:
    a = f.read()
b = a.split('\n')
c = sorted(b)
print(c)
c = str(c)
with open('output.txt','w') as f:
    f.write(c)
