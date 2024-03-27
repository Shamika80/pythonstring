def highlight_keywords(reviews, keywords):
  """
  This function takes a list of reviews and a list of keywords and highlights
  the keywords in uppercase within each review.

  Args:
      reviews: A list of strings containing product reviews.
      keywords: A list of strings containing keywords to highlight.

  Returns:
      None. The function prints the modified reviews with highlighted keywords.
  """
  for review in reviews:
    for keyword in keywords:
      # Case-insensitive replacement with uppercase keyword
      review = review.upper().replace(keyword.upper(), keyword)
    print(review)

def sentiment_tally(review, positive_words, negative_words):


  
  positive_count = 0
  negative_count = 0
  for word in review.lower().split():  
    if word in positive_words:
      positive_count += 1
    elif word in negative_words:
      negative_count += 1
  return {"positive": positive_count, "negative": negative_count}

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]


highlight_keywords(reviews.copy(), keywords=positive_words + negative_words)  


for review in reviews:
  sentiment = sentiment_tally(review, positive_words, negative_words)
  print(f"Review: {review}")
  print(f"Sentiment: Positive - {sentiment['positive']}, Negative - {sentiment['negative']}")
  print("-"*20)