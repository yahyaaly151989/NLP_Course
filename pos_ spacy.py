import spacy

# Download and install the 'en_core_web_sm' model
spacy.cli.download("en_core_web_sm")

# Load the model after downloading
nlp = spacy.load("en_core_web_sm")

# Continue with your processing code
text = "He went to school, he played with his friends"
doc = nlp(text)

# Print token details with POS explanations
for token in doc:
    print(
        token.text,
        " | ",
        token.pos_,
        " | ",
        spacy.explain(token.pos_)
    )
doc = nlp("He went to school, he played with his friends")

for token in doc:
    print(token," | ", token.pos_, " | ", spacy.explain(token.pos_), " | ", token.tag_, " | ", spacy.explain(token.tag_))

earnings_text = """
Apple etc. reported its quarterly earnings today. The company's revenue was $100 billion, showing a 25% increase from the previous quarter. However, the net income decreased by 5% to $20 billion. The CEO, Tim Cook, expressed confidence in the company's future growth prospects.
"""

doc = nlp(earnings_text)

process_tokens = []

for token in doc:
    if token.pos_ not in ["SPACE", "PUNCT", "X"]:
        process_tokens.append(token.text)

# Join the filtered tokens into a single string
processed_text = " ".join(process_tokens)

print(processed_text)





