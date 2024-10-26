# Program Face Detection ( Valentino Daniel Kusumo 19624107 )

Program ini menggunakan library OpenCV untuk menggunakan fitur - fitur yang ada didalamnya, seperti VideoCapture, detectMultiScale, dan lain lain yang membantu program ini bekerja dengan baik

Program akan menangkap objek frame by frame untuk mendeteksi wajah seseorang ( lebar, ketinggian, dan lainnya )

Dalam program ini, juga diberikan sebuah box berwarna merah agar mudah dilihat objek yang sedang di*capture*

Kemudian, program ini dapat dihentikan oleh user dengan menekal tombol q ( program akan berhenti total dan kamera akan mati )


## Langkah - langkah 

- Pertama, kita perlu import atau copy file yang sudah dibuat (oleh orang lain) untuk membuat program ini *haarcascade_frontalface_alt2.xml*

- Kemudian, buat file baru dalam folder yang sama dan paste isi file yang telah dicopy tersebut 

- Lalu, membuat sebuah variabel untuk menggunakan kamera, yang kebetulan di program ini menggunakan kamera bawaan laptop

- Kemudian, membuat beberapa function, seperti face_detection, drawer_box, close_window, dan main itu sendiri dimana program akan dijalankan

- Terakhir, program sudah dapat digunakan dengan baik
