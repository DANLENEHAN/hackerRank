
if __name__ == "__main__":

    """

    Once I get a left and right for an index I must stop

    For example take index 4

    Once I get a left which could be 3 and a right which could be 5
    I need to break  and continue.


    So for each index. Create a while loop with an index counter.
    Thew try get a left and right with index plus and minus 1
    once found return and go to next index


    """

    def get_max_index_prod(arr):
        def get_index_product(index, val, list_, max_product):
            if max_product >= ((index) * (len(list_))):
                return 0
            left_index = index - 1
            right_index = index + 1
            left = False
            right = False

            while not left or not right:
                if list_[left_index] > val:
                    left = True

                if list_[right_index] > val:
                    right = True

                if not right:
                    right_index += 1

                if not left:
                    left_index -= 1

                if right_index == len(list_) or left_index == -1:
                    return 0

                if max_product >= ((left_index + 1) * (right_index + 1)):
                    return 0

            right_index += 1
            left_index += 1
            if not left or not right:
                return 0
            else:
                return left_index * right_index

        max_product = 0
        for index in range(len(arr)):
            if index == 0 or index == len(arr) - 1:
                continue
            else:
                curr_index = len(arr) - 1- index
                new_prod = get_index_product(curr_index, arr[curr_index], arr, max_product)
                if max_product < new_prod:
                    max_product = new_prod
                if max_product >= (curr_index -1) * (len(arr)-1):
                    return max_product
        return max_product

    f = open("tempy.txt").read().split(" ")
    print(
        get_max_index_prod(arr=f)
    )