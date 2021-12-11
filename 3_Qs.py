
def get_shift_index(shift, index, len_arr):
    """
    If shift is a minus value we shift left
    if it's a plus value we shift right.

    First step is to remove a full array
    circle, meaning get the remainder of
    the absolute shift, divided by array length.

    Once we've got that we have that number we
    have the actual number of movements within the
    array we can do to get the destination index.
    Without fully passing through the array. 

    Add our current index to this number of movements.
    If movements is minus (meaning left shift) we're
    fine and don't need to manipulate this result as
    we'll always be able to index [len(arr)-1 - len(arr)-1]
    If it's a plus number though it could be as high as
    len(arr)-1 + len(arr) -1. Meaning we should subtract 
    len(arr) from this number to get the actual index.
    """


    movements = abs(shift) % len_arr

    # If we've just done shift/len_arr movements
    # I.E we're in the same place
    if movements == 0:
        return index

    if shift < 0:
        return index - movements
    elif shift > 0:
        new_index = index + movements
        return (
            new_index if new_index < len_arr else new_index - len_arr
        )

def q1():
    """
    Shift an array. Minus
    value to shift left and
    a plus value for right
    """

    arr = [1, 2, 3, 4, 5]
    shift = -4

    new_arr = [0]*len(arr)
    for index in range(len(arr)):
        new_arr[
            get_shift_index(
                index=index,
                shift=shift,
                len_arr=len(arr)
            )
        ] = arr[index]

    print(
        new_arr
    )


def q2(string, sub_string):
    """
    Find count of occurances of a
    substring in a string
    """
    len_substring = len(sub_string)

    string_dict = {}
    for x in range(len(string)):

        curr_str = string[x:x+len_substring]

        if curr_str in string_dict:
            string_dict[curr_str] += 1
        else:
            string_dict[curr_str] = 1

    return string_dict.get(sub_string, 0)



def q3(strings, queries):
    """
    """

    occurance_dict = {}

    for string in strings:
        if string in occurance_dict:
            occurance_dict[string] += 1
        else:
            occurance_dict[string] = 1

    print(occurance_dict)

    return [
        occurance_dict.get(query, 0) for query in queries
    ]


if __name__ == "__main__":

    strings = ['aba', 'baba', 'aba', 'xzxb']
    queries = ['aba', 'xzxb', 'ab']
    strings = ['def', 'de', 'fgh']
    queries = ['de', 'lmn' , 'fgh']
    print(q3(strings=strings, queries=queries))
    # q2("I am an Indian, by birth.", "Birth")
    # q1()



    n = 3
