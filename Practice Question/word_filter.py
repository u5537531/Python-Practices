import re
from collections import Counter

def word_filter_counter(text, filter_words):
    # Lowercase the text and filter words for case-insensitive comparison
    text_lower = text.lower()
    filter_words_lower = [word.lower() for word in filter_words]

    # Use regex to split the text into words, considering punctuation
    words = re.findall(r'\b\w+\b', text_lower)

    # Filter and count the words
    filtered_counts = Counter(word for word in words if word in filter_words_lower)

    return dict(filtered_counts)

print(word_filter_counter("Hello world, hello!", ["hello"]))  # Test case 1
print(word_filter_counter("The quick brown fox.", ["the"]))  # Test case 2
print(word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]))  # Test case 3
print(word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]))  # Test case 4
