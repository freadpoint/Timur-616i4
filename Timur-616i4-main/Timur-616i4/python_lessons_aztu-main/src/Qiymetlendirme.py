#-91.5 -108.1 NA -86.2 -103.3 -105 NA -97.4 -89.0
parts= input ().split()
values=[]
missing=0
for p in parts :
    if p =="NA":
      missing += 1
else :
    values.append(float(p))
print("Ölçmə:", len(values))
print("Boş:", missing)
print("min:", min(values))
print("max:", max(values))
avg=round(sum(values))
print("orta qiymet:",avg)
def level (v):
    if v <-105:
        return "zəif"
    elif v <-95:
        return "orta"
    else:
        return "yaxşi"
for v in values:
    print(v, "-", level (v))
count=("zəif":0"orta":0,"yaxşi":0)
for v in values:
  S=level
  counts[1] +=1
print(counts)
share=round(counts["zəif"]/len(values))

