def main(s):
    """
    Given a variable s string of length five. Determine the number of digits involved in this variable.
    Args:
        s(str): parameter
    Returns:
        int: answer
    """
    ans = 0
    idx = 0
    if s[idx].isdigit():
        ans+=1
    idx+=1
    if s[idx].isdigit():
        ans+=1
    idx+=1
    if s[idx].isdigit():
        ans+=1
    idx+=1
    if s[idx].isdigit():
        ans+=1
    idx+=1
    if s[idx].isdigit():
        ans+=1
    idx+=1
    return ans
print(main('12340'))