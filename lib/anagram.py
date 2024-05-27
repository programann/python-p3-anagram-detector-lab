# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, words):
        anagrams = []
        #Use the sorted functionality to arrange the letters alphabetically
        sorted_word = sorted(self.word)
        # Using for loop to iterte over a=each string.
        for w in words:
            # If a words has the same letters as self.word then it is an anagram 
            if sorted(w) == sorted_word:
                anagrams.append(w)
        return anagrams

        