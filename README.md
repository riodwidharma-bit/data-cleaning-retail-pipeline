Retail Sales Data Cleaning Dan Preprocessing Pipeline

Project Overview
Prooyek ini bertujuan membangung pipeline pembersihan data (data cleaning pipeline) otomatis menggunakan python dan pandas untuk mengolah dataset transaksi retail sales mentah sebanyak 12,500+ baris data.Pipeline ini menangani berbagai masalah dari data kotor seperti missing value, format tipe data yang salah, serta ketidakseraagaman teks agar dataset siap dimasukn ke dalam database SQL atau sistem analitik.

Tech Stack Dan Tools
- Language          : Python 3.0.0
- Library           : Pandas
- Version Control   : Git dan Github

Key Cleaning Steps
Berikut adalah manipulasi data yang dilakukan dalam pipeline:
1.  Handling Missing Values ('NaN) :
    - Kolom 'Item' diisi dengan label default 'Unknown'.
    - Kolom 'Discount Applied' Diisi dengan boolean 'False'.
    - Kolom 'Price Per Unit' dan 'Quantity' diisi mengunakan nilai Median agar tidak terdistorsi oleh oulier.
    - Kolom 'Total Spent' dihitung secara presisi dari hasil kalkulasi 'Price Per Unit * Quantity'.
2.  Type Casting Dan Formatting    :
    - Menilai ulang kolom 'Transaction Date' dari 'string' menjadi tipe 'datetime64'.
    - Konversi kolom 'Quantity' dari 'float' menjadi 'integer'.
3.  String Standardization         :
    - Menghapus spasi yang berantakan dengan '.str.strip()' dan menerapkan kapitalisasi pada kolom teks ('Category', 'Location', 'Payment Method', Dll.).
4.  Deduplication                  :
    -Menghapus seluruh baris data duplikat menggunakan 'drop_duplicates()'.

SQL Database Dan Data Ingestion :
Dataset yang sudah bersih diimpor secara otomatis ke database SQLite ('retail_database.db) menggunakan 'load_to_sql.py'.

Sample Analysis Queries ('analisis_query.py') :
1.  Revenue Per Category : Menghitung total pendapatan dan transaksi berdasarkan kategori produk.
2.  Location Insight     : Menganalisis metode pembayaran yang paling sering digunakan disetiap lokasi.

How To Run
1.  Clone repository ini :
    '''bash
    git clone [https://github.com/username/data-cleaning-retail-pipeline.git](https://github.com/username/data-cleaning-retail-pipeline.git)
    cd data-cleaning-retail-pipeline