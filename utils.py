from transformers import pipeline
from nltk import word_tokenize

# Initialize a Hugging Face pipeline for semantic analysis
semantic_model = pipeline("text-classification", model="bert-base-uncased", return_all_scores=True, framework="pt")

def semantic_score(prompt, response):
    """
    Compute a semantic similarity score using a transformer model.
    """
    combined_text = f"Prompt: {prompt}\nResponse: {response}"
    results = semantic_model(combined_text)
    score = results[0][1]["score"] * 10  # Scale to 0-10
    feedback = "Good semantic alignment!" if score > 7 else "The response could align better with the prompt."
    return feedback, score

def keyword_score(response, keywords):
    """
    Score the response based on the presence of specific keywords.
    """
    response_tokens = set(word_tokenize(response.lower()))
    match_count = sum(1 for keyword in keywords if keyword in response_tokens)
    total_keywords = len(keywords)

    if total_keywords == 0:
        return "No keywords provided for scoring.", 0

    score = (match_count / total_keywords) * 10  # Scale to 0-10
    feedback = f"Matched {match_count}/{total_keywords} keywords."
    return feedback, score

def extract_keywords(prompt):
    """
    Extract keywords from the prompt for simple keyword matching.
    """
    # Basic approach: Extract nouns using NLTK tokenizer (can be extended with spaCy or advanced techniques)
    return [word.lower() for word in word_tokenize(prompt) if word.isalnum()]
