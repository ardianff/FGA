kal = input('Masukkan Kalimatnya : ')
kalimat = kal.lower()
konversi = kalimat \
  .replace('satu', '1') \
  .replace('dua', '2') \
  .replace('tiga', '3') \
  .replace('empat', '4') \
  .replace('lima', '5') \
  .replace('enam', '6') \
  .replace('tujuh', '7') \
  .replace('delapan', '8') \
  .replace('sembilan', '9') \
  .replace('sepuluh', '10') \
  .replace('ditambah', '+') \
  .replace('dikurangi', '-') \
  .replace('dikali', '*') \
  .replace('dibagi', '/')
hasil = eval(konversi)
print(konversi,'=',hasil)