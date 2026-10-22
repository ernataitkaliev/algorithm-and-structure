# Task 13. Reverse a String
def reverse_str(s):
    if len(s) == 0:
        return ""
    return reverse_str(s[1:]) + s[0]

print(reverse_str("algorithm"))
