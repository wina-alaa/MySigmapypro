meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "SHEESH": "Sedikit Ketidaksetujuan",
            "CREEPY": "Menakutkan, tidak menyenangkan",
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print (meme_dict[word])
else:
    print ("MAAF KATA TERSEBUT TIDAK TERSEDIA")
