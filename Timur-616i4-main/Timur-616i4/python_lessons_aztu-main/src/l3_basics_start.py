# # Dərs 3 · Blok 1 — Python-un 10 kərpici
# # İşə salma (de-praktikum qovluğundan): python src/l3_basics_start.py
# # Dərsdə hər kərpicin kodunu slayddan öz bölməsinə yazırıq.
# # Hər bölmə əvvəlcə öz başlığını çap edir — terminalda həmişə
# # ən aşağıdakı bölməyə baxın. Tam kod dərsdən sonra Teams-də olacaq.

# print("=== Kərpic 1 ===")   # Proqram — əmrlər ardıcıllığı
# # TODO: print(...) ilə 4 sətir (slayd «Kərpic 1»)

# print("=== Kərpic 2 ===")   # Dəyişən — adı olan qutu
# # TODO: cell, rsrp, drops

# print("=== Kərpic 3 ===")   # Tiplər: int, float, str, bool, None
# # TODO: type(...) və «mətn ≠ ədəd»

# print("=== Kərpic 4 ===")   # Müqayisə → True / False
# # TODO: rsrp < -105, ==

# print("=== Kərpic 5 ===")   # Siyahı (list)
# # TODO: rsrp_list, indeks, len, orta

# print("=== Kərpic 6 ===")   # Lüğət (dict)
# # TODO: row = {...}, row["region"]

# print("=== Kərpic 7 ===")   # Dövr (for) və şərt (if / else)
# # TODO: zəif ölçmələri saymaq

# print("=== Kərpic 8 ===")   # Funksiya: çağırmaq və yaratmaq
# # TODO: round, len, max; def is_weak(rsrp)

# print("=== Kərpic 9 ===")   # Nöqtə: metod
# # TODO: name.strip().capitalize()

print("=== Kərpic 10 ===")  # import — hazır alət qutusu
# TODO: import math; import pandas as pd

data = "-91.5 -108.1 NA -86.2 -103.3 -105 NA -97.4 -89.0"
parts = data.split()

values = []
missing = 0
for p in parts:
    if p == "NA":
        missing += 1
    else:
        values.append(float(p))
print("Ölçmə:", len(values))
print("Boş:", missing)

print("Min:", min(values))
print("Max:", max(values))
print("Orta qiymət:", round(sum(values) / len(values), 1))

def level(v):
    if v < -105:
        return "zəif"
    elif v < -95:
        return "orta"
    else:
        return "yaxşı"

for v in values:
    print(v, "→", level(v))

counts = {"zəif": 0, "orta": 0, "yaxşı": 0}
for v in values:
    s = level(v)
    counts[s] += 1
print(counts)

share = round(counts["zəif"] / len(values) * 100, 1)
print("Zəif payı:", share, "%")
if share >= 30:
    print("Qərar: briqadanı göndər")
elif share >= 10:
    print("Qərar: müşahidədə saxla")
else:
    print("Qərar: stansiya normaldır")

current = 0
best = 0
for v in values:
    if level(v) == "zəif":
        current += 1
        if current > best:
            best = current
    else:
        current = 0
print("Ən uzun zəif seriya:", best)



























# parts = input().split()
# values = []
# for p in parts:
#         values.append(float(p))
# print(len(values))
# print(min(values))
# print(max(values))
# print(sum(values)/len(values))