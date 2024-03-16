def is_palindrome(s):
    return s == s[::-1]

string = input()
print(is_palindrome(string))