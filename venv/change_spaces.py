# замена всех пробелов в текстовом файле на запятые (для вставки в код мз матлаба в питон)

file = open('coefs.txt','r')
s = []
s_new = []
for line in file:
    s.append(line.replace(' ',','))
file.close()

file = open('coefs2.txt','w')
for line in s:
    file.write(line)
file.close()

f = [1,56,1312,66]

file = open('tetx.txt','w')
for i in range(0,len(f)-1):
    file.write(str(f[i])+' ')
file.close()

print(s[0])