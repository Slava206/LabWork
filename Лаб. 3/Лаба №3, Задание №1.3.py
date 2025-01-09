f = open('example.txt', 'r', encoding='utf-8')
#a = f.read()
while True:
    a = f.readline()
    if not a:
        break
    print(a.strip())
#print(a)
f.close()
