text = "kartik"

arr = list(text)
n = len(arr)

for i in range(n//2):
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

reverse_text = ""

for ch in arr:
    reverse_text = reverse_text + ch

print(reverse_text)
