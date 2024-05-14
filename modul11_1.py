# Program untuk pengecekan apakah semua anggota tuple sama
def pengecekan(data):
    if type(data) == tuple:
        flag = True
        for x in data:
            if x == data[0]:
                flag = True
            else:
                flag = False
    else:
        flag = False
    print(flag)

tA= (90, 90, 90, 90)
pengecekan(tA)

