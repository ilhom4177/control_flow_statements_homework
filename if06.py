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
    positive = 0
    negative = 0
  
    if a > 0:
        positive +=1
    else:
        negative +=1
    if b > 0:
        positive +=1
    else:
        negative +=1
    if c > 0:
        positive +=1
    else:
        negative +=1
    return "there are a lot of positive numbers"
    return "there are a lot of negative numbers"
print(main(1,2,4))