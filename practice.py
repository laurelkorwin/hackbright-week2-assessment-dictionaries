from collections import defaultdict
from string import punctuation

"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    #turns the list of words into a set, which removes duplicate values
    remove_dupes = set(words)
    #turns the set with unique values back into a list, per instructions
    remove_dupes_list = list(remove_dupes)

    return remove_dupes_list


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    #turns items1 and items2 into sets, and then puts the items they have in common into another set
    unique_common_items = set(items1) & set(items2)
    #turns the set above into a list, per instructions
    unique_common_items_list = list(unique_common_items)

    return unique_common_items_list


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    positive = {}

    negative = {}

    paired_list = []

    for num in numbers:
        if num >= 0:
            positive[num] = True
        else:
            negative[num] = True

    for num in positive.keys():
        if num == 0:
            paired_list.append([num, num])
        elif -num in negative:
            paired_list.append([num, -num])

    return paired_list


def get_sum_zero_pairs_2(numbers):
    """Solution I thought of first, but dictionaries aren't as useful in this version (hence the solution above).

    I tried it and it works, though!!"""

    sum_zero_pairs = {}
    pairs_list = []

    #removes duplicates from the list and gives back a unique, sorted list
    unique_nums = set(numbers)
    sorted_numbers = sorted(list(unique_nums))

    #takes out zeroes, since they mess up calcs. If there is a zero, puts it in
    #the dictionary with key [0, 0] and value 1 (since value doesn't matter here)

    for number in sorted_numbers:
        if number == 0:
            sum_zero_pairs[(0, 0)] = 1
            numbers.remove(number)

    while len(sorted_numbers) > 1:
        #sets the last index in the list as a variable
        last_index = len(sorted_numbers) - 1

        #removes "outlier" values in the list that don't have a negative or positive match
        for index in range(0, last_index):
            first_value = sorted_numbers[0]
            last_value = sorted_numbers[last_index]
            abs_first = abs(first_value)
            abs_last = abs(last_value)
            if abs_first != abs_last:
                if abs_first > abs_last:
                    sorted_numbers.remove(first_value)
                else:
                    sorted_numbers.remove(last_value)
                last_index = len(sorted_numbers) - 1

    #now the fun begins!! with clean / useful data. If the first value is the last value:
    #dictionary key is created, and the first and last values are removed from the list.
    #then, it moves on to the next one.
        if first_value + last_value == 0:
            sum_zero_pairs[(first_value, last_value)] = 1
            sorted_numbers.remove(first_value)
            sorted_numbers.remove(last_value)

    for key in sum_zero_pairs.keys():
        pairs_list.append(list(key))

    return pairs_list


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    #creates empty dictionary for letters.
    #you can do this two ways - with default dict, and commented out syntax below to add
    #or with regular dict, and .get method

    #dict_of_letters = defaultdict(int)
    dict_of_letters = {}

    #removes punctuation marks, strips phrase of spaces and makes all letters lowercase
    phrase = phrase.translate(None, punctuation)
    phrase = phrase.replace(" ", "").lower()

    #puts each letter into the dictionary
    for letter in phrase:
        dict_of_letters[letter] = dict_of_letters.get(letter, 0) + 1
        # dict_of_letters[letter] += 1

    #creates a blank list for letters / instances
    list_of_instances = []

    #goes through the dictionary and appends instances and letters to the list
    #with instances FIRST so you can sort on them :)
    for letter, instances in dict_of_letters.items():
        list_of_instances.append([instances, letter])

    #sorts the list of instances in reverse, and creates a blank list for max letters
    sorted_list_of_instances = sorted(list_of_instances, reverse=True)
    max_letters = []

    #appends the letter at the beginnign of the reverse-sorted list to your new list
    max_letters.append(sorted_list_of_instances[0][1])

    #goes through the rest of the list, and if the letter/instances in question are already in the max list
    #AND the next instances value is the same as the one in the max list
    #puts the next letter into the max list
    for index in range(0, len(sorted_list_of_instances) - 1):
        if (sorted_list_of_instances[index][1] in max_letters and
            sorted_list_of_instances[index][0] == sorted_list_of_instances[index + 1][0]):

                max_letters.append(sorted_list_of_instances[index + 1][1])

    #returns a sorted version of the max_letters list
    return sorted(max_letters)


def top_chars2(phrase):
    """Another way to do this..."""

    #creates empty dictionary for letters.
    #you can do this two ways - with default dict, and commented out syntax below to add
    #or with regular dict, and .get method

    #dict_of_letters = defaultdict(int)
    dict_of_letters = {}

    #removes punctuation marks, strips phrase of spaces and makes all letters lowercase
    phrase = phrase.translate(None, punctuation)
    phrase = phrase.replace(" ", "").lower()

    #puts each letter into the dictionary
    for letter in phrase:
        dict_of_letters[letter] = dict_of_letters.get(letter, 0) + 1
        # dict_of_letters[letter] += 1

    #sets max_key and max_value placeholders
    max_key = None
    max_value = 0

    #loops through the dictionary and checks keys / values against the max value & key
    #if the value is greater, replaces both max value and key until you have the most common
    for letter, value in dict_of_letters.items():
        if value > max_value:
            max_value = value
            max_key = letter

    #puts max_key in a list
    max_key = [max_key]

    #loops through again to get ties. if the letter isn't already the max key,
    #and value is the same as max value, appends the letter to the list
    for letter, value in dict_of_letters.items():
        if letter not in max_key and value == max_value:
            max_key.append(letter)

    return max_key

#####################################################################
# You can ignore everything below this.


def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
