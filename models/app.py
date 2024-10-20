import json
import random
import string
from tkinter import ttk, scrolledtext
from typing import List, Dict, Set, Optional
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class NLPInterviewChatbot:
    def __init__(self):
        # Load interview data from JSON file
        with open('data/interview_data.json', 'r') as file:
            interview_data = json.load(file)
        
        self.categories = interview_data["questions"]
        
        # NLP preprocessing tools
        self.stop_words = set([
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
            "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 
            'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 
            'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 
            'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
            'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 
            'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
            'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
            'with', 'about', 'against', 'between', 'into', 'through', 'during', 
            'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 
            'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 
            'then', 'once'
        ])
    
    def preprocess_text(self, text):
        """Apply NLP preprocessing techniques"""
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans("", "", string.punctuation))
        # Tokenization
        tokens = text.split()
        # Remove stop words
        tokens = [token for token in tokens if token not in self.stop_words]
        return tokens
    
    def calculate_similarity(self, tokens1, tokens2):
        """Calculate Jaccard similarity between two token sets"""
        set1 = set(tokens1)
        set2 = set(tokens2)
        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))
        return intersection / union if union != 0 else 0
    
    def find_matching_category(self, user_question):
        # Preprocess user question
        question_tokens = self.preprocess_text(user_question)
        
        best_match = None
        highest_similarity = 0
        
        # Check each category
        for category in self.categories:
            # Combine all keywords for the category
            category_tokens = [self.preprocess_text(category["question"])]
            
            # Calculate similarity
            similarity = self.calculate_similarity(question_tokens, category_tokens[0])
            
            if similarity > highest_similarity and similarity > 0.1:  # Threshold
                highest_similarity = similarity
                best_match = category
                
        return best_match
    
    def get_response(self, user_question):
        matching_category = self.find_matching_category(user_question)
        
        if matching_category:
            # Use previous responses to avoid repetition
            response = random.choice(matching_category["responses"])
            return response
        else:
            default_responses = [
                "Could you please rephrase your question?",
                "I'm not sure I understood. Could you ask that in a different way?",
                "I'm not familiar with that type of question. Could you try asking something else?",
                "That's an interesting question. Could you elaborate or ask it differently?"
            ]
            return random.choice(default_responses)

def create_chat_interface():
    chatbot = NLPInterviewChatbot()
    terminal_width = 80  # Assuming default terminal width
    
    print("\n" + "="*terminal_width)
    print("Interview Chatbot".center(terminal_width))
    print("="*terminal_width)
    print("\nType 'quit' to exit")
    print("Ask your interview questions and I'll provide responses.\n")
    
    while True:
        try:
            # Right-aligned user input with padding
            user_input = input(" "*60 + "You: ").strip()
            
            if user_input.lower() == 'quit':
                print("\nThank you for practicing! Good luck with your interviews!")
                break
            
            # Left-aligned bot response
            response = chatbot.get_response(user_input)
            print(f"\nBot: {response}\n")
            
        except KeyboardInterrupt:
            print("\nExiting chatbot...")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            continue

if __name__ == "__main__":
    create_chat_interface()
