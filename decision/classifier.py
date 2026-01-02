# decision/classifier.py

class ContentClassifier:
    def __init__(self):
        self.good_words = [
            "math", "physics" , "sewing", "knitting", "crochet", "christianity", "christian", 
            "python", "coding", "programming", "developer", "software", "engineer", "quant", 
            "investing"] 

        self.bad_words = [
            "gym", "self", "fitness", "fashion", "movie", "film", "america", "politics", "food", 
            "game", "philosophy", "trump", "hot", "girl", "tate", "redpill", "kirk", "fuentes", 
            "government", "funny", "skit", "comedy", "goals", "cat", "health", "cute", "wake", 
            "spirit", "habit", "psych", "dog", "sad", "gland", "truth", "devil", "satan", 
            "evil"] 

    def score(self, text: str) -> float:
        if any(w in text for w in self.bad_words):
            return 0.0001 #multiplier for like ratio and 10th-rooted multiplier for watch time

        if any(w in text for w in self.good_words):
            return 1000

        return 0.01
