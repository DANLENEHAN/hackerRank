
def is_balanced(mapper, string):

    stack = []
    lefts = ["{", "(", "["]

    if string[0] not in lefts:
        return False

    for char in string:

        if char in lefts:
            stack.append(char)
        elif char not in lefts:
            try:
                top = stack.pop()
            except:
                return False
            if mapper[top] != char:
                return False

    if stack != []:
        return False

    return True


if __name__ == "__main__":

    string = "()()[()([{[()][]{}(){()({[]}[(((){(())}))]()){}}}])]"
    mapper = {
        "{": "}",
        "[": "]",
        "(": ")"
    }

    print(is_balanced(mapper=mapper, string=string))