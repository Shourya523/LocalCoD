class DetectedProvider:
    def __init__(self,info,provider):
        self.info=info
        self.provider=provider
        
    def __repr__(self):
        return f"DetectedProvider(info={self.info})"
    