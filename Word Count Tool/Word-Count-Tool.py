text=input("Enter text to count words: ") #input from user
# Function to count words in a given text
def count_words(text):
    words=text.split()
    return len(words) 
word_count = count_words(text) 
print("Word count:", word_count)
# Code checks number of words in text entered by user and outputs it