def est_palindrome(mot):
    # Stopping condition: an empty word or a word with only one character
    if len(mot) <= 1:
        return True
    
    # Initialize pointers for the beginning and end of the word
    debut = 0
    fin = len(mot) - 1
    
    # Continue until the pointers meet
    while debut < fin:
        # If characters at both ends are not equal, it's not a palindrome
        if mot[debut] != mot[fin]:
            return False
        # Move the pointers towards the center
        debut += 1
        fin -= 1
    
    # If the loop completes without finding a mismatch, it's a palindrome
    return True

# Test cases
mot1 = "radar"
mot2 = "python"
mot3 = "kayak"

print(est_palindrome(mot1))  # True
print(est_palindrome(mot2))  # False
print(est_palindrome(mot3))  # True
