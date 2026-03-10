import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('stopwords')
stop = set(stopwords.words("english"))

print("Aman Dubal T076")

# BOOLEAN RETRIEVAL #

docs = {
1:"this is the first document",
2:"this document is the second document",
3:"and this is the third one",
4:"is this the first document"
}

# preprocessing
def preprocess(text):
    words = text.lower().split()
    return [w for w in words if w not in stop]

processed = {i:preprocess(t) for i,t in docs.items()}

# inverted index
index={}
for d,terms in processed.items():
    for t in terms:
        index.setdefault(t,set()).add(d)

# Boolean Query
query = ["first","third"]
result = index.get(query[0],set()) & index.get(query[1],set())

print("\nBOOLEAN RETRIEVAL")
print("Query: first AND third")
print("Result:", sorted(result))

# VECTOR SPACE MODEL #

documents = [
"python programming language and data analysis",
"machine learning algorithms and programming techniques",
"natural language processing applications"
]

query = ["python programming"]

vectorizer = TfidfVectorizer(stop_words="english")

tfidf = vectorizer.fit_transform(documents)
query_vec = vectorizer.transform(query)

similarity = cosine_similarity(query_vec, tfidf)

print("\nVECTOR SPACE MODEL (TF-IDF)")
for i,score in enumerate(similarity[0],1):
    print(f"Doc {i} similarity:", round(score,3))

print("Most relevant document: Doc", similarity.argmax()+1)
