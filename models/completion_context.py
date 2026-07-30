# CompletionContext holds the code snippets before and after the cursor position.
# This data structure allows providers to format prompts accurately for code completion.

class CompletionContext:
    def __init__(self, prefix, suffix, language=None):
        # prefix: Code text appearing before the cursor
        self.prefix = prefix
        
        # suffix: Code text appearing after the cursor
        self.suffix = suffix
        
        # language: Optional programming language tag (e.g., 'python', 'javascript')
        self.language = language

    def __repr__(self):
        return f"CompletionContext(prefix={repr(self.prefix)}, suffix={repr(self.suffix)}, language={self.language})"
