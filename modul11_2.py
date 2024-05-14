# Program Memasukkan Identitas
def identitas(info):
    print('NIM      :', info[1])
    print('NAMA     :', info[0])
    print('ALAMAT   :', info[2],"\n")
    
    tplNim = tuple(info[1])
    print("NIM:", tplNim,"\n")
    tplNamaDepan = tuple(info[0].split()[0])
    print("NAMA DEPAN:", tplNamaDepan,"\n")
    tplNamaTerbalik = tuple(info[0].split()[::-1])
    print("NAMA TERBALIK:", tplNamaTerbalik)

data = ('Matahari Bhakti Nendya', '22064091', 'Bantul, DI Yogyakarta')
identitas(data)

