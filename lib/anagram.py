# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        sorted_word = sorted(self.word)
        for w in words:
            if sorted(w) == sorted_word:
                anagrams.append(w)
        return anagrams

        