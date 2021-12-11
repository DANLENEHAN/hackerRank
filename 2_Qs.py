

arr = [1, 2, 3, 4, 5]

# Once you get halfway through the list
# you'll be undoing your previous swaps
for i in range(round(len(arr)/2)):
    holder = arr[len(arr)-i-1]
    arr[len(arr)-i-1] = arr[i]
    arr[i] = holder

print(arr)


"""

Question:
https://www.hackerrank.com/challenges/dynamic-array/problem?isFullScreen=true

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    arr = []

    get_index = lambda  x, la, n: (x^la) % n
    
    last_answers = [0]

    for op in queries:
        query, x, y = op
        idx = get_index(x, last_answers[-1], n)
 
        if query == 1:
            if len(arr) - 1 >= idx:
                arr[idx].append(y)
            else:
                arr.append([y])
        elif query == 2:
            last_answers.append(
                arr[idx][y%len(arr[idx])]
            )
    return last_answers[1:]

# Write your code here

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    arr = {}

    get_index = lambda  x, la, n: (x^la) % n
    
    last_answers = [0]

    for op in queries:
        query, x, y = op
        idx = get_index(x, last_answers[-1], n)
 
        if query == 1:
            if idx in arr:
                arr[idx].append(y)
            else:
                arr[idx] = [y]
        elif query == 2:
            last_answers.append(
                arr[idx][y%len(arr[idx])]
            )
    return last_answers[1:]


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    
    arr = {}

    get_index = lambda  x, la, n: (x^la) % n
    
    last_answers = [0]

    for op in queries:
        query, x, y = op
        idx = get_index(x, last_answers[-1], n)
 
        if query == 1:
            if idx in arr:
                arr[idx].append(y)
            else:
                arr[idx] = [y]
        elif query == 2:
            last_answers.append(
                arr[idx][y%len(arr[idx])]
            )
    return last_answers[1:]


    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
