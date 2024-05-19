import enchant

class SpellChecker:
    def __init__(self):
        # Initializing the SpellChecker class with an instance of the enchant dictionary for US English
        self.spell_checker = enchant.Dict("en_US")

    def correct_spelling(self, word):
        # Checking if the word is spelled correctly using the enchant library's check method
        if self.spell_checker.check(word):  
            return word
        # If the word is misspelled, getting suggestions for correct spellings using the suggest method
        suggestions = self.spell_checker.suggest(word)
        # If suggestions are available, returning the first suggested word
        if suggestions:
            return suggestions[0]
        # If no suggestions are available, returning the original word
        else:
            return word