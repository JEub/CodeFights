""" Two arrays are called "similar" if one can be
obtained from another by swapping at most one pair
of elements in one of the arrays.

Given two arrays "a" and "b", check whether they are
similar."""

def areSimilar(a, b):
    # get a list of all elements j in a that dont equal their
    # counterpart k in b.
    l = [[j,k] for j,k in zip(a,b) if j!=k]

    # if the list is larger than two pairs then more than 1 swap required
    # if the list is one pair then no swaps can be made
    if len(l)>2 or len(l)==1:
        return False

    # if the list has 0 pairs then they are the same for all elements
    elif len(l)==0:
        return True

    # Otherwise check (j0 = k1) and (j1 = k0)
    # this checks whether the swap makes the arrays the same
    else:
        return l[0][0]==l[1][1] and l[1][0]==l[0][1]
