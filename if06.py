def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    musbat = 0
    if a>0:
        musbat+=1

    if b>0:
        musbat+=1

    if c>0:
        musbat+=1

    manfiy = 0
    if a<0:
        manfiy+=1
    if b<0:
        manfiy+=1
    if c<0:
        manfiy+=1
    if musbat > manfiy:
        return "there are a lot of positive numbers"
    if manfiy > musbat:
        return "there are a lot of negative number"
    return z
print(main(3,3,-6))