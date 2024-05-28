# litool

**litool** adalah alat sederhana untuk melakukan pemindaian dan injeksi SQL pada sebuah situs web. Alat ini dapat digunakan untuk mengidentifikasi kerentanan keamanan pada aplikasi web yang mungkin rentan terhadap serangan SQL Injection.

## Instalasi

Untuk menggunakan **litool**, Anda perlu mengikuti langkah-langkah instalasi berikut:

1. Pastikan Anda memiliki Python yang terinstal di komputer Anda.
2. Unduh atau salin repositori **litool** ini ke dalam komputer Anda.
3. Buka terminal dan navigasikan ke direktori di mana Anda menyimpan repositori **litool**.
4. Instal dependensi yang diperlukan dengan menjalankan perintah berikut:


## Penggunaan

Anda dapat menggunakan **litool** dengan menjalankan skrip `litool.py` dari terminal dengan argumen yang sesuai. Berikut adalah beberapa contoh penggunaannya:

1. Untuk melakukan pemindaian SQL Injection pada sebuah situs web: python litool.py http://yourweb.com --scan
2. Untuk melakukan injeksi SQL pada sebuah situs web: python litool.py http://yourweb.com --inject


Pastikan untuk mengganti `http://yourweb.com` dengan URL situs web yang ingin Anda uji.

## Kontribusi

Jika Anda ingin berkontribusi pada pengembangan **litool**, Anda dapat melakukan fork repositori ini, membuat perubahan yang diperlukan, dan mengajukan pull request. Kami sangat menghargai setiap kontribusi yang diberikan oleh komunitas.