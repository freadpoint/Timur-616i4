# print("null")
# psrp_list = [21, 3, 76, 86, 12]
# weak = 0
# for v in psrp_list:
#     if v < -105:
#         print(v, "- zeif")
#         weak = weak + 1
#     else:
#         print(v, "- normal")

# print("Zeif olcme sayi:", weak)


imput_1 = int(input())
if imput_1 < 1:
    print(imput_1, "number is less than 0")
elif imput_1 == 0:
    print(imput_1, "you have got the 0")
elif imput_1 > 2:
    print(imput_1, "you have more than 0")
else:
    print('no such number')