from transformers import pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english")
data = ["I love you", "I hate you"]
output=sentiment_pipeline(data)
print(output)
