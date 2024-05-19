from spell_checker import SpellChecker
from plural_checker import PluralChecker

class InputHandler:
    def __init__(self):
        # Initializing InputHandler with instances of SpellChecker and PluralChecker
        self.spell_checker = SpellChecker()
        self.plural_checker = PluralChecker()

    def get_corrected_input(self, user_input):
        # Correcting spelling and converting plural forms to singular in the user input
        return ' '.join([self.spell_checker.correct_spelling(self.plural_checker.get_singular_form(word)) for word in user_input.split()])
