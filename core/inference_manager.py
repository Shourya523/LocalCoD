from discovery.scanner import Scanner

class InferenceManager:
    def __init__(self):
        self.scanner = Scanner()

    def generate(self, model, prompt):

        detected_providers = self.scanner.scan()

        for detected in detected_providers:

            if model in detected.info.installedModels:
                return detected.provider.generate(model, prompt)

        raise Exception(f"Model '{model}' not found.")