from discovery.scanner import Scanner

class InferenceManager:
    def __init__(self):
        self.scanner = Scanner()

    def generate(self, request):

        detected_providers = self.scanner.scan()

        for detected in detected_providers:

            if request.model in detected.info.installedModels:
                return detected.provider.generate(request)

        raise Exception(f"Model '{request.model}' not found.")

    def complete(self, request):

        detected_providers = self.scanner.scan()

        for detected in detected_providers:

            if request.model in detected.info.installedModels:
                return detected.provider.complete(request)

        raise Exception(f"Model '{request.model}' not found.")