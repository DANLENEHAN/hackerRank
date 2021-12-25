
"""

Good one here on Prefix sums.

Got a working solution that fails on runtime.
Failed due to actually calulating sum on
every index in the ranges a,b. Rather than using
a prefix/cumulative sum solution:
https://www.thepoorcoder.com/hackerrank-array-manipulation-solution/

n -> size of array
m -> number of operations

arrays always three elements
a, b, k

a-> first index
b-> second index
k-> summand

"""

def my_arrayManipulation(queries):
    res_dict = {}
    sum_func = lambda element: element + k

    max_num = 0
    for query in queries:
        a,b,k = query

        for index in range(a, b+1):
            if index in res_dict:
                res = sum_func(res_dict[index])
            else:
                res = sum_func(0)

            res_dict[index] = res
            if res > max_num:
                max_num = res

    print(res_dict)
    return max_num


def arrayManipulation(queries):
    res_dict = {}

    # cumulative/prefix Sum
    for a,b,k in queries:
        if a in res_dict:
            res_dict[a] += k
        else:
            res_dict[a] = k
        if b in res_dict:
            res_dict[b+1] -= k
        else:
            res_dict[b+1] = -k

    prefix_sum = 0
    max_sum = 0
    for key in sorted(res_dict):
        prefix_sum += res_dict[key]
        print(prefix_sum)
        if prefix_sum > max_sum:
            max_sum = prefix_sum

    print({k:res_dict[k] for k in sorted(res_dict)})
    return max_sum


# Easy
n, m = 5, 3
queries = [[1,2,100],[2,5,100],[3,4,100]]

f = open("input.txt", "r")
data = f.read().split("\n")
f.close()

# Hard
# Expected output 2506721627
# n, m = list(map(int, data[0].split(" ")))
# queries = [list(map(int, line.split(" "))) for line in data[1:]]

print(arrayManipulation(queries))
