from core.inference_manager import InferenceManager

manager = InferenceManager()

response = manager.generate(
    model="batiai/gemma4-26b:latest",
    prompt="Tell me a joke."
)

print(response.text)