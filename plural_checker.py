class PluralChecker:
    def __init__(self):
        pass  # Constructor with no initialization needed

    def is_plural(self, word):
        # Check if the word ends with 's' to determine if it's plural
        return word.endswith('s')

    def get_singular_form(self, word):
        # If the word is plural, remove the 's' to get its singular form
        if self.is_plural(word):
            return word[:-1]
        else:
            return word  # Return the word unchanged if it's already singular

    def get_plural_form(self, word):
        # If the word is not plural, add 's' to make it plural
        if not self.is_plural(word):
            return word + 's'
        else:
            return word  # Return the word unchanged if it's already plural
