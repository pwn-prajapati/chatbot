import nltk
nltk.data.path.append("C:/Users/VICTUS/AppData/Roaming/nltk_data")

import nltk
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

def sentence_similarity(sent1, sent2, stop_words):
    words1 = [w.lower() for w in word_tokenize(sent1) if w.isalpha()]
    words2 = [w.lower() for w in word_tokenize(sent2) if w.isalpha()]
    all_words = list(set(words1 + words2))

    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)

    for w in words1:
        if w not in stop_words:
            vector1[all_words.index(w)] += 1

    for w in words2:
        if w not in stop_words:
            vector2[all_words.index(w)] += 1

    return cosine_similarity([vector1], [vector2])[0][0]

def build_similarity_matrix(sentences, stop_words):
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
    for i in range(len(sentences)):
        for j in range(len(sentences)):
            if i != j:
                similarity_matrix[i][j] = sentence_similarity(sentences[i], sentences[j], stop_words)
    return similarity_matrix

def generate_summary(text, top_n=5):
    stop_words = set(stopwords.words('english'))
    sentences = sent_tokenize(text)
    if len(sentences) < top_n:
        return text

    sim_matrix = build_similarity_matrix(sentences, stop_words)
    scores = nx.pagerank(nx.from_numpy_array(sim_matrix))
    ranked = sorted(((scores[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = [s for _, s in ranked[:top_n]]
    return '\n'.join(summary)
