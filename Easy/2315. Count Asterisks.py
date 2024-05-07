class Solution:
    def countAsterisks(self, s: str) -> int:
        '''
        We are interested in counting asterisks that are not in between a pair
        Asterisks that are outside a pair only occur after even count bars the ones in between occur after the odd count bars
        Hence we keep track of the bar counts and count asterisks that occur after even count bars
        '''
        bar_count, star_count = 0, 0

        for char in s:
            if char == "|":
                bar_count += 1
            if bar_count % 2 == 0: # after even count we are out of pair
                if char == '*':
                    star_count += 1
            
        return star_count


        