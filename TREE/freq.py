# Problem Statement

# Write a program to count the frequency of each element in an array.

# You are given N integers. Your task is to print each number and its frequency.

# The output should be printed in the order of appearance.

# Input Format
# First line contains integer N
# Second line contains N space-separated integers


n = int(input())
arr = list(map(int, input().split()))

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

for key in freq:
    print(key, freq[key])