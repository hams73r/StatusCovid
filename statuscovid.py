import requests, json, os

def app_label() :
    print('+-----------------------------+')
    print('|       Status COVID-19       |')
    print('|         > Hams73r <         |')
    print('|          v 1.0.0.1          |')
    print('+-----------------------------+')

def app_clear() :
    if os.name == 'nt' : os.system('cls') # Untuk Windows
    else : os.system('clear') # Untuk Linux/OS X

in_menu = 1
usr_pilih = ['','','','','']
url_base = 'https://api.kawalcorona.com/'
url_data = ['positif', 'sembuh', 'meninggal']
val_data = ['', '', '', '', '', '', '']
val_global = []

while in_menu == 1 :
    app_clear()
    app_label()
    val_global = (json.loads((requests.get(url_base)).text))
    for i in range(len(url_data)) :
        val_data[i] = (json.loads((requests.get(url_base + url_data[i])).text))['value']

    print('|        Seluruh Dunia        |')
    print('+-----------------------------+')
    print('Positif   : ' + val_data[0]) # Positif (u_u)
    print('Sembuh    : ' + val_data[1]) # Sembuh (^o^)
    print('Meninggal : ' + val_data[2]) # Meninggal (T~T)
    ##print('Aktif     : %d' % (int(val_data[0])-int(val_data[1])-int(val_data[2]))) # Aktif
    print('+-----------------------------+')
    print('|          Indonesia          |')
    print('+-----------------------------+')
    id_indo = 'Indonesia'
    for i in range(len(val_global)) :
        if str(val_global[i]['attributes']['Country_Region']) == id_indo :
            g_attr = val_global[i]['attributes']
            print('Positif   : ' + str(g_attr['Confirmed'])) # Positif (u_u)
            print('Sembuh    : ' + str(g_attr['Recovered'])) # Sembuh (^o^)
            print('Meninggal : ' + str(g_attr['Deaths'])) # Meninggal (T~T)
            print('Aktif     : ' + str(g_attr['Active'])) # Aktif
            break
        
    print('+-----------------------------+')
    print('|             Menu            |')
    print('+-----------------------------+')
    print('[ 1 ] Cari Provinsi ( ID )')
    print('[ 2 ] Cari Negara ( ALL )')
    print('[ 3 ] Bantuan & Info')
    print('[ 4 ] Refresh')
    print('\n[ 0 ] Keluar')
    print('+-----------------------------+')

    pilih_menu = usr_pilih[0]
    if pilih_menu == '' :
        pilih_menu = str(input('[ > ] '))
        ##usr_pilih = pilih_menu

    app_clear()
    app_label()
    if pilih_menu == '1' :
        val_prov = (json.loads((requests.get(url_base + 'indonesia/provinsi/')).text))
        print('|         Cari Provinsi       |')
        print('+-----------------------------+')
        print('[ 1 ] Masukan Nama Provinsi')
        print('\n[ 0 ] Kembali')
        print('+-----------------------------+')
        
        pilih_menu_prov = usr_pilih[1]
        if pilih_menu_prov == '' :
            pilih_menu_prov = str(input('[ > ] '))
            ##usr_pilih[1] = pilih_menu_prov

        app_clear()
        app_label()
        if pilih_menu_prov == '1' :
            print('|     Masukan Nama Provinsi   |')
            print('+-----------------------------+')
            print('Kosongi untuk menampilkan semua data.')
            print('+-----------------------------+')
            cari_data = str(input('[ > ] '))
            hasil_id = []
            hasil_data = []
            for i in range(len(val_prov)) :
                data_attr = val_prov[i]['attributes']
                if cari_data in (str(data_attr['Provinsi'])).lower() :
                   hasil_id.append(i)
                   hasil_data.append(str(data_attr['Provinsi']))

            app_clear()
            app_label()
            if len(hasil_data) > 0 :
                print('|   Hasil Pencarian Provinsi  |')
                print('+-----------------------------+')
                for i in range(len(hasil_data)) :
                       print('[ %d ] %s' % (i+1, hasil_data[i]))

                print('\n[ 0 ] Kembali ')
                print('+-----------------------------+')
                pilih_data = str(input('[ > ] '))
                if pilih_data.isnumeric() : pilih_data = int(pilih_data) - 1
                else : pilih_data = -1

                if pilih_data >= 0 :
                    app_clear()
                    app_label()
                    print('|       Status Provinsi       |')
                    print('+-----------------------------+')
                    data_attr = val_prov[pilih_data]['attributes']
                    print('Kode Prov  : ' + str(data_attr['Kode_Provi']))
                    print('Provinsi   : ' + str(data_attr['Provinsi']))
                    print('Positif    : ' + str(data_attr['Kasus_Posi'])) # Positif (u_u)
                    print('Sembuh     : ' + str(data_attr['Kasus_Semb'])) # Sembuh (^o^)
                    print('Meninggal  : ' + str(data_attr['Kasus_Meni'])) # Meninggal (T~T)
                    print('\n[ 0 ] Kembali ')
                    print('+-----------------------------+')
                    input('[ > ] ')

            else :
                print('|   Hasil Pencarian Provinsi  |')
                print('+-----------------------------+')
                print('Tidak ditemukan hasil apapun.\nSilahkan masukan kata kunci yang lain.')
                print('\n[ 0 ] Kembali ')
                print('+-----------------------------+')
                input('[ > ] ')
    
    elif pilih_menu == '2' :
        print('|         Cari Negara         |')
        print('+-----------------------------+')
        print('[ 1 ] Masukan Nama Negara')
        print('\n[ 0 ] Kembali')
        print('+-----------------------------+')
        
        pilih_menu_neg = usr_pilih[1]
        if pilih_menu_neg == '' :
            pilih_menu_neg = str(input('[ > ] '))
            ##usr_pilih[1] = pilih_menu_prov

        app_clear()
        app_label()
        if pilih_menu_neg == '1' :
            print('|     Masukan Nama Negara     |')
            print('+-----------------------------+')
            print('Kosongi untuk menampilkan semua data.')
            print('+-----------------------------+')
            cari_data = str(input('[ > ] '))
            hasil_id = []
            hasil_data = []
            for i in range(len(val_global)) :
                data_attr = val_global[i]['attributes']
                if cari_data in (str(data_attr['Country_Region'])).lower() :
                   hasil_id.append(i)
                   hasil_data.append(str(data_attr['Country_Region']))

            app_clear()
            app_label()
            if len(hasil_data) > 0 :
                print('|    Hasil Pencarian Negara   |')
                print('+-----------------------------+')
                for i in range(len(hasil_data)) :
                       print('[ %d ] %s' % (i+1, hasil_data[i]))

                print('\n[ 0 ] Kembali ')
                print('+-----------------------------+')
                pilih_data = str(input('[ > ] '))
                if pilih_data.isnumeric() : pilih_data = int(pilih_data) - 1
                else : pilih_data = -1
               
                if pilih_data >= 0 :
                    app_clear()
                    app_label()
                    print('|        Status Negara        |')
                    print('+-----------------------------+')
                    data_attr = val_global[pilih_data]['attributes']
                    print('Negara    : ' + str(data_attr['Country_Region']))
                    print('Lat, Long : ' + str(data_attr['Lat']) + ', ' + str(data_attr['Long_']))
                    print('Positif   : ' + str(data_attr['Confirmed'])) # Positif (u_u)
                    print('Sembuh    : ' + str(data_attr['Recovered'])) # Sembuh (^o^)
                    print('Meninggal : ' + str(data_attr['Deaths'])) # Meninggal (T~T)
                    print('Aktif     : ' + str(data_attr['Active'])) # Aktif
                    print('\n[ 0 ] Kembali ')
                    print('+-----------------------------+')
                    input('[ > ] ')

            else :
                print('|    Hasil Pencarian Negara   |')
                print('+-----------------------------+')
                print('Tidak ditemukan hasil apapun.\nSilahkan masukan kata kunci yang lain.')
                print('\n[ 0 ] Kembali ')
                print('+-----------------------------+')
                input('[ > ] ')

    elif pilih_menu == '3' :
        print('|       Bantuan & Info        |')
        print('+-----------------------------+')
        print('Sumber Data dan Informasi\nhttps://kawalcorona.com')
        print('+-----------------------------+')
        input('[ < ] Kembali ')
        
    elif pilih_menu == '4' : print()
        
    else :
        print('[] Terimakasih dan Sampai Jumpa []')
        in_menu = 0
