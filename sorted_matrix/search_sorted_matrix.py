def search_in_sorted_matrix(matrix, target):
  # O(r * c) runtime, O(1) space
  # for row in matrix
    # for col in row
      # if matrix[row][col] == target
        # return (row, col) 
  # return (-1, -1)
​
  # O(r log c) ~ O(n log n) runtime, O(1) space
  # binary search on all the elements in a row, starting with 
  # the first row 
  # if our binary search doesn't find the target in that row,
  # move on to the next row 
​
  # O(r + c) runtime, O(1) space
  # how do we take advantage of the fact that both rows are sorted
  # where should we start searching? 
  # would starting at a different corner help? 
  # start at the top right corner
  # init starting indices at the top right corner
  row = 0
  col = len(matrix[0]) - 1
​
  # loop so long as the indices stay in bounds of the matrix 
  while row < len(matrix) and col >= 0:
    # if the current element > target, move left
    if matrix[row][col] > target:
      col -= 1 
    # if the the current element < target, move down
    elif matrix[row][col] < target:
      row += 1
    else:
      return (row, col)
    # we have to start in a corner where moving in one direction 
    # gets us smaller elements, and moving in the other direction gets 
    # us larger elements
  return (-1, -1)
​
  # could we start in the middle? it's not clear how to systematically
  # move through the matrix if we start in the middle 