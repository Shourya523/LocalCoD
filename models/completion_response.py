# CompletionResponse wraps the generated code completion result returned by a provider.

class CompletionResponse:
    def __init__(self, text):
        # text: The code completion string produced by the model
        self.text = text

    def __repr__(self):
        return f"CompletionResponse(text={self.text})"
