import csv
import os
import math
csv_buka = 'data.csv'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    clear_screen()
    print ('### Aplikasi Memprediksi Harga Emas ###')
    show_data()
    inputan_user()
    show_data()
    print('tekan 0 u/ keluar \ntekan 1 u/ lagi ')
    a = input('>> ')
    if ( a == '0'):
        exit()
def show_data():
    data = []
    with open('data.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    print ('tgl \t\t  V1 \t      V2 \t    V3 \t\t  ket')
    print ('-'*63)
    for dt in data:
        print(f"{dt['tgl']} \t {dt['V1']} \t   {dt['V2']} \t   {dt['V3']} \t {dt['ket']}")
def inputan_user():
    with open('data.csv', mode='a', newline='') as csv_file:
        fieldnames = ['tgl', 'V1', 'V2', 'V3', 'ket']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        tgl= input('masukkan tanggal :')
        v1= int (input('masukkan nilai tukar Dollar ke Rupiah:'))
        v2= float (input('masukkan niali tukar Euro ke Rupiah:'))
        v3= float (input('masukkan harga minyak mentah:'))
        V_1 = []
        V_2 = []
        V_3 = []
        clear_screen()
        ket = []
        with open ('ket.csv') as cf:
            buka = csv.reader(cf, delimiter=',')
            for riw in buka:
                ket.append(riw)
            p_naik = float(ket[1][0]) / float(ket[1][3])
            p_tetap = float(ket[1][1]) / float(ket[1][3])
            p_turun = float(ket[1][2]) / float(ket[1][3])
        with open('V1.csv') as cf1:
            buka = csv.reader(cf1, delimiter=',')
            for raw in buka:
                V_1.append(raw)
            mean_v1_naik = float(V_1[1][1]) / float(ket[1][0]) 
            var_v1_naik = float(V_1[2][1]) / (float(ket[1][0]) - 1)
            std_v1_naik = math.sqrt(var_v1_naik)
            mean_v1_tetap = float(V_1[1][2]) / float(ket[1][1])
            var_v1_tetap = float(V_1[2][2]) / (float(ket[1][1]) - 1)
            std_v1_tetap = math.sqrt(var_v1_tetap)
            mean_v1_turun = float(V_1[1][3]) / float(ket[1][2])
            var_v1_turun = float(V_1[2][3]) / (float(ket[1][2]) - 1)
            std_v1_turun = math.sqrt(var_v1_turun)
            p_v1_naik = 1 / ( std_v1_naik * math.sqrt(2 * 22 / 7)) * math.exp(-(( v1 - mean_v1_naik ) ** 2) / ( 2 * var_v1_naik ))
            p_v1_tetap = 1 / ( std_v1_tetap * math.sqrt(2 * 22 / 7)) * math.exp(-(( v1 - mean_v1_tetap ) ** 2) / ( 2 * var_v1_tetap ))
            p_v1_turun = 1 / ( std_v1_turun * math.sqrt(2 * 22 / 7)) * math.exp(-(( v1 - mean_v1_turun ) ** 2) / ( 2 * var_v1_turun ))
        with open('V2.csv') as cf1:
            buka = csv.reader(cf1, delimiter=',')
            for raw in buka:
                V_2.append(raw)
            mean_v2_naik = float(V_2[1][1]) / float(ket[1][0]) 
            var_v2_naik = float(V_2[2][1]) / (float(ket[1][0]) - 1)
            std_v2_naik = math.sqrt(var_v2_naik)
            mean_v2_tetap = float(V_2[1][2]) / float(ket[1][1])
            var_v2_tetap = float(V_2[2][2]) / (float(ket[1][1]) - 1)
            std_v2_tetap = math.sqrt(var_v2_tetap)
            mean_v2_turun = float(V_2[1][3]) / float(ket[1][2])
            var_v2_turun = float(V_2[2][3]) / (float(ket[1][2]) - 1)
            std_v2_turun = math.sqrt(var_v2_turun)
            p_v2_naik = 1 / ( std_v2_naik * math.sqrt(2 * 22 / 7)) * math.exp(-(( v2 - mean_v2_naik ) ** 2) / ( 2 * var_v2_naik ))
            p_v2_tetap = 1 / ( std_v2_tetap * math.sqrt(2 * 22 / 7)) * math.exp(-(( v2 - mean_v2_tetap ) ** 2) / ( 2 * var_v2_tetap ))
            p_v2_turun = 1 / ( std_v2_turun * math.sqrt(2 * 22 / 7)) * math.exp(-(( v2 - mean_v2_turun ) ** 2) / ( 2 * var_v2_turun ))
        with open('V3.csv') as cf1:
            buka = csv.reader(cf1, delimiter=',')
            for raw in buka:
                V_3.append(raw)
            mean_v3_naik = float(V_3[1][1]) / float(ket[1][0]) 
            var_v3_naik = float(V_3[2][1]) / (float(ket[1][0]) - 1)
            std_v3_naik = math.sqrt(var_v3_naik)
            mean_v3_tetap = float(V_3[1][2]) / float(ket[1][1])
            var_v3_tetap = float(V_3[2][2]) / (float(ket[1][1]) - 1)
            std_v3_tetap = math.sqrt(var_v3_tetap)
            mean_v3_turun = float(V_3[1][3]) / float(ket[1][2])
            var_v3_turun = float(V_3[2][3]) / (float(ket[1][2]) - 1)
            std_v3_turun = math.sqrt(var_v3_turun)
            p_v3_naik = 1 / ( std_v3_naik * math.sqrt(2 * 22 / 7)) * math.exp(-(( v3 - mean_v3_naik ) ** 2) / ( 2 * var_v3_naik ))
            p_v3_tetap = 1 / ( std_v3_tetap * math.sqrt(2 * 22 / 7)) * math.exp(-(( v3 - mean_v3_tetap ) ** 2) / ( 2 * var_v3_tetap ))
            p_v3_turun = 1 / ( std_v3_turun * math.sqrt(2 * 22 / 7)) * math.exp(-(( v3 - mean_v3_turun ) ** 2) / ( 2 * var_v3_turun ))
        ph_naik = p_naik * p_v1_naik * p_v2_naik * p_v3_naik
        ph_tetap = p_v1_tetap * p_tetap * p_v2_tetap * p_v3_tetap
        ph_turun = p_turun * p_v1_turun * p_v2_turun * p_v3_turun
        if ( ph_naik > ph_tetap and ph_naik > ph_turun):
            hasil = 'naik'
        elif (ph_tetap > ph_naik and ph_tetap > ph_turun):
            hasil = 'tetap'
        else:
            hasil = 'turun'
        writer.writerow({'tgl': tgl, 'V1': v1, 'V2': v2, 'V3': v3, 'ket': hasil})
    if (hasil == 'naik'):
        jml = int(ket[1][3]) + 1
        naik = int(ket[1][0]) + 1
        ket[1][3] = jml
        ket[1][0] = naik
        with  open('ket.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for dt in ket:
                writer.writerow(dt)
        jml_naik_v1 = int(V_1[1][1]) + v1
        mean_smntra_v1 = jml_naik_v1 / naik
        var_naik_v1 = float(V_1[2][1]) + (v1 - mean_smntra_v1) ** 2
        V_1[1][1] = jml_naik_v1
        V_1[2][1] = var_naik_v1
        with open('V1.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_1:
                writer.writerow(da)
        jml_naik_v2 = float(V_2[1][1]) + v2
        mean_smntra_v2 = jml_naik_v2 / naik
        var_naik_v2 = float(V_2[2][1]) + (v2 - mean_smntra_v2) ** 2
        V_2[1][1] = jml_naik_v2
        V_2[2][1] = var_naik_v2
        with open('V2.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_2:
                writer.writerow(da)
        jml_naik_v3 = float(V_3[1][1]) + v3
        mean_smntra_v3 = jml_naik_v3 / naik
        var_naik_v3 = float(V_3[2][1]) + (v3 - mean_smntra_v3) ** 2
        V_3[1][1] = jml_naik_v3
        V_3[2][1] = var_naik_v3
        with open('V3.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_3:
                writer.writerow(da)
    elif (hasil == 'tetap'):
        jml = int(ket[1][3]) + 1
        tetap = int(ket[1][1]) + 1
        ket[1][3] = jml
        ket[1][1] = tetap
        with  open('ket.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for dt in ket:
                writer.writerow(dt)
        jml_tetap_v1 = int(V_1[1][2]) + v1
        mean_smntra_v1 = jml_tetap_v1 / tetap
        var_tetap_v1 = float(V_1[2][2]) + (v1 - mean_smntra_v1) ** 2
        V_1[1][2] = jml_tetap_v1
        V_1[2][2] = var_tetap_v1
        with open('V1.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_1:
                writer.writerow(da)
        jml_tetap_v2 = float(V_2[1][2]) + v2
        mean_smntra_v2 = jml_tetap_v2 / tetap
        var_tetap_v2 = float(V_2[2][2]) + (v2 - mean_smntra_v2) ** 2
        V_2[1][2] = jml_tetap_v2
        V_2[2][2] = var_tetap_v2
        with open('V2.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_2:
                writer.writerow(da)
        jml_tetap_v3 = float(V_3[1][2]) + v3
        mean_smntra_v3 = jml_tetap_v3 / tetap
        var_tetap_v3 = float(V_3[2][2]) + (v3 - mean_smntra_v3) ** 2
        V_3[1][2] = jml_tetap_v3
        V_3[2][2] = var_tetap_v3
        with open('V3.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_3:
                writer.writerow(da)
    else:
        jml = int(ket[1][3]) + 1
        turun = int(ket[1][2]) + 1
        ket[1][3] = jml
        ket[1][2] = turun
        with  open('ket.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for dt in ket:
                writer.writerow(dt)
        jml_turun_v1 = int(V_1[1][3]) + v1
        mean_smntra_v1 = jml_turun_v1 / turun
        var_turun_v1 = float(V_1[2][3]) + (v1 - mean_smntra_v1) ** 2
        V_1[1][3] = jml_turun_v1
        V_1[2][3] = var_turun_v1
        with open('V1.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_1:
                writer.writerow(da)
        jml_turun_v2 = float(V_2[1][4]) + v2
        mean_smntra_v2 = jml_turun_v2 / turun
        var_turun_v2 = float(V_2[2][4]) + (v2 - mean_smntra_v2) ** 2
        V_2[1][4] = jml_turun_v2
        V_2[2][4] = var_turun_v2
        with open('V2.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_2:
                writer.writerow(da)
        jml_turun_v3 = float(V_3[1][4]) + v3
        mean_smntra_v3 = jml_turun_v3 / turun
        var_turun_v3 = float(V_3[2][4]) + (v3 - mean_smntra_v3) ** 2
        V_3[1][4] = jml_turun_v3
        V_3[2][4] = var_turun_v3
        with open('V3.csv', mode='w', newline='') as cv:
            writer = csv.writer(cv, delimiter=',')
            for da in V_3:
                writer.writerow(da)
if __name__ == "__main__":
    while True:
        show_menu()