array = int(input("masukan nomor : "))
prima = []
for x in array:
    for i in range(2,x): # atau pake  rumus int(x ** 0.5) + 1
        if x % i == 0:
            break
    else :
        prima.append(x)
print("array : ", array)
print("prima : ", prima)
print("jumlah bilangan prima : "), len(prima)