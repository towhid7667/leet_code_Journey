def isPalindrome(s):
    lowerString = s.lower()
    converted_string = ""
    for char in lowerString:
        if char.isalnum():
            converted_string += char
    reversed_string = converted_string[::-1] 
    if converted_string == reversed_string:
        return True
    else:
        return False   
    
isPalindrome("A man, a plan, a canal: Panama")   