# To run this code:
# Connect to internet
# Create virtual environment
# Activate virtual environment

# After that, then
# Just pip install sentence-transformers scikit-learn, kivy


# U can make your own dataset, that it's format should look like the dialogs.txt or the self.data variable
# U can contact me 0981254727 on whatsApp if, U want to understand a little bit more.

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from data import health_data
import time

class WargeBot:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def load_dataset(self, data_file="dialogs.txt"):

                self.data = health_data

                with open(data_file, "r") as f:
                    self.lines = f.readlines()

                for line in self.lines:
                    parts = line.strip().split("\t")
                    if len(parts) >= 2:
                        self.data.append((parts[0], parts[1]))

                self.questions = [q for q, a in self.data]
                self.answers = [a for q, a in self.data]

                self.questions_embeddings =  self.model.encode(self.questions)

    def type_text(self,text, delay=0.08):
        for c in text:
            print(c,end="",flush=True)
            time.sleep(delay)

    def get_response(self,user_input):
        user_embedding = self.model.encode([user_input])

        similarities = cosine_similarity(user_embedding, self.questions_embeddings)
        best_index = np.argmax(similarities)
        best_score = similarities[0][best_index]

        if best_score < 0.3:
            return "I don't understand that yet."
        
        return self.answers[best_index]


# bot = WargeBot()
# bot.load_dataset()
# print("WargeBot: Hello! Ask me anything (type 'exit' to quit)")

# while True:
#     user_input = input("\nYou: ")

#     if user_input.lower() == "exit":
#         bot.type_text("WargeBot: Goodbye ^__^")
#         break

#     response = bot.get_response(user_input)

#     print("WargeBot: ", end="")
#     bot.type_text(response)