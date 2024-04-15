import string, random

class Codec:
    '''
    Create a function that creates a random 6-character code, using the 62 alphanumeric characters.
    Use two maps, one that maps the long urls to short and vise versa for the other map
    Avoid duplicate shortURLs by checking if the one generated is already used. If yes, keep generating
    '''
    chars = string.ascii_letters + string.digits
    
    def __init__(self):
        self.url_to_short = dict()
        self.short_to_url = dict()
        
    def getShortUrl(self) -> str:
        code = ''.join(random.choice(self.chars) for i in range(6)) # randomly generate 6 character alphanumeric code
        return "http://tinyurl.com/" + code

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_to_short:
            return self.url_to_short[longUrl]
        
        # Prevent duplicate tiny urls
        short = self.getShortUrl()
        while short in self.short_to_url:
            short = self.getShortUrl()
        
        self.url_to_short[longUrl] = short
        self.short_to_url[short] = longUrl

        return short

    
    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_to_url[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))