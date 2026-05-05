# #
# Code
# Testcase
# Testcase
# Test Result
# Test Result
# Note
# 136. Single Number
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

numbs = [2,1,3,2,9]
for i in numbs : 
     if numbs.count(i) == 1 :
         print(i)
         break 
     
     