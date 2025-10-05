
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class TFIDF_Engine:
    def __init__(self, data_path="faq_data.json"):
        self.data_path = data_path
        self.vectorizer, self.question_vectors = self._prepare_data()

    def _prepare_data(self):
        with open(self.data_path, 'r') as f:
            self.faqs = json.load(f)
        
        questions = [faq['question'] for faq in self.faqs]
        vectorizer = TfidfVectorizer()
        question_vectors = vectorizer.fit_transform(questions)
        return vectorizer, question_vectors

    def get_response(self, query, threshold=0.5):
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.question_vectors)
        max_similarity = similarities.max()
        
        if max_similarity > threshold:
            best_match_index = similarities.argmax()
            return self.faqs[best_match_index]['answer']
        return None

