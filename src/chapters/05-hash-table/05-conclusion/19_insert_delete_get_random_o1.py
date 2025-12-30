# https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1141/
class RandomizedSet(object):

    # Intuition:
    # Use hash map and a list.
    # Hash map maps a value to index in the list.
    # `getRandom` returns a random element from the list.
    # The trick is to substitute an element to be removed
    # from the list with the last element from the list
    # and to update the hash map accordingly.
    def __init__(self):
        self.val_map = {}
        self.val_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val not in self.val_map
        if res:
            self.val_map[val] = len(self.val_list)
            self.val_list.append(val)
        return res

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        res = val in self.val_map
        if res:
            idx = self.val_map[val]
            last_val = self.val_list[-1]
            self.val_list[idx] = last_val
            self.val_list.pop()
            self.val_map[last_val] = idx
            del self.val_map[val]
        return res

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.val_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()