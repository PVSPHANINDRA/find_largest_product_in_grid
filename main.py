import pandas as pd

"""
Grid size = rows * columns
Adjacent numbers = n
Iterate through all over elements in the grid with window size = x*y where x = min(rows,n) and y = min(columns,n) by incrementing row
and column indexes
We gonna find out the different combination of n adjacent elements in 4 directions:
    a: horizontal
    b: vertical
    c: left-diagonal
    d: right-diagonal

Eg: grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0]]
    n = 2

    For the above grid and n values, the window size is 2*2
    When window is [[1, 2],
                    [6, 8]]

    The horizontal set --> [1, 2], [6, 8]
    The vertical set --> [1, 6], [2, 8]
    The Left Diagonal --> [2, 6]
    The right diagonal --> [1, 8]

Apart from the windows at the end of rows n columns, we only consider the first value of horizontal and vertical
Eg: grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 0],
            [1, 2, 3, 4, 5]]
    n = 2
    
    With the above grid and n,
         window at end of columns are [[4,5], [9,0]] &&  [[9,0],[4,5]]
         window at end of rows are [[6,7], [1,2]] && [[7,8], [2,3]] && [[8,9], [3,4]] && [[9,0], [4,5]]
    
    For the above windows, we consider all horizontal and vertical values(Reason: To avoid, repeated combinations sets)

window_size = n*n does not fit in the grid, then
    1. diagonals are not possible
    2. Only one direction is possible(horizontal or vertical) but not both
Eg: grid = [[1, 2, 3, 4, 5],
            [0, 1, 4, 5, 6]]
    n = 3

    Window_size = 3*3 does not fit, so reducing the windowing size to 2*3.
    With this size, only horizontal value is possible
"""


# Returns total number of combinations for n adjacent numbers in same direction in a grid
def get_total_combinations(grid: any, contiguous_integers: int) -> int:
    n = contiguous_integers
    rows = len(grid)
    columns = len(grid[0])

    # n is greater than rows and columns --> no combination can be made
    # Eg: grid size = 10 * 10 and n = 11
    if n > rows and n > columns:
        print("contiguous integers is exceeding both columns and rows")
        print("No possible combination")
        return 0

    minimum = min(rows, columns)

    # checking window size n*n fits are not with the grid
    # if it does not, only thing is possible(horizontal or vertical) but not both
    if minimum < n:
        return minimum * (max(rows, columns) - (n - 1))

    # sets with all the windows
    #  part_1: 4 * (rows - (n -1)) * (columns - (n -1)) -> represents 4 directions(2 diagonal, 1 horizontal, 1 vertical) of all windows
    #  part_2: (n - 1)* ((rows - (n -1)) + (columns - (n -1))) 
    #     represents all horizontal and vertical directions of windows at the end of row n col
    #     (n-1) -> 1 is subtracted since one direction is covered in part_1 
    return 4 * (rows - (n - 1)) * (columns - (n - 1)) + (n - 1) * ((rows - (n - 1)) + (columns - (n - 1)))


# Returns the greatest product of the grid for n adjacent numbers
# returns -1 if the  contiguous integers size is greater than rows and columns
def find_greatest_product_of_contiguous_integers(grid: any, contiguous_integers: int) -> int:
    n = contiguous_integers
    rows = len(grid)
    columns = len(grid[0])

    # n is greater than rows and columns --> no combination can be made
    # Eg: grid size = 10 * 10 and n = 11
    if n > rows and n > columns:
        print("contiguous integers is exceeding both columns and rows")
        print("No possible combination")
        return -1

    # window
    window_rows = min(n, rows)
    window_columns = min(n, columns)
    is_diagonal_possible = False if min(rows, columns) < n else True

    largest_prod = 0
    largest_prod_arr = []
    counter = 0

    # iterating all elements with window by incrementing row and column indexes
    for i in range(0, rows - (window_rows - 1)):
        for j in range(0, columns - (window_columns - 1)):

            # horizontal_direction
            # if window_column is less than n --> no horizontal direction can be found
            # Eg : [[1,2], [2,5], [3,4]] and n = 3 
            # window size = 3*2
            # horizontal direction is not possible as 3 elements are needed. 
            if window_columns >= n:
                # window at the end of the row --> need to calculate all the horizontal set
                # else only one horizontal set(first one)
                # Why: To avoid duplicate sets
                row_range = window_rows if i == rows - (window_rows - 1) - 1 else 1
                for row_index in range(row_range):
                    counter += 1
                    arr = []
                    prod = 1
                    for col_index in range(window_columns):
                        val = grid[i + row_index][j + col_index]
                        arr.append(val)
                        prod *= val

                    # update
                    if prod > largest_prod:
                        largest_prod = prod
                        largest_prod_arr = arr

            # vertical direction
            # if window_row is less than n --> no vertical direction can be found
            # Eg : [[1,2,3], [2,5,7]] and n = 3 
            # window size = 2*3
            # vertical direction is not possible as 3 elements are needed. 
            if window_rows >= n:
                # window at the end of the row --> need to calculate all the vertical set
                # else only one vertical set(first one)
                # Why: To avoid duplicate sets
                col_range = window_columns if j == columns - (window_columns - 1) - 1 else 1
                for col_index in range(col_range):
                    counter += 1
                    prod = 1
                    arr = []
                    for row_index in range(window_rows):
                        val = grid[i + row_index][j + col_index]
                        arr.append(val)
                        prod *= val

                    # update
                    if prod > largest_prod:
                        largest_prod = prod
                        largest_prod_arr = arr

            # window fits in the grid and its size is n*n
            # diagonals are possible
            if is_diagonal_possible:
                counter += 2
                left_arr = []
                right_arr = []
                left_diagonal_prod = 1
                right_diagonal_prod = 1
                for _index in range(n):
                    left_val = grid[i + _index][j - 1 - _index]
                    right_val = grid[i + _index][j + _index]
                    left_diagonal_prod *= left_val
                    right_diagonal_prod *= right_val
                    left_arr.append(left_val)
                    right_arr.append(right_val)

                # update
                if left_diagonal_prod > largest_prod:
                    largest_prod = left_diagonal_prod
                    largest_prod_arr = left_arr
                if right_diagonal_prod > largest_prod:
                    largest_prod = right_diagonal_prod
                    largest_prod_arr = right_arr

    print("Largest_product_set:", largest_prod_arr)
    # print("Total number of combinations", counter)
    return largest_prod


csv_contents = pd.read_csv('TechConsultingTestGrid.csv', header=None)
grid = csv_contents.values.tolist()
contiguous_integers = 3

combinations = get_total_combinations(grid, contiguous_integers)
print("Total number of combinations:", combinations)

greatest_product = find_greatest_product_of_contiguous_integers(grid, contiguous_integers)
print("Largest product:", greatest_product)
