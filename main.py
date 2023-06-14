def check_brackets(string):
    stack = []
    for i, char in enumerate(string):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if not stack or not is_matching_bracket(stack.pop()[0], char):
                return i
    if stack:
        return stack.pop()[1]
    return -1


def is_matching_bracket(open_bracket, close_bracket):
    return open_bracket == "(" and close_bracket == ")" or \
        open_bracket == "[" and close_bracket == "]" or \
        open_bracket == "{" and close_bracket == "}"


if __name__ == "__main__":
    brackets = ["[{()}]", "{[]}", "(})[{]"]

    for bracket in brackets:
        invalid_index = check_brackets(bracket)
        if invalid_index == -1:
            print("All brackets are valid.")
        else:
            print(f"Invalid bracket found at index:", invalid_index)
