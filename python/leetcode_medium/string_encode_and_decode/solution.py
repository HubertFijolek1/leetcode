class Solution:
    def encode(self, strs):
        """
        Encodes a list of strings to a single string.
        
        Args:
        strs (List[str]): The list of strings to encode.
        
        Returns:
        str: The encoded string, with each original string prepended by its length and a delimiter '#'.
        
        Examples:
        encode(["hello", "world"]) returns "5#hello5#world"
        encode(["", "abc", "def"]) returns "0#3#abc3#def"
        """
        # Use list comprehension to append each string's length and '#' before the string
        return ''.join(f'{len(s)}#{s}' for s in strs)  

    def decode(self, s):
        """
        Decodes a single string to a list of strings.
        
        Args:
        s (str): The encoded string.
        
        Returns:
        List[str]: The original list of strings, decoded from the input string.
        
        Examples:
        decode("5#hello5#world") returns ["hello", "world"]
        decode("0#3#abc3#def") returns ["", "abc", "def"]
        """
        strs = []  
        i = 0  
        while i < len(s):  # Process the entire encoded string
            j = s.find('#', i)  # Find the next '#' character from position i
            length = int(s[i:j]) 
            # Append the string that follows '#' up to the length specified
            strs.append(s[j+1:j+1+length])
            i = j + 1 + length  # Move index i to the position after the current string
        return strs 

# Example Usage
sol = Solution()
encoded = sol.encode(["hello", "world"])
print("Encoded:", encoded)  # Encoded: 5#hello5#world
decoded = sol.decode(encoded)
print("Decoded:", decoded)  # Decoded: ['hello', 'world']
