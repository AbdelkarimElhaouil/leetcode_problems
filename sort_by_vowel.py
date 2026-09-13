"""
Sort Words by Vowel Count
Complete the sort_words_by_vowels function.

You will sort a list of words using a custom sort order with sorted() and a tuple key.

Sorting rules, in this exact order:

Fewest vowels first (use vowel_count helper)
If two words have the same number of vowels, the shorter word comes first
If both vowel count and length are the same, sort alphabetically (ignore case)
Only the vowels a, e, i, o, u count, and they should be counted case-insensitively.

You must:

Implement vowel_count(word) that returns how many vowels are in word
Implement sort_words_by_vowels(words) that returns a new sorted list
Use Python's built-in sorted with a tuple key: e.g. (vowel_count(...), len(...), word.lower())
Example
words = ["sky", "aeiou", "test", "Apple", "rhythm"]
result = sort_words_by_vowels(words)
print(result)
# ["sky", "rhythm", "test", "Apple", "aeiou"]

Explanation:

"sky" → 0 vowels, length 3
"rhythm" → 0 vowels, length 6
"test" → 1 vowel
"Apple" → 2 vowels
"aeiou" → 5 vowels
So by the rules: fewest vowels first, then shortest length, then alphabetical.

"""

def vowel_count(word):
    return sum(1 for x in word if x.lower() in "aeiou")


def sort_words_by_vowels(words):
    return list(sorted(words, key=lambda x: (vowel_count(x), len(x), x.lower())))


words = ["sky", "aeiou", "test", "Apple", "rhythm"]
result = sort_words_by_vowels(words)
print(result)

# data = ['apple', 'banana', 'apricot', 'blueberry', 'avocado']

# def func1(s): return len(s)      # sort by length first
# def func2(s): return s[0]        # then by first letter
# def func3(s): return s[-1]       # then by last letter

# result = sorted(data, key=lambda x: (func1(x), func2(x), func3(x)))
# print(result)

# print(vowel_count("aeidddu"))

