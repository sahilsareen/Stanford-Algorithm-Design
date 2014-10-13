# owner: ssareen [ Sahil Sareen, Software Engineer, Arista Networks, Bangalore India ]
#                [ sahil.sareen@hotmail.com, sareensah@gmail.com ]
#
# Time Complexity : O(logN)
#  
# Algorithm : Divide and Conquer
# 

def pow_X_n( x, n ):
    # Base Cases
    if n == 0:
        return 1
    if n == 1:
        return x

    # General Case
    pow_X_n_2 = pow_X_n( x, n/2 )
    if n%2 == 0:
        return pow_X_n_2 * pow_X_n_2
    else:
        return pow_X_n_2 * pow_X_n_2 * x

print pow_X_n( 2, 10 )
print pow_X_n( 2, 11 )
