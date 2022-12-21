# import libraries
from collections import defaultdict
from typing import Counter

# creating an empty list
lst = []

# number of elements as input
n = int(input("Enter number of elements: "))

# iterating till the range
for i in range(0, n):
    ele = int(input("Enter elements {}: ".format(i)))
    
    lst.append(ele) # adding the element

print("\n")

# count function
def sockPairs(n, lst):
    pairs = 0
    count = defaultdict(int)

    for item in lst:
        count[item] += 1

    for k,v in count.items():
        pairs += v // 2

    return pairs

print("Output: ")
print(sockPairs(n, lst))