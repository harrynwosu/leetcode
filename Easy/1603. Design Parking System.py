class ParkingSystem:
    '''
    Use an array to keep track of the number of slots left for each car type
    When a new car is added, decrement its car type count by 1
    '''

    def __init__(self, big: int, medium: int, small: int):
        self.slots = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        if not self.slots[carType - 1]:
            return False
        self.slots[carType - 1] -= 1
        return True
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)