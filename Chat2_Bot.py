#!/usr/bin/env python
# coding: utf-8

import nltk
import string
import streamlit as st
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from pathlib import Path

# Télécharger ressources NLTK
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("punkt_tab")

# Charger le fichier texte
file_path = Path("agriculture.txt")
data = file_path.read_text(encoding="utf-8")

# Découper en phrases
sentences = sent_tokenize(data, language="french")

# Prétraitement
stop_words = set(stopwords.words("french"))

def preprocess(text):
    words = word_tokenize(text.lower(), language="french")
    words = [
        word for word in words
        if word not in stop_words and word not in string.punctuation
    ]
    return words

# Trouver phrase la plus pertinente
def get_most_relevant_sentence(query):
    query_words = set(preprocess(query))

    max_similarity = 0
    most_relevant_sentence = "Désolé, je n’ai pas trouvé cette information."

    for sentence in sentences:
        sentence_words = set(preprocess(sentence))

        similarity = len(query_words.intersection(sentence_words)) / float(
            len(query_words.union(sentence_words))
        )

        if similarity > max_similarity:
            max_similarity = similarity
            most_relevant_sentence = sentence

    return most_relevant_sentence

# Fonction chatbot
def chatbot(question):
    return get_most_relevant_sentence(question)

# Interface Streamlit
def main():
    st.title("🌱 Chatbot Djamil AGRO")
    st.write(
        "Bonjour 👋 ! Je suis le chatbot de Djamil AGRO. "
        "Posez-moi vos questions sur les prix, fruits, légumes et livraisons."
    )

    question = st.text_input("Vous :")

    if st.button("Envoyer"):
        if question.strip():
            response = chatbot(question)
            st.write("🤖 Chatbot :", response)
        else:
            st.warning("Veuillez saisir une question.")

if __name__ == "__main__":
    main()
