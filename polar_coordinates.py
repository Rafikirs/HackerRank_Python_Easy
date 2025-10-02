# Exercise: Polar Coordinates
# URL: https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
# Description: Working with complex numbers 

import cmath
z = input()

if z[0] == '-':
    if '-' in z[1:]:
        second_pos = z[1:].index('-')
        a = "-" + z[1:second_pos+1]
        b = "-" + z[second_pos+2:-1]
    else:
        second_pos = z.index('+')
        a = '-' + z[1:second_pos]
        b = z[second_pos+1:-1]
else:
    if '-' in z:
        second_pos = z.index('-')
        a = z[:second_pos]
        b = "-" + z[second_pos+1:-1]
    else:
        second_pos = z.index('+')
        a = z[:second_pos]
        b = z[second_pos+1:-1]

a = int(a) 
b = int(b)       

print(abs(complex(a, b)))
print(cmath.phase(complex(a, b)))
