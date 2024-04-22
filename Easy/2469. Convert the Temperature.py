from typing import List

class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        '''
        Regular temperature conversions
        Use the given formulas and return array of results.
        '''
        kelvin = celsius + 273.15
        farenheit = celsius * 1.80 + 32

        return [kelvin, farenheit]
        