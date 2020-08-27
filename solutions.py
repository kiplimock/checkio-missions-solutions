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
