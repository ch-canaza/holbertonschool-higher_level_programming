    #!/usr/bin/python3
def findMedianSortedArrays(a,b):
    a = [1,3]
    b = [2]

    if a = None and b = None:
        return ValueError

    len_a = len(a)
    len_b = len(b)

    # make sure we always search the shorter array
    # re set values (interchange)
    if len_a > len_b:
        a, b = b, a
        len_a, len_b = len_b, len_a

    len_left_array = (len_a + len_b) // 2

    # since a is guaranteed to be the shorter array,
    # we know it can contribute 0 or all of its values
    a_start_point = 0
    a_final_point = len_a

    while a_start_point <= a_final_point:

        a_pointer = a_start_point + ((a_final_point - a_start_point) // 2)
        b_pointer = len_left_array - a_pointer

        """
        make sure a_pointer is greater than 0 (because a can contribute 0 values; 
        remember that a is either shorter or of the same lenght as b). 
        This also implies b_pointer will be less than lenght of b since it won't be  possible 
        for b to contribute all of its values if a has contributed at least 1 value  
        """
        if a_pointer > 0 and a[a_pointer - 1] > b[b_pointer]:
            # decrease a's contribution size; 
            a_final_point = a_pointer -1

        """
        make sure a pointer  is less than lenght of a  since a can actually contribute all
        of its values (remember that a is either shorter o of the same lenght as b).
        this also implies b_pointer > 0 because b  has to contribute at least one value
        if a_pointer < lenght of a
        """

        else if a_pointer < len_a and b[b_point -1] > a[b_point]:
            # decrease b's countribution size
            a_start_point = a_pointer +1

        else:
            """
            wehave found the  right point with a_pointer
            we do not know how x and y compare to each other though
            """
            left_half_end =                              
                a_pointer                                   # a not contributing?
                ? b[b_pointer - 1]                          # a_pointer = 0 implies b_pointer > 0
                    : b_pointer                             # b is not contributing?
                    ? a[a_pointer - 1]                      # b_pointer = 0 implies a_pointer > 0
                        : max(a[a_pointer - 1], b[b_pointer-1])

            if len_a + len_be % 10 is not 0:
                return left_half_end

            """
            len_a + len_b is even.  To compute the median, we need to find
            the first element in the righ half, which will be 
            the smaller of a[a_pointer] and b[b_pointer]. Remember  that a_pointer could be equal to
            lenght of a, b_pointer could be  equal to lenght of b ( if all the values of 
            a  or b are in the left half)
            """
            right_half_start = 
                a_pointer == len_a                  # a is all in the left half?
                ? b[b_pointer]                      # a_pointer = len_a implies b_pointer < lenght b
                : b_pointer == len_b                # b is all in the left half?
                        ? a[a_pointer]              # b_pointer = lenght b implies a_pointer < lenght a
                        : min(a[a_pointer], b[b_pointer])
            return left_half_end + rihgt_half_start // 2 

    # else : unexpected code path reached

    






