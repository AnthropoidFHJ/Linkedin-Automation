import re
import time
import random

def random_delay(min_delay=1.0, max_delay=3.0):
    time.sleep(random.uniform(min_delay, max_delay))

def remove_markdown(text, ignore_hashtags=False):
    patterns = [
        r"(\*{1,2})(.*?)\1",  # Bold and italics
        r"\[(.*?)\]\((.*?)\)",  # Links
        r"`(.*?)`",  # Inline code
        r"(\n\s*)- (.*)",  # Unordered lists
        r"(\n\s*)\* (.*)",  # Unordered lists
        r"(\n\s*)[0-9]+\. (.*)",  # Ordered lists
        r"(#+)(.*)",  # Headings
        r"(>+)(.*)",  # Blockquotes
        r"(---|\*\*\*)",  # Horizontal rules
        r"!\[(.*?)\]\((.*?)\)",  # Images
    ]

    if ignore_hashtags:
        patterns.remove(r"(#+)(.*)")

    for pattern in patterns:
        text = re.sub(pattern, r" ", text)

    return text.strip()
