import pandas as pd

f = open("masiv.csv", 'r')

list_all = []

for line in f:
    line = line.strip()
    parts = line.split('\t')
    list_all.append(parts)

f.close()

df = pd.DataFrame(list_all)

df = df.astype(int)

row_sums = df.sum(axis=1)

with open("res.txt", "w") as f:
    for s in row_sums:
        f.write(str(s) + "\n")

print("Готово! Суми рядків записано у res.txt")