# https://leetcode.com/problems/fizz-buzz/
# uncommon but fast
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # Idea: Loop four times over the result array.
        # Handle single requirement in each loop.
        # A bit counterintuitive but beats all other solutions
        # in terms of speed.

        # Allocate
        result = [ "" ] * n

        # fill in "1", "2"...
        for i in range(0, n):
            result[i] = str(i + 1)

        # "Fizz" on every third
        for i in range(2, n, 3):
            result[i] = "Fizz"

        # "Buzz" on every fifth
        for i in range(4, n, 5):
            result[i] = "Buzz"

        # "FizzBuzz" when number is divisible by both
        # 3 and 5 so it must be divisible by 15. Then
        # every 15th is "FizzBuzz"
        for i in range(14, n, 15):
            result[i] = "FizzBuzz"
    
        return result
