
s="programming"

rev=""

for ch in s:
    if ch not in rev:
        rev=rev+ch

print(rev)