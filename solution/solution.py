from typing import List

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        # Get the number of rows and columns in the matrix
        R = len(matrix)
        C = len(matrix[0])
        
        # Initialize an empty dictionary (not used in this code)
        numIdxMap = {}
        
        # Initialize an empty list to store the lucky numbers
        result = []

        # Iterate over each row in the matrix
        for i in range(R):
            row = matrix[i]
            
            # Find the index of the minimum value in the row
            minColIdx = row.index(min(matrix[i]))
            
            # Get the minimum value in the row
            minValInRow = matrix[i][minColIdx]
            
            # Initialize a flag to indicate if the minimum value is a lucky number
            isLuckyNum = True
            
            # Check if the minimum value is the maximum in its column
            for r in range(R):
                if r != i and matrix[r][minColIdx] > minValInRow:
                    # If there's a larger value in the same column, it's not a lucky number
                    isLuckyNum = False
                    break

            # If the minimum value is a lucky number, add it to the result list
            if isLuckyNum:
                result.append(minValInRow)

        # Return the list of lucky numbers
        return result