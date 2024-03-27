def highlight_keywords(reviews, keywords):
  
  for review in reviews:
    for keyword in keywords:
      # Case-insensitive replacement with uppercase keyword
      review = review.upper().replace(keyword.upper(), keyword)
    print(review)

reviews = [
    "This product is really good. I'm impressed with its quality.",
    "The performance of this product is excellent. Highly recommended!",
    "I had a bad experience with this product. It didn't meet my expectations.",
    "Poor quality product. Wouldn't recommend it to anyone.",
    "The product was average. Nothing extraordinary about it."
]
keywords = ["GOOD", "EXCELLENT", "BAD", "POOR", "AVERAGE"]

highlight_keywords(reviews, keywords)