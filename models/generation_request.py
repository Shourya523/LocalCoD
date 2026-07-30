class GenerationRequest:

    def __init__(
        self,
        model,
        prompt,
        temperature=0.7,
        stream=False,
    ):
        self.model = model
        self.prompt = prompt
        self.temperature = temperature
        self.stream = stream