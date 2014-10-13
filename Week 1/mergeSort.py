# owner: ssareen [ Sahil Sareen, Software Engineer, Arista Networks, Bangalore India ]
#                [ sahil.sareen@hotmail.com, sareensah@gmail.com ]
#
# Time Complexity : O(NlogN)
# Space Complexity : O(N)
#
# Algorithm : Divide and Conquer
#

def mergeSort( array, first, last ):
    
    # Recurssion
    mid = ( first + last ) / 2
    if first < last :
        mergeSort( array, first, mid )
        mergeSort( array, mid + 1, last )
    
    # Now first half and second half is individually sorted in Ascending Order
    # Merge both halves to get fully sorted array
    # Keep picking up the smaller front element from each sorted portion
    temp = [ None ] * ( last - first + 1 )
    firstHalfFront = first
    secondHalfFront = mid + 1
    pos = 0

    while firstHalfFront <= mid and secondHalfFront <= last:
        if array[ firstHalfFront ] < array[ secondHalfFront ]:
            temp[ pos ] = array[ firstHalfFront ]
            firstHalfFront += 1
        else:
            temp[ pos ] = array[ secondHalfFront ]
            secondHalfFront += 1
        pos += 1
    
    if firstHalfFront <= mid:
        temp[ pos : ] = array[ firstHalfFront : mid + 1 ]
    else:
        temp[ pos : ] = array[ secondHalfFront : last + 1 ]
    
    pos = 0
    while first <= last:
        array[ first ] = temp[ pos ]
        first += 1
        pos += 1


array =  [1,3,5,2,0,99,23,51]
mergeSort( array, 0, len(array)-1 )
for i in array:
    print i
