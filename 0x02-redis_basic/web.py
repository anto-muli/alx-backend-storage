import requests
import redis
from functools import wraps
from typing import Callable

# Initialize the Redis client
r = redis.Redis()

def cache_page(expiration: int = 10):
    """Decorator to cache the result of get_page function."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(url: str) -> str:
            # Check if the URL is already cached
            cached_page = r.get(f"cached:{url}")
            if cached_page:
                return cached_page.decode('utf-8')

            # If not cached, call the function and cache the result
            result = func(url)
            r.setex(f"cached:{url}", expiration, result)
            return result
        return wrapper
    return decorator

@cache_page(expiration=10)
def get_page(url: str) -> str:
    """Fetches the HTML content of a URL and caches it."""
    # Increment the access count for the URL
    r.incr(f"count:{url}")

    # Fetch the HTML content
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk"
    
    # Fetch the page content
    content = get_page(url)
    print(content)
    
    # Print the access count
    count = r.get(f"count:{url}").decode('utf-8')
    print(f"URL accessed {count} times")
