# import libraries
from collections import defaultdict

# input and change to list
lst = list(map(int, input("Enter the numbers: ").split()))

# count length of the list
n = len(lst)

# count function
def sockPairs(n, lst):
    pairs = 0
    count = defaultdict(int)

    for item in lst:
        count[item] += 1

    for k,v in count.items():
        pairs += v // 2

    return pairs

# output
print("Output: ",sockPairs(n, lst))