import itertools
from pprint import pprint

def solution(word):
    answer = 0
    vowels = ['A', 'E', 'I', 'O', 'U']
    vowels_combinations = []

    for i in range(1, len(vowels) + 1):
        pds = itertools.product(vowels, repeat=i)
        for pd in pds:
            vowels_combinations.append(''.join(pd))

    vowels_combinations.sort()
    for idx, vowel in enumerate(vowels_combinations):
        if word == vowel:
            answer = idx
            
    return answer

solution('AAAAE')