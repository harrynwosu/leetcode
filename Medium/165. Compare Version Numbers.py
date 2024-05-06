class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        Split the two strings by full stops, converting each partition to an into to get rid of leading zeros
        If both are equal immediately return 0
        Otherwise, use two pointers to scan the arrays.
        If at any point, v1[i] < v2[j] return -1 as version 1 is less
        Else if v2[j] < v1[i]] return i as version 2 is less
        After this while loop, it's possible to have leftover element in one array in the case that array is longer.
        If we have leftovers in v1 and the leftovers are not all zeros, return 1 as version 2 is less
        If we have leftovers in v2 and they are not all zeros, return -1 as version 1 is less
        Return 0 otherwise (presence of only trailing zeros that just makes the longer one equal to the shorter one anyway)
        '''
        v1 = [int(rev) for rev in version1.split(".")]
        v2 = [int(rev) for rev in version2.split(".")]

        if v1 == v2:
            return 0
        
        i, j = 0, 0

        while i < len(v1) and j < len(v2):
            if v1[i] == v2[j]:
                i += 1
                j += 1
            elif v1[i] < v2[j]:
                return -1
            else:
                return 1

        if i < len(v1) and any(i != 0 for i in v1[i:]):
            return 1
        
        if j < len(v2) and any(j != 0 for j in v2[j:]):
            return -1
        
        return 0
