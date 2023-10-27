class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_string = s.lower()
        converted_string = ''
        for i in lower_string:
            if i.isalnum():
                converted_string += i
        reverse_string = converted_string[::-1]
        return reverse_string == converted_string
                