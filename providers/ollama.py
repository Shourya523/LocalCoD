from providers.base import BaseProvider ## implement the abstract class from base providers file to here
import requests
from models.provider_info import ProviderInfo


class OllamaProvider(BaseProvider):
    
    def detect(self):
        try:
            response = requests.get("http://127.0.0.1:11434/api/tags")
            data = response.json()

            return ProviderInfo(
                name="Ollama",
                models=self.get_models(data)
            )

        except requests.exceptions.RequestException:
            return None
    def get_models(self,data):
        model_lists=[]
        for models in data["models"]:
            model_lists.append(models["name"])
        return model_lists
            

""" 
provider=OllamaProvider()
print(provider.detect())
print(provider.get_models()) 

"""