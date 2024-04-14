from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes):
        '''
        Use a hashmap to map group_size -> index for each person in the groupSizes array
        The hashmap contains:
            key: the different group sizes
            value: array containing all indices that belong to a group of that size key
        Once we have that we loop over the different group sizes in the map and construct the different groups
        How:
            1. For each groupSize key, intitialize an empty starting array, curr_list
            2. Add indices that have this group size to this current array
            3. After each add, check if the current array has reached that group size
            4. If yes, add the current starting array to the overal result array and empty the starting array for the next batch
            5. If no, keep adding to the current array
        '''
        groups = defaultdict(list)
        res = []

        for i, size in enumerate(groupSizes):
            groups[size].append(i)
        
        for size in groups.keys():
            curr_list = []
            for idx in groups[size]:
                curr_list.append(idx)
                if len(curr_list) == size:
                    res.append(curr_list)
                    curr_list = []
                    
        return res
