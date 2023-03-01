from collections import Counter

def longest_palindrome_length(s):
    # Count the frequency of each character in the string
    char_count = Counter(s)

    # Keep track of the total length of the palindrome
    length = 0

    # Loop through the character counts
    for count in char_count.values():
        # Add the maximum even number less than or equal to the count to the length
        length += (count // 2) * 2

        # If the count is odd and we haven't added the center character yet, add it to the length
        if count % 2 == 1 and length % 2 == 0:
            length += 1

    return length

print(longest_palindrome_length("bananas"))