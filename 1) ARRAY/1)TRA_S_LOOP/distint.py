arr = [2, 3, 2, 5, 3]

freq = {}

for i in range(len(arr)):
    if arr[i] not in freq:
        freq[arr[i]] = 1

distinct_count = len(freq)

print(distinct_count)
