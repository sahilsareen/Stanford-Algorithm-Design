# owner: ssareen [ Sahil Sareen, Software Engineer, Arista Networks, Bangalore India ]
#                [ sahil.sareen@hotmail.com, sareensah@gmail.com ]
#
# Time Complexity : O(N^2)
#
# Count the number of inversions in an array
# Inversion Count : How far[ Swaps? ] is the array from being sorted?
# Solution1: Do bubble sort and count the number of swaps
# 
# [2, 4, 1, 3, 5]
# Swapping  1  and  2
# Swapping  2  and  4
# Swapping  3  and  4
# [1, 2, 3, 4, 5]
# Inversion Count :  3
#
# Solution2: Count the number of elements that 
# are to the right and smaller than the current element
# Why this works?: Start from the last element and by logic similar to insertion sort 
# count the number of swaps needed to place the 'next element' in place 
# This is equal to the number of elements to the right smaller than the 'next element'
# (4), [1,3,5] : two elements smaller than 4 : Swaps = 2
# Swap(4,1) => [1,4,3,5] => Swap(4,3) => [1.3.4.5]
# (2) [1,3,4,5] or (2) [4,1,3,5] : one elements smaller than 1 : Swaps = 1
# This is because only elements smaller than (2) need to be swapped and one swap per element
# Swap(2,1) => [1,2,3,4,5]
#
#

# Solution1
def bubbleSortSwapsCount( array ):
    arrayLen = len( array )
    inversionCount = 0
    for i in xrange( 0, arrayLen ):
        for j in xrange( i, arrayLen ):
            if array[ i ] > array[ j ]:
                array[ j ], array[ i ] = array[ i ], array[ j ]
                inversionCount += 1
                print "Swapping ", array[ i ], " and ", array[ j ]
    return inversionCount

# Solution2
def insertionSortSwapsCount( array ):
    arrayLen = len( array )
    inversionCount = 0
    for i in xrange( arrayLen-1, -1, -1 ):
        for j in xrange( i, arrayLen ):
            if array[ i ] > array[ j ]:
                inversionCount += 1
                print "Counting for ", array[ i ], " and ", array[ j ]
    return inversionCount

array = [ 2, 4, 1, 3, 5 ]
print array
inversionCount = insertionSortSwapsCount( array )
# Advantage : array is not modified
print array
print "Inversion Count( InsertionSort Logic ) : ", inversionCount

inversionCount = bubbleSortSwapsCount( array )
print array
print "Inversion Count( BubbleSort Logic ) : ", inversionCount

