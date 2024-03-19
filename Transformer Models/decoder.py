from transformers import pipeline

generator = pipeline("text-generation", model="openai-community/gpt2")
output = generator(
    "In this course, we will teach you how to",
    max_length=30,
    num_return_sequences=2,
    truncation=True,
    pad_token_id=50256
)

print(output)


