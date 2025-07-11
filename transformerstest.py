# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text-generation", model="microsoft/DialoGPT-medium")
prompt = "Explain in one sentence why the sky is blue:"
result = pipe(prompt, 
             max_new_tokens=50,
             temperature=0.7,
             do_sample=True,
             pad_token_id=pipe.tokenizer.eos_token_id,
             use_safetensors=True)
print(result[0]['generated_text'])