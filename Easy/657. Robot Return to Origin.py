class Solution:
    def judgeCircle(self, moves: str) -> bool:
        pos = [0, 0]
        directions =  {'U': 1, 'D': -1, 'L': -1, 'R': 1}

        for move in moves:
            if move == 'U' or move == 'D':
                pos[1] += directions[move]
            else:
                pos[0] += directions[move]
        
        return pos == [0, 0]
        