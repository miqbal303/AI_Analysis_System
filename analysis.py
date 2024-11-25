from utils import semantic_score, keyword_score, extract_keywords
from cache import cache_response

def analyze_response(prompt, response):
    """
    Analyze the client's response using both semantic and keyword-based approaches.
    """
    # Check if the response is already cached
    cached_feedback = cache_response(prompt, response, None)
    if cached_feedback:
        return cached_feedback

    # Extract keywords for keyword scoring
    keywords = extract_keywords(prompt)
    keyword_feedback, keyword_score_result = keyword_score(response, keywords)

    # Perform semantic analysis
    semantic_feedback, semantic_score_result = semantic_score(prompt, response)

    # Combine the results
    overall_score = (keyword_score_result + semantic_score_result) / 2
    feedback = (
        f"Keyword Analysis: {keyword_feedback}\n"
        f"Semantic Analysis: {semantic_feedback}\n"
        f"Overall Score: {overall_score:.2f}/10"
    )

    # Cache the feedback and return it
    return cache_response(prompt, response, feedback)
