from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "Machine learning is great",
    "Natural language processing is amazing",
    "Machine learning and NLP are related",
    "Deep learning is part of machine learning"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

print("Bag of Words - Feature Names:")
print(vectorizer.get_feature_names_out())

print("\n" + "="*60 + "\n")

print("Document-Term Matrix:")
print(X.toarray())

print("\n" + "="*60 + "\n")

print("Term Frequencies:")
for i, doc in enumerate(corpus):
    print(f"\nDocument {i+1}: '{doc}'")
    feature_index = X[i].nonzero()[1]
    for idx in feature_index:
        print(f"  {vectorizer.get_feature_names_out()[idx]}: {X[i, idx]}")
