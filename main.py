def binary_search(list, target, side):
    "binary search that returns the index of the target"
    # initial values
    low_index = 0
    high_index = len(list) - 1
    closest_index = 0
    # boolean to determine if the target is present or not
    found = False

    while low_index <= high_index:
        # find the middle point
        middle = low_index + (high_index - low_index) // 2
        # update closest_index with the new middle
        closest_index = middle
        # target acquired
        if list[middle] == target:
            found = True
            # if there are duplicates then find the right most index
            if side == "right" and middle != len(list) - 1:
                while middle < len(list) - 1 and list[middle] == list[middle + 1]:
                    middle += 1
            # same but find the left most index
            elif side == "left" and middle != 0:
                while middle > 0 and list[middle] == list[middle - 1]:
                    middle -= 1
            # return the left/right most index of the element that matches the target
            return middle
        # updates the boundaries depending on which side of the list to search
        if list[middle] < target:
            low_index = middle + 1
        else:
            high_index = middle - 1
    # if the target is not present then return the index of the next most appropriate value
    if not found:
        if side == "left":
            return if_not_found_lo(list, target, closest_index)
        # if side == "right"
        return if_not_found_hi(list, target, closest_index)


def if_not_found_lo(list, target, closest_index):
    "adjusts the closest index if needed"
    if target < list[0]:
        return 0
    # increments until it finds the next appropriate value to use
    elif list[closest_index] < target:
        while list[closest_index] < target:
            closest_index += 1
    return closest_index


def if_not_found_hi(list, target, closest_index):
    "adjusts the closest index if needed"
    if target > list[len(list) - 1]:
        return len(list) - 1
    # decrements until it finds the next appropriate value to use
    elif list[closest_index] > target:
        while list[closest_index] > target:
            closest_index -= 1
    return closest_index


def calculate_start_to_hi(list, hi):
    "calculates the range if lo is None"
    # binary search for the right most hi index
    hi_index = binary_search(list, hi, "right")
    # extract the range from the start up to the hi index
    extracted_range = list[:hi_index + 1]

    return extracted_range


def calculate_lo_to_end(list, lo):
    "calculates the range if hi is None"
    # binary search for the left most lo index
    lo_index = binary_search(list, lo, "left")
    # extract the range from the lo index to the end of the list
    extracted_range = list[lo_index:]

    return extracted_range


def calculate_lo_to_hi(list, lo, hi):
    "calculates the range if neither lo or hi is None"
    # find the lo and hi indices
    lo_index = binary_search(list, lo, "left")
    hi_index = binary_search(list, hi, "right")
    # extract the range using the indices found above
    extracted_range = list[lo_index:hi_index + 1]

    return extracted_range


def extract(list, lo, hi):
    "extracts a list of elements that fall within a range specified by the lo and high parameters"
    # list to hold the extracted range
    extracted_range = []
    # checks that list is not None
    if list is None:
        return None
    # checks for empty list
    if len(list) == 0:
        return extracted_range
    # returns the list if lo and hi are None
    if lo is None and hi is None:
        return list
    # checks that if lo and hi are not None
    if lo is not None and hi is not None:
        # self explanatory
        if lo > hi:
            return None
        # returns an empty list if both lo and hi are less than the list elements
        if lo < list[0] and hi < list[0]:
            return extracted_range
        # returns an empty list if both lo and hi are greater than the list elements
        if lo > list[len(list) - 1] and hi > list[len(list) - 1]:
            return extracted_range
        # if hi is greater than the last element then treat it as None
        if hi > list[len(list) - 1]:
            extracted_range = calculate_lo_to_end(list, lo)
            return extracted_range
        # if lo is less than the first element then treat it as None
        if lo < list[0]:
            extracted_range = calculate_start_to_hi(list, hi)
            return extracted_range
    # calculates the range from the start to hi if lo is None
    if lo is None:
        if hi is not None and hi < list[0]:
            return extracted_range
        # if hi is out of bounds on the high side then it needs to be treated as None
        if hi is not None and hi > list[len(list) - 1]:
            extracted_range = calculate_lo_to_end(list, 0)
            return extracted_range
        # calcuation for hi is in range
        extracted_range = calculate_start_to_hi(list, hi)
    # calculates the range from lo to the end if hi is None
    elif hi is None:
        if lo is not None and lo < list[0]:
            return list
        # if lo is out of bounds on the high side then return empty list
        if lo is not None and lo > list[len(list) - 1]:
            return extracted_range
        # calculation for lo is in range
        extracted_range = calculate_lo_to_end(list, lo)
    # calculates the range between lo and hi
    else:
        extracted_range = calculate_lo_to_hi(list, lo, hi)

    return extracted_range
