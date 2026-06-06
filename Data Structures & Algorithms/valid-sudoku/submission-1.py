class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        validity = True

        for row in board:
            unique_chars = list(set(row))
            if len(unique_chars) < 9:
                counter = 0
                for item in row:
                    if item == ".": counter+=1
                if counter + len(unique_chars) != 10:
                    return False
                
        for col in range(len(board)):
            column_vals = []
            for row in board:
                column_vals.append(row[col])
            unique_chars = list(set(column_vals))
            if len(unique_chars) < 9:
                counter = 0
                for item in column_vals:
                    if item == ".": counter+=1
                if counter + len(unique_chars) != 10:
                    return False

        map_dict = {
            f"{i},{j}": {
                ".": 0,
                "1": 0,
                "2": 0,
                "3": 0,
                "4": 0,
                "5": 0,
                "6": 0,
                "7": 0,
                "8": 0,
                "9": 0
            } for i in range(3) for j in range(3)
        }

        for row in range(len(board)):
            for col in range(len(board[row])):
                char = board[row][col]
                map_dict[f"{row//3},{col//3}"][char] += 1
        
        # print(map_dict)
        for char_count_dict in map_dict.values():
            for char in range(1,10):
                if char_count_dict[f"{char}"] > 1:
                    return False



        return True


            
