import nltk
from nltk.corpus import stopwords

# download stopwords if not available
try:
    stop = set(stopwords.words("english"))
except:
    nltk.download("stopwords")
    stop = set(stopwords.words("english"))

def tokenize(text):
    return text.lower().split()

def build_index(d1, d2):
    t1, t2 = tokenize(d1), tokenize(d2)
    terms = sorted(set(t1 + t2))
    index = {}

    for term in terms:
        if term in stop:
            continue
        docs = []
        if term in t1:
            docs.append(f"Document1 ({t1.count(term)})")
        if term in t2:
            docs.append(f"Document2 ({t2.count(term)})")
        if docs:
            index[term] = docs
    return index

def print_index(index):
    print("INVERTED INDEX:\n")
    for term, docs in index.items():
        print(term, "->", ", ".join(docs))

doc1 = "The quick brown fox jumped over the lazy dog"
doc2 = "The lazy dog slept in the sun"

index = build_index(doc1, doc2)
print_index(index)
