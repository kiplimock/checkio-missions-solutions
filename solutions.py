# ----------------------------- #
# ------- QUESTION ONE -------- #
# ----------------------------- #
def sum_numbers(mystring):
    mynums = []
    for item in mystring.split():
        if item.isdigit():
            mynums.append(int(item))

    return sum(mynums)


# ----------------------------- #
# ------- QUESTION TWO -------- #
# ----------------------------- #
def checkio(array):
    sum_array = 0
    # initialize the sum as 0
    for index in range(len(array)):
        # generate indexes of the array without storing them
        if index%2 == 0:
            # check for even index
            sum_array += array[index]
            # increment the sum by every even element
    try:
        return sum_array*array[-1]
    except:
        return 0


# ----------------------------- #
# ------- QUESTION THREE -------- #
# ----------------------------- #
def left_join(phrases):
    return ','.join(map(lambda word: word.replace('right','left'), phrases))



# ----------------------------- #
# ------- QUESTION FOUR -------- #
# ----------------------------- #
# This solution is unnecessarily complicated
# avoid by all means. The others are simpler
def checkio(words):
    for index in range(len(words.split())):
        # loop variable to count through the length of the list
        if len(words.split()) < 3 or index + 3 > len(words.split()):
            # the sentence should have at least 3 words
            # the loop variable should never exceed the length of the list
            # when slicing in python, it's possible to have an index grreater than the length of the string
            return False
        elif ''.join(words.split()[index:index+3]).isalpha():
            # join all the words to remove space characters because they are not alphabetic
            # now you can check if the string is purely alphabetic
            return True


# ----------------------------- #
# ------- QUESTION FIVE -------- #
# ----------------------------- #

import re

def first_word(text: str) -> str:
    return re.search("([\w']+)", text).group(1)


# ----------------------------- #
# ------- QUESTION SIX -------- #
# ----------------------------- #
from datetime import datetime

def days_diff(a, b):
    return abs((datetime(*b) - datetime(*a)).days)

# ----------- or
import datetime as dt

def days_diff(a,b):
    t1 = dt.date(a[0], a[1], a[2])
    t2 = dt.date(b[0], b[1], b[2])
    return abs((t2-t1).days)

# ----------------------------- #
# ------- QUESTION SEVEN -------- #
# ----------------------------- #
def count_digit(text):
    return len([char for char in text if char.isnumeric()])
    # counts the length of the string containing the digits

# ----------------------------- #
# ------- QUESTION EIGHT -------- #
# ----------------------------- #
def backward_string_by_word(text):
    return ''.join([word[::-1] for word in re.split(r'(\s+)', text)])

# ----------------------------- #
# ------- QUESTION NINE -------- #
# ----------------------------- #
def bigger_price(num, item_list):
    return sorted(item_list, key = lambda dic: dic['price'], reverse=True)[0:num]

# ------------- or
def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    return [data.pop([i['price'] for i in data].index(
        max([i['price'] for i in data]))) for x in range(limit)]

# ----------------------------- #
# ------- QUESTION TEN -------- #
# ----------------------------- #
import re

def between_markers(text, begin, end):
    if begin in text and end in text: # case 1 where both begin and end are in the text
        # empty string where end comes before begin
        if text.index(begin) > text.index(end):
            return ''
        else: # otherwise
            match = re.search(begin+r'[\w\s]+'+end, text) # this pattern is only for this case
            # slice the string removing the begin and end substrings
            return match.group()[len(begin):(len(match.group())-len(end))]
    elif begin in text and not end in text:
        # the '\\' includes one '\' in the pattern to capture characters like '[' and ']' in the text 
        match = re.search('\\' + begin+r'[\W\w\s]+', text)
        return match.group()[len(begin):]
    
    elif end in text and not begin in text:
        match = re.search(r'[\W\w\s]+'+'\\'+end, text).group()
        return match[:len(match)-len(end)]
    
    else:
        # where there is no begin or end in the text
        return text

# ----------------- or
def between_markers(text: str, begin: str, end: str) -> str:
    start = text.find(begin) + len(begin) if begin in text else None
    stop = text.find(end) if end in text else None
    return text[start:stop]

# ----------------------------- #
# ------- QUESTION ELEVEN -------- #
# ----------------------------- #
def checkio(lst):
    return [x for x in lst if lst.count(x) > 1]

# ----------------------------- #
# ------- QUESTION TWELVE -------- #
# ----------------------------- #
def popular_words(text, words):
    keys = [key for key in words]
    values = [text.lower().split().count(word) for word in words]
    return dict(zip(keys, values))

# ----------------------------- #
# ------- QUESTION THIRTEEN -------- #
# ----------------------------- #
def second_index(text, sub):
    return [i for i in range(len(text)) if text.startswith(sub,i)][1] if text.count(sub) > 1 else None

# ----------------------------- #
# ------- QUESTION FOURTEEN -------- #
# ----------------------------- #
from collections import Counter
def frequency_sort(items):
    result = [[elem]*freq for (elem,freq) in Counter(items).most_common()]
    return [j for i in result for j in i]
    # also same as
    # return [elem for elem, freq in Counter(items).most_common() for elem in [elem]*freq]
