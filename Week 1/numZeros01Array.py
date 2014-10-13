# owner: ssareen [ Sahil Sareen, Software Engineer, Arista Networks, Bangalore India ]
#                [ sahil.sareen@hotmail.com, sareensah@gmail.com ]
#
# Time Complexity : O(logN)
#
# Given an array with 1s followed by 0s, count the number of zeros
#

def get1stZeroPos( array, first, last ):
    mid = ( first + last ) / 2
    
    if array[ mid ] == 1:
        return get1stZeroPos( array, mid + 1, last)

    elif array[ mid ] == 0 and array[ mid - 1 ] == 1:
        return mid
    else:
        return get1stZeroPos( array, first, mid - 1 )

def countZeros( array ):
    arrayLen = len( array )

    if arrayLen == 0:
        return 0

    if array[ arrayLen - 1 ] == 1:
        return 0
    elif array[ 0 ] == 0:
        return arrayLen
    else:
        return arrayLen - get1stZeroPos( array, 0, arrayLen - 1 )

array = [1,1,1,1,0,0,0,0]
print countZeros(array )

array = [1,1,1,1,1]
print countZeros(array )

array = [0,0,0,0,0]
print countZeros(array )

array = []
print countZeros(array )
