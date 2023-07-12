class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
    #Dictionary to store roman/int conversions
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    #Variable to store the integer value
        int_value = 0

    #Loop through the string
        for i in range(len(s)):
            #If the current character is less than the next character
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                #Subtract the current character from the next character
                int_value -= roman_to_int[s[i]]
            #Else
            else:
                #Add the current character to the integer value
                int_value += roman_to_int[s[i]]

        return int_value
