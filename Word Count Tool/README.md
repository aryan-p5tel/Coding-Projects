# Word Counter

A simple Python script that counts the number of words in a piece of text entered by the user.

---

## Description

### `count_words(text)`
- **Purpose**: Takes a string as input and returns the number of words.  
- **How it works**:  
  - Splits the text into words using `.split()` (splits on spaces and whitespace).  
  - Returns the length of the resulting list.  

---

## Example Usage

### Code:
```python
# Function to count words in a given text
def count_words(text):
    words = text.split()
    return len(words)

# Ask user for input
text = input("Enter text to count words: ")
word_count = count_words(text)
print("Word count:", word_count)

Enter text to count words: I love computer science

Word count: 4
#python word_counter.py

