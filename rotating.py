"""
This looks for an equation of the form 
(x+a)/b = c/(d+x)
that has the same solutions when rotated 180.
It does this by searching all possible values of a, b, c and d.

In the code, the rotated equation is
(x+e)/f = g/(h+x)
where e, f, g and h are rotated by the rotate(n) function.
"""

from numpy.lib.scimath import sqrt

def rotate(n):
    """
    This takes a number n and returns its 'rotated' version, according to my rules about what a rotated number looks like:
    - 1, 5 and 8 are unchanged (for 5 imagine a digital clock!);
    - 6 rotates to 9, and vice versa;
    - 2, 3, 4 and 7 are not rotated meaningfully.
    """
#    if n==1 or n==5 or n==8: # not including 2
    if n==1 or n==5 or n==8 or n==2: # including 2
        return n
    elif n==6:
        return 9
    elif n==9:
        return 6
    else:
        raise ValueError("Number should be 1, 5, 6, 8 or 9")

#candidatevalues = (1,5,6,8,9) # values that can rotate - not including 2
candidatevalues = (1,2,5,6,8,9) # values that can rotate - including 2

# Searches all combinations of candidatevalues looking for matching solutions from the standard and rotated equations.
# Uses SciPy for the square root to deal with any potential complex numbers.
for a in candidatevalues:
    for b in candidatevalues:
        for c in candidatevalues:
            for d in candidatevalues:
                e = rotate(d)
                f = rotate(c)
                g = rotate(b)
                h = rotate(a)
                if (not (a==h and b==g and c==f and d==e)) and (not (a==e and b==f and c==g and d==h)) and b!=1 and c!=1: # only test cases that aren't boring and b and c !=1 so not reducible
                    x1 = (-(d+a) + sqrt((d+a)**2 - 4*(a*d-b*c)))/2 # a,b,c,d +ve
                    x2 = (-(d+a) - sqrt((d+a)**2 - 4*(a*d-b*c)))/2 # a,b,c,d -ve
                    
                    if (d+a) == (h+e) and (d+a)**2 - 4*(a*d-b*c) == (h+e)**2 - 4*(e*h-f*g):
                        print(a,b,c,d," / ",e,f,g,h,"/",x1,x2)
