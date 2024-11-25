class ResponseCache:
    """
    A simple in-memory cache for storing and retrieving responses.
    """
    def __init__(self):
        self.cache = {}

    def get(self, key):
        """
        Retrieve a cached value by key.
        """
        return self.cache.get(key)

    def set(self, key, value):
        """
        Cache a value by key.
        """
        self.cache[key] = value

    def clear(self):
        """
        Clear all cached values.
        """
        self.cache.clear()

# Example usage of the cache
cache = ResponseCache()

def cache_response(prompt, response, feedback):
    """
    Cache the feedback for a given prompt and response.
    """
    key = f"{prompt}|{response}"
    if cache.get(key) is None:
        cache.set(key, feedback)
        print("Response cached.")
    else:
        print("Response retrieved from cache.")
    return cache.get(key)
