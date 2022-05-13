## Finding the Largest product in grid

In the below 10x10 grid, three numbers along a horizontal line have been highlighted.

    [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75],
    [49, 49, 99, 40, 17, 81, 18, 57, 60, 87],
    [81, 49, 31, 73, 55, 79, 14, 29, 93, 71], 
    [52, 70, 95, 23, 4, 60, 11, 42, 69, 24],
    [22, 31, 16, 71, 51, 67, 63, 89, 41, 92],
    [24, 47, 32, 60, 99, 3, 45, 2, 44, 75],
    [32, 98, 81, 28, 64, 23, 67, 10, 26, 38],
    [67, 26, 20, 68, 2, 62, 12, 20, 95, 63],
    [24, 55, 58, 5, 66, 73, 99, 26, 97, 17],
    [21, 36, 23, 9, 75, 0, 76, 44, 20, 45]]

The product of these numbers is 4 x 60 x 11 = 2640.

### Questions

1. How many different combinations are there of three adjacent numbers in the same direction (up, down, left, right or diagonally) in
   the 10 x 10 grid?
2. What is the greatest product of three adjacent numbers in the same direction (up, down, left, right or diagonally) in the 10 x 10
   grid?

### Solution:

main.py has two functions:

#### Function 1:

- Name:   get_total_combinations

- Parameters: grid(int[][]) and contiguous integer(integer)

- Returns:

    - 0 if contiguous_integer is greater than grid rows and columns
    - any positive integer value

#### Function 2:

- Name:   find_greatest_product_of_contiguous_integers

- Parameters: grid(int[][]) and contiguous integer(integer)

- Returns:

    - -1 if contiguous_integer is greater than grid rows and columns
    - any positive integer value

#### Execution:

TechConsultingTestGrid.csv is the grid to test on. Above functions are called at the end of the main.py

The Results are:

    Total number of combinations:288
    Largest_product_set: [95, 71, 99]
    Largest product: 667755