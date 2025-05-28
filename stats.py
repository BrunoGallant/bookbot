def get_num_words(text: str) -> int:
    """
    Counts the number of words in the given text.
    Args:
        text (str): The text to count words in.
    Returns:
        int: The number of words in the text.
    """
    return len(text.split())

def count_characters(text: str) -> dict:
    """
    Counts the occurrences of each character in the given text.
    Args:
        text (str): The text to count characters in.
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            char = char.lower()  # Normalize to lowercase
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count
    