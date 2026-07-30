from providers.registry import SUPPORTED_PROVIDERS

class Scanner:
    def scan (self):
        active_providers=[]
        for provider in SUPPORTED_PROVIDERS:
            provider_info = provider.detect()
            if provider_info:
                active_providers.append(provider_info)
        return active_providers