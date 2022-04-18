"""
Probelm Description (HackerRank)

If you've to rename a given filename e.g. "ababa"
to a new name e.g. "aba" but you can only delete
characters. How many different ways could you
do this. 

"""


def find_substrings(new_name, old_name, curr_str=""):

    if len(curr_str) == len(new_name):
        return [curr_str]

    substrings = []
    for idx, char in enumerate(old_name):
        curr_str += char
        if (
            len(curr_str) <= len(new_name)
            and curr_str[-1] == new_name[len(curr_str) - 1]
        ):
            substrings += find_substrings(
                new_name=new_name, old_name=old_name[idx + 1 :], curr_str=curr_str
            )
        curr_str = curr_str[:-1]
    return substrings


print(find_substrings(new_name="aba", old_name="ababa"))
