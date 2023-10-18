from collections import Counter
import string

def count_word_frequencies(text):
    # Remove punctuation and convert text to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()

    # Split the text into words
    words = text.split()

    # Count word frequencies
    word_count = Counter(words)

    return word_count

if __name__ == "__main__":
    # Take input from the user
    input_text = input("Enter a text: ")

    # Count word frequencies in the input text
    word_frequencies = count_word_frequencies(input_text)

    # Display word frequencies
    for word, frequency in word_frequencies.items():
        print(f"{word}: {frequency}")
