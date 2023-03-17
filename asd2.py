def fibonacciSearch(arr, x):
    """
    Fungsi Fibonacci Search yang mengembalikan indeks dari elemen x pada array arr,
    atau -1 jika x tidak ada di arr.
    """
    n = len(arr)
    fib2 = 0  # fibonacci(n-2)
    fib1 = 1  # fibonacci(n-1)
    fib = fib2 + fib1  # fibonacci👎
  
    # Cari nilai dari fibonacci(n) yang terbesar yang lebih kecil atau sama dengan n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
  
    # Indeks awal untuk pencarian
    offset = -1
  
    # Melakukan pencarian
    while fib > 1:
        i = min(offset+fib2, n-1)
  
        # Jika x lebih besar daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kanan
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
  
        # Jika x lebih kecil daripada nilai elemen pada indeks i, lakukan pencarian pada subarray kiri
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
  
        # Jika x ditemukan, kembalikan indeks i
        else:
            return i
  
    # Jika elemen tidak ditemukan, kembalikan -1
    if fib1 and arr[offset+1] == x:
        return offset+1
  
    # Jika elemen tidak ditemukan, kembalikan -1
    return -1


print(fibonacciSearch([3,7,11,20,27,46,62,81,94],4))