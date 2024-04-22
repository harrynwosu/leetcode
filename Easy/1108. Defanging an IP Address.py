class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = address.replace(".", "[.]")
        return defanged
        