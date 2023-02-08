def num_of_zeros(grid: list) -> int:
    """Counts the number of zeroes by counting every time 0 appears in each row 
       using the .count() method"""
    count = 0  # initializing count variable
    for list_ in grid:  # looping through every row in the grid
        count += list_.count(0)  # for each row in the grid, the amount of times 0 occurs is added to variable count
    return count  # after all rows are looped through, the total count of 0s is returned
    
    """Test Code:"""
    # assert num_of_zeros([[1,1,1,0],[1,1,1,0],[1,1,0,0],[0,0,0,0]]) == 8
    # assert num_of_zeros([[1, 1],[1, 1]]) == 0
    # assert num_of_zeros([[],[]]) == 0
    # assert num_of_zeros([[], [0, 0, 1]]) == 2
