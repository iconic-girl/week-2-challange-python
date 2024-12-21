# List of words
words = ["apple", "banana", "cherry", "date", "kiwi", "mango", "orange"]

# List comprehension to filter words with an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Display the result
print("Original list:", words)
print("Words with odd number of characters:", odd_length_words)