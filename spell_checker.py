from textblob import TextBlob

class SpellChecker:
    def __init__(self):
        pass  # No need to initialize anything for TextBlob

    def correct_spelling(self, word):
        # Creating a TextBlob object for the word
        blob = TextBlob(word)
        # Correcting the spelling of the word using TextBlob's correct method
        corrected_word = str(blob.correct())
        # If the corrected word is the same as the original word, return the original word
        if corrected_word.lower() == word.lower():
            return word
        # Otherwise, return the corrected word
        return corrected_word
