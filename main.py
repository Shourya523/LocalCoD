from core.inference_manager import InferenceManager

manager = InferenceManager()
from models.generation_request import GenerationRequest

request = GenerationRequest(
    model="batiai/gemma4-26b:latest",
    prompt="Tell me a joke."
)

response = manager.generate(request)

print(response.text)