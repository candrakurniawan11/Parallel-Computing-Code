
from multiprocessing import Process, Queue

# Fungsi untuk menghitung jumlah sebagian (partial sum)
def partial_sum(start, end, q, pid):
    s = sum(range(start, end + 1))
    print(f"Process {pid}: sum({start} to {end}) = {s}")
    q.put(s) # Masukkan hasil ke dalam antrean (Queue)

if __name__ == "__main__":
    # VERSI SERIAL
    print("Menjalankan Versi Serial")
    n = 5
    total_serial = 0
    for i in range(1, n+1):
        total_serial += i
        print(f"step {i}: total = {total_serial}")
    print("Final Serial sum is", total_serial)
    
    print("\n Menjalankan Versi Paralel ")
    # VERSI PARALEL 
    q = Queue() # Membuat antrean untuk menyimpan hasil dari setiap proses
    
    # Membagi tugas penjumlahan dari 1-5 menjadi dua proses
    p1 = Process(target=partial_sum, args=(1, 3, q, 1)) # Proses 1: jumlahkan 1 sampai 3
    p2 = Process(target=partial_sum, args=(4, 5, q, 2)) # Proses 2: jumlahkan 4 sampai 5
    
    # Memulai eksekusi proses
    p1.start()
    p2.start()
    
    # Menunggu kedua proses selesai sebelum lanjut ke baris berikutnya
    p1.join()
    p2.join()
    
    # Mengambil dua hasil yang dimasukkan oleh p1 dan p2 ke dalam antrean, lalu menjumlahkannya
    total_parallel = q.get() + q.get()
    print("Final Parallel Sum =", total_parallel)