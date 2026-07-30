from providers.base import BaseProvider ## implement the abstract class from base providers file to here
import requests
from models.provider_info import ProviderInfo
from models.generation_response import GenerationResponse
from models.completion_response import CompletionResponse
from context.extractor import ContextExtractor


class OllamaProvider(BaseProvider):
    
    def detect(self):
        try:
            response = requests.get("http://127.0.0.1:11434/api/tags")
            data = response.json()

            return ProviderInfo(
                name="Ollama",
                loadedModels=self.get_loaded_models(),
                installedModels=self.get_models(data)
            )

        except requests.exceptions.RequestException:
            return None
    def get_models(self,data):
        model_lists=[]
        for models in data["models"]:
            model_lists.append(models["name"])
        return model_lists
    def get_loaded_models(self):
        response=requests.get("http://127.0.0.1:11434/api/ps")
        model_loaded=response.json()
        loaded_models = []
        for model in model_loaded["models"]:
            loaded_models.append(model["name"])
        return loaded_models
    def generate(self, request):
        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": request.model,
                "prompt": request.prompt,
                "temperature": request.temperature,
                "stream": request.stream
            }
        )
        return GenerationResponse(
            text=response.json()["response"]
        )

    def complete(self, request):
        # Step 1: Extract prefix and suffix from request using ContextExtractor
        extractor = ContextExtractor()
        context = extractor.extract(request)

        # Step 2: Build a concise prompt asking strictly for direct code completion
        prompt = (
            f"Output ONLY the code snippet to insert between the prefix and suffix. "
            f"Do not write explanations, comments, or markdown code fences.\n\n"
            f"Prefix:\n{context.prefix}\n"
            f"Suffix:\n{context.suffix}\n"
            f"Completion:"
        )

        # Retrieve max_tokens from request (defaulting to 64 tokens)
        max_tokens = getattr(request, "max_tokens", 64)

        # Step 3: Send request to Ollama HTTP API with num_predict option to limit tokens
        payload = {
            "model": request.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "num_predict": max_tokens
            }
        }

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json=payload
        )

        # Step 4: Extract completed code text and wrap in CompletionResponse
        return CompletionResponse(
            text=response.json()["response"]
        )


        