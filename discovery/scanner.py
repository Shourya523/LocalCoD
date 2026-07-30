from providers.registry import SUPPORTED_PROVIDERS
from discovery.detected_provider import DetectedProvider

class Scanner:
    def scan (self):
        active_providers=[]
        for provider in SUPPORTED_PROVIDERS:
            provider_info = provider.detect()
            if provider_info:
                active_providers.append(
                    DetectedProvider(
                        info=provider_info,
                        provider=provider
                    )
                )
        return active_providers