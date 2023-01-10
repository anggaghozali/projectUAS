import time


def Jdl_Tbl():
    print("=========================================================================")
    print("|                              Tugas_UAS                                |")
    print("|    312210030                                               TI.22.C1   |")
    print("|                         Angga Muhamad Gojali                          |")
    print("=========================================================================")
    print("=========================================================================")
    print("| No |     NIM     |       NAMA        |  TUGAS  |  UTS | UAS |  AKHIR  |")
    print("=========================================================================")
  

def foot_Tbl():
    print("=========================================================================")


def cetak_daftar_nilai(df):
    print("Mencetak daftar nilai...")
    Jdl_Tbl()
    if (len(df) == 0):
        print("Belum ada data / Kosong")
    else:
        time.sleep(1)
        x = 1
        for i, j in df.items():
            print('| {0:^3}| {1:11} | {2:<17} | {3:7} | {4:4} | {5:3} | {6:7.2f} |'.format(
                x, i, df[i]["nama"], df[i]["tugas"], df[i]["uts"], df[i]["uas"], df[i]["akhir"]))
            x += 1
        foot_Tbl()


def cetak_hasil_pencarian(df, dn):
    print("mencetak hasil cari nilai...")
    nama = input("Cari Data nilai berdasarkan Nama : ")
    Jdl_Tbl()
    dn.Cari_data(df, nama)
    foot_Tbl()
