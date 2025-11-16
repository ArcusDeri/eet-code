# https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1126/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Intuition:
        # Track each condition in its own `set` while
        # iterating the board
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        subs = [[set() for _ in range(3)] for _ in range(3)]

        for row_i in range(len(board)):
            for col_i in range(len(board[0])):
                n = board[row_i][col_i]
                if n == ".":
                    continue

                if (n in rows[row_i] or
                    n in cols[col_i] or
                    n in subs[row_i // 3][col_i // 3]):
                    return False
                rows[row_i].add(n)
                cols[col_i].add(n)
                subs[row_i // 3][col_i // 3].add(n)
        return True
                