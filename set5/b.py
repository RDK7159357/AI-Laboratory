from nltk.tokenize import sent_tokenize, word_tokenize

text = """Natural language processing (NLP) is a field of artificial intelligence. 
It focuses on the interaction between computers and humans. NLP techniques are used 
to analyze and understand human language. Machine learning algorithms help in this process."""

print("Sentence Chunking:")
sentences = sent_tokenize(text)
for i, sent in enumerate(sentences, 1):
    print(f"{i}. {sent.strip()}")

print("\n" + "="*60 + "\n")

print("Word Chunking:")
words = word_tokenize(text)
print(f"Total words: {len(words)}")
print(f"Words: {words[:20]}...")

print("\n" + "="*60 + "\n")

print("Character-level Chunks (size=50):")
chunks = [text[i:i+50] for i in range(0, len(text), 50)]
for i, chunk in enumerate(chunks, 1):
    print(f"Chunk {i}: {chunk}...")
