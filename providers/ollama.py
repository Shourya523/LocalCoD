from providers.base import BaseProvider ## implement the abstract class from base providers file to here
import requests


class OllamaProvider(BaseProvider):
    
    def detect(self):
        try:
            response =requests.get("http://127.0.0.1:11434/api/tags")
            return response.status_code==200
        except requests.exceptions.RequestException:
            return False
    def get_models(self):
        if self.detect():
            response=requests.get("http://127.0.0.1:11434/api/tags")
            data=response.json()
            model_lists=[]
            for models in data["models"]:
                model_lists.append(models["name"])
            return model_lists
        else:
            print("no models are running")
            

""" 
provider=OllamaProvider()
print(provider.detect())
print(provider.get_models()) 

"""