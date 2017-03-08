def find_max_min(my_list):

    max_no = max (my_list)
    # maximum number
    min_no = min (my_list)
    # minimum number

    if min_no == max_no:
    # If they are equal, return a one element array as test requires
        return [min_no]
    else:
        return [min_no, max_no]
