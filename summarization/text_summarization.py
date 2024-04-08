from gensim.summarization import summarize

def generate_summary(text, ratio=0.2):
    try:
        summary = summarize(text, ratio=ratio)
        print(f"Summary: {summary}")
        return summary
    except ValueError:
        print("Error generating summary. Text is too short.")
    return None