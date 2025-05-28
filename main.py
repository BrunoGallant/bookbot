from stats import get_num_words, count_characters

def get_boot_text(file_path: str) -> str:
    """
    Loads file content from the specified file path.
    Args:
        file_path (str): The path to the file to be read.
    Returns:
        str: The content of the file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def main():
    """
    Main function to execute the script.
    """
    file_path = 'books/frankenstein.txt'
    try:
        boot_text = get_boot_text(file_path)
        counted = get_num_words(boot_text)
        print(f"{counted} words found in the document")
        print(count_characters(boot_text))
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()  