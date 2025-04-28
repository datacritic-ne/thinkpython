#! python3

import shelve
import sys

import anagram_sets

def store_anagrams(wordlist, anagram_map):
    
    #anagrams = anagram_sets.all_anagrams(wordlist)
    
    ana_shelf = shelve.open(wordlist, flag='c')
    #ana_shelf.update(anagrams)
    for word, word_list in anagram_map.items():
        ana_shelf[word] = word_list

    ana_shelf.close()

def read_anagrams(wordlist, word):
    
    shelf = shelve.open(wordlist)
    sig = anagram_sets.signature(word)
    
    try:
        return shelf[sig]
    except KeyError:
        return []
    #store_anagrams('words.txt')

    #with shelve.open('anagram_shelf') as s:
        
    #    if word in s:
    #        value = s[word]
    #        print(value)
    #    else:
    #        print("This word doesn\'t have any anagrams in the word list.")

#read_anagrams('opts')
def main(script, command='make_db'):
    if command == 'make_db':
        anagram_map = anagram_sets.all_anagrams('words.txt')
        store_anagrams('anagrams.db', anagram_map)
    else:
        print(read_anagrams('anagrams.db', command))


if __name__ == '__main__':
    main(*sys.argv)