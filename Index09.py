def main(s):
    """
    a single character string is given. Convert it to int type, return -1 if not possible.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    if s.isdigit():
        ans = s
    else:
        ans = -1
    return ans
print(main('k'))