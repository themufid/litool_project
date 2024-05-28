# litool

**litool** adalah alat sederhana untuk melakukan pemindaian dan injeksi SQL pada sebuah situs web. Alat ini dapat digunakan untuk mengidentifikasi kerentanan keamanan pada aplikasi web yang mungkin rentan terhadap serangan SQL Injection.

## Fitur

- **Deteksi Kerentanan SQL Injection**
- **Eksploitasi Otomatis Kerentanan**
- **Menyimpan Hasil Pemindaian ke File Teks dan PDF**

## Instalasi

Untuk menggunakan **litool**, Anda perlu mengikuti langkah-langkah instalasi berikut:

1. Pastikan Anda memiliki Python dan pip yang terinstal di komputer Anda.
2. Unduh atau salin repositori **litool** ini ke dalam komputer Anda.
3. Buka terminal dan navigasikan ke direktori di mana Anda menyimpan repositori **litool**.
4. Instal dependensi yang diperlukan dengan menjalankan perintah berikut: 'pip install requests colorama fpdf'

## Penggunaan

Anda dapat menggunakan **litool** dengan menjalankan skrip `litool.py` dari terminal dengan argumen yang sesuai. Berikut adalah beberapa contoh penggunaannya:

1. Pemindaian Kerentanan
Untuk memindai kerentanan pada URL target, gunakan perintah berikut: python litool.py <target_url> --scan --output <output_file>

contoh: python litool.py http://www.yourweb.com --scan --output hasil_pemindaian

Hasil pemindaian akan disimpan dalam folder results dengan nama file hasil_pemindaian.txt dan hasil_pemindaian.pdf.


2. Eksploitasi Kerentanan
python litool.py http://www.yourweb.tech --inject --output hasil_injeksi


Pastikan untuk mengganti `http://yourweb.com/tech` dengan URL situs web yang ingin Anda uji.

## Kontribusi

Jika Anda ingin berkontribusi pada pengembangan **litool**, Anda dapat melakukan fork repositori ini, terimakasih.