
# Q1

def q1():
    n = 3
    string_res = ''.join([str(x) for x in range(1, n+1)])
    print(string_res)

# Q2

def q2():
    if __name__ == "__main__":

        num_a = input()
        a = input().split(" ")
        num_b = input()
        b = input().split(" ")
        
        track_dict = {}

        all_list = a + b
        
        for char in all_list:
            if char in track_dict:
                track_dict[char] += 1
            else:
                track_dict[char] = 1

        print(len([char for char in track_dict if track_dict[char] == 1]))


# Q3 - Good one

"""
    TASK
    You are given a set  and  number of other sets. These  number of sets have to perform some specific mutation operations on set .

    Your task is to execute those operations and print the sum of elements from set .

    Input Format

    The first line contains the number of elements in set .
    The second line contains the space separated list of elements in set .
    The third line contains integer , the number of other sets.
    The next  lines are divided into  parts containing two lines each.
    The first line of each part contains the space separated entries of the operation name and the length of the other set.
    The second line of each part contains space separated list of elements in the other set.

    Sample Input 

    16
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
    4
    intersection_update 10
    2 3 5 6 8 9 1 4 7 11
    update 2
    55 66
    symmetric_difference_update 5
    22 7 35 62 58
    difference_update 7
    11 22 35 55 58 62 66



"""

def q3():
    from functools import reduce

    if __name__ == "__main__":

        len_a = input()
        a = set(input())
        range_n = int(input())

        action_list = []
        for x in range(range_n):
            action = input().split(" ")[0]
            action_set = set(input().split(" "))
            action_list.append((action, action_set))
            
        for action_tup in action_list:
            func = getattr(a, action_tup[0])
            func(action_tup[1])

        if len(a) != 0:
            print(
                reduce(lambda a, b: int(a)+int(b), a)
            )
        else:
            print(0)


# Q4 - Good one

"""
    Another 'Easy' but Good Probelm: 
    https://www.hackerrank.com/challenges/list-comprehensions/problem

    You are given three integers x, y,and z representing the dimensions of a cuboid
    along with an integer . Print a list of all possible coordinates given by (i,j,k)
    on a 3D grid where the sum of i + j + k  is not equal to 3 Please use list
    comprehensions rather than multiple loops, as a learning exercise.

    0 <= i <= x,
    0 <= j <= y,
    0 <= k <= z


    Example:
    x = 1
    y = 1
    z = 2
    n = 3

    All the possible permuatations of this is 2x2x3 = 12

"""

def q4():
    if __name__ == "__main__":
        x_max = int(input())
        y_max = int(input())
        z_max = int(input())
        n = int(input())


        print(
            [
                [x, y, z] for x in range(x_max+1) for y in range(y_max+1) for z in range(z_max+1)  if sum([x, y, z]) != n
            ]
        )

# Q5 - TODO - See if there's a better way of doing this

def q5():
    if __name__ == "__main__":
        n = input()
        array = input().split(" ")

        unique_array = []
        for val in array:
            if int(val) in unique_array:
                continue
            else:
                unique_array.append(int(val))

        for x in range(len(unique_array)):
            for y in range(len(unique_array)):
                if unique_array[x] < unique_array[y]:
                    curr_val = unique_array[y]
                    unique_array[y] = unique_array[x]
                    unique_array[x] = curr_val

        print(unique_array[-2])
