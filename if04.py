def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    
    k=0
    if a>0:
        k+=1
    if b>0:
        k+=1
    if c>0:
        k+=1

    return k
print(main(3,-3,-6)) 