import random

class MinesMap:

    def __init__(self, n, m):
        self._number_of_columns = n
        self._number_of_rows = m
        self._mines_map = [[[False, 0] for i in range(n)] for j in range(m)]

    def CheckAdjacents(self, x, y):
        if (x > 0){
            if 
        }
    
    def BuildMap(self, start_x, start_y):
        for i in range(n):
            for j in range(m):
                is_mine = random.choice([True, False])
                self._mines_map[i][j][0] = is_mine
        self._mines_map[start_x + 1][start_y + 1][0] = False
        for i in range(n):
            for j in range(m):
                
