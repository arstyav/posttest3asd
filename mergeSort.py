def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        left_data = data[:mid]
        right_data = data[mid:]

        print(f"kiri: {left_data}")
        print(f"kanan: {right_data}")

        print(20*'=')

        mergeSort(left_data)
        mergeSort(right_data)

data = [2, 8, 10, 7, 5, 1, 3]
mergeSort(data)