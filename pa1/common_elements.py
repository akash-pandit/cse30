def common_elements(list_1: list, list_2: list) -> list:
    """Use a list's length to determine the shorter list to loop through, then loop through that shorter list 
    and check if that number exists within the larger list, appending it to a list to be returned if it is"""
    if len(list_1) <= len(list_2):
        return [num for num in list_1 if num in list_2]
        # for every number in list 1, if that number is also in list 2, add it to a list to be returned
    else:
        return [num for num in list_2 if num in list_1]
        # for every number in list 2, if that number is also in list 1, add it to a list to be returned
    
    # NOTE: It is ambiguous whether lists that have several occurances of the same common element would return every shared occurance, or only return it once.
    # That case will not be tested in the grading. This code will return the former scenario.
    
   
    """Test code:"""
    # assert common_elements([8, 3, 8, 7, 3], [3, 8, 4]) == [3, 8]
    # assert common_elements([2, 5, 4, 1], [5, 3, 6, 2, 4, 10, 11, 15, 9]) == [2, 4, 5]
    # assert common_elements([], []) == []
    # assert common_elements([1, 2, 3], []) == []
    # assert common_elements([], [1, 2, 3]) == []
    # assert common_elements([2, 2, 2], [2, 2]) == [2, 2]  
    # The above test may be false in a different interpretation, where common_elements([2, 2, 2], [2, 2]) would return [2]
