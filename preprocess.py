import re


def clean_text(text):
    """
    Cleans and formats medical reports before summarization.

    Parameters:
    text (str): The input medical report text.

    Returns:
    str: The cleaned text.
    """
    if isinstance(text, list):  # Handle multiple paragraphs in abstracts
        text = " ".join(text)

    text = text.replace("\n", " ")
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'[^\w\s.,]', '', text)  # Remove special characters except .,
    return text.strip()


# Example usage
if __name__ == "__main__":
    sample_text = "  This is   a test text! With extra spaces... \n and some special chars!@# "
    print(clean_text(sample_text))  # Output: "This is a test text. With extra spaces... and some special chars."
