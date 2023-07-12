class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        reversed_num = 0
        temp = x
        while temp >= 1:
            reversed_num = reversed_num * 10 + temp % 10
            temp = temp // 10

        return reversed_num == x
