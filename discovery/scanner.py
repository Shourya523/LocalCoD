from providers.registry import SUPPORTED_PROVIDERS

class Scanner:
    def scan (self):
        active_providers=[]
        for provider in SUPPORTED_PROVIDERS:
            if provider.detect():
                active_providers.append(provider)
        return active_providers
scannerTemp= Scanner()
print(scannerTemp.scan())