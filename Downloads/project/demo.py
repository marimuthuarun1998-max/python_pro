
data = [1, 2, 3, 2, 1, 4, 2, 3, 1]

dic={}

for i in data:
    dic[i]=dic.get(i,0)-1
    dic[i]=dic.get(i,0)-1

for key,value in dic.items():
    if value>1:
        print(key)
