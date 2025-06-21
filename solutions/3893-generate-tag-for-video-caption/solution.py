class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()  # split caption into words
        if not words:
            return "#"
        
        # Convert to camelCase
        res = words[0].lower()  # first word in lowercase
        for word in words[1:]:
            if word:
                res += word[0].upper() + word[1:].lower()
        
        # Remove non-letter characters
        cleaned = ''.join(ch for ch in res if ch.isalpha())

        # Add '#' and truncate to 100 characters
        final_result = '#' + cleaned
        return final_result[:100]

