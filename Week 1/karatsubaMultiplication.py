# owner: ssareen [ Sahil Sareen, Software Engineer, Arista Networks, Bangalore India ]
#                [ sahil.sareen@hotmail.com, sareensah@gmail.com ]
#
# Standard Multiplication ( Two 'n' bit numbers) : O( n^2 )
# Karatsuba Multiplication ( Two 'n' bit numbers) : O( n^1.59 )
# Algo: Divide and Conquer
# Break the numbers into two halves, Multiply, Add
# num1 x num2 
# num1 = num1R * 2^(n/2) + num1L
# num2 = num2R * 2^(n/2) + num2L
# num1 x num2 = ( num1R * 2^(n/2) + num1L ) x ( num2R * 2^(n/2) + num2L )
#             = [ num1R x num2R ] x 2^(n) + [ num1R x num2L + num2R x num1L  ] x 2^(n/2) + num1L x num2L
#     T(n)    =       T(n/2)              +      T(n/2)     +   T(n/2)                   +   T (n/2)     + O(n)  
#             =       4T(n/2) + O(n)  = O(n^2) [ NO GAIN! ]
# ----
# num1 x num2 = ( num1R * 2^(n/2) + num1L ) x ( num2R * 2^(n/2) + num2L )
#             = [ num1R x num2R ] x 2^(n) + [ num1R x num2L + num2R x num1L  ] x 2^(n/2) + num1L x num2L
#                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             =  productTerm1             +              ....                            + productTerm2      
# num1R x num2L + num2R x num1L = ( num1R + num1L ) x ( num2R + num2L ) - [ num1R x num2R + num1L x num2L ]
#                                 [ New computation: productTerm3     ] - [ Already computed: productTerm1 + productTerm2 ]
#     T(n)    =       3T(n/2) + O(n)
#             =       O(n^1.59)      < O(n^2) 
#

from math import ceil

def makeEqualLength( num1, num2 ):
    maxLength = max( len( num1 ), len( num2 ) )
    num1 = num1.rjust( maxLength, '0' )
    num2 = num2.rjust( maxLength, '0' )
    return ( num1, num2, maxLength )

def splitIntoHalves( num, numLen ):
    return ( num[ numLen/2 : ], num[ 0 : numLen/2 ] )

def multiply( num1, num2 ):
    ( num1, num2, numLen ) = makeEqualLength( num1, num2 )

    # Base Cases
    if numLen == 0:
        return 0
    if numLen == 1:
        return int( num1 ) * int( num2 )
    
    # General Case numLen > 1
    ( num1L, num1R ) = splitIntoHalves( num1, numLen )
    ( num2L, num2R ) = splitIntoHalves( num2, numLen )
    
    productTerm1 = multiply( num1R, num2R )
    productTerm2 = multiply( num1L, num2L )
    productTerm3 = multiply( bin( int( num1R, 2 ) + int( num1L, 2 ) )[2:], bin( int( num2R, 2 ) + int( num2L, 2 ) )[2:] )

    return productTerm1 * ( 1 << numLen ) + productTerm2 + ( productTerm3 - ( productTerm1 + productTerm2 ) ) * ( 1 << int( ceil( numLen/2.0 ) ) )

num1 = '11'
num2 = '100'
product =  multiply( num1, num2 )
print int(num1,2),'x',int(num2,2),'=' ,product
