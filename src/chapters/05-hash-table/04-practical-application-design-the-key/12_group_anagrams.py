class Solution(object):
    def partition(self, what, low, high):
        pivot_point = (low + high) // 2
        pivot = what[pivot_point]
        what[high], what[pivot_point] = what[pivot_point], what[high]

        i = low - 1

        for j in range(low, high):
            if what[j] < pivot:
                i += 1
                what[i], what[j] = what[j], what[i]
        
        what[i + 1], what[high] = what[high], what[i + 1]
        return i + 1

    def quick_sort(self, what, low, high):
        if low < high:
            p = self.partition(what, low, high)
            self.quick_sort(what, low, p - 1)
            self.quick_sort(what, p + 1, high)

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            chars = list(s)
            self.quick_sort(chars, 0, len(s) - 1)
            key = ''.join(chars)
            if key in m:
                m[key].append(s)
            else:
                m[key] = [s]

        return list(m.values())
