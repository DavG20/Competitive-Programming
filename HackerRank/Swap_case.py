def swap_case(s):
    ans=""
    for chrs in s:
        if chrs.isupper():
            ans+=chrs.lower()
        else:
            ans+=chrs.upper()
    return ans

