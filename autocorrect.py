from spellcheck import SpellChecker

def autoCorrect(word):
    spell = SpellChecker()
    misspelled = spell.unknown(word)
    word=spell.correction(word.lower())
    return word


