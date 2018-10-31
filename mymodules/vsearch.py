def search_for_vowels(phrase:str) -> set:
    """Return any vowels supplied in phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search_for_letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))
