parts = input().split()
values = []
for p in parts:
        values.append(float(p))
print(len(values))
print(min(values))
print(max(values))
print(sum(values)/len(values))