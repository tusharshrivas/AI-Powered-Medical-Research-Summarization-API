from transformers import pipeline

# Load summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_text(text):
    """
    Summarizes the cleaned text using a transformer-based model.

    Parameters:
    text (str): The cleaned input text.

    Returns:
    str: The summarized text.
    """
    if not text.strip():
        return "No valid content to summarize."

    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
    return summary[0]["summary_text"]

# Example usage
if __name__ == "__main__":
    sample_text = "A 45-year-old female presents with chest pain and high blood pressure. No prior history of cardiovascular disease."
    print(summarize_text(sample_text))
