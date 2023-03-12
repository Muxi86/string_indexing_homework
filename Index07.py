def main(s,n):
    """
    The s string variable is given. n Return the character in the index, otherwise return False.
    Args:
        s(str): parameter
    Returns:
        str: answer
    """
    if len(s)>=n:
        ans = s[n]
    else:
        ans = False
    return ans
print(main("uz",4))