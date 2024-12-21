words=[ "Hawaa","Abel", "Mango" ,"books",
"laptop", "cup", "plate", "wifi" ,"ugali"    
]
odd_length_words =[word for word in words if len(word) % 2!=0]
print("words with odd number of characters:",odd_length_words)
