"""
Intro to python exercises shell code
"""


def is_odd(x):
    return x%2!=0
    """
    returns True if x is odd and False otherwise
    """

print(is_odd(3))
print(is_odd(4))

def is_palindrome(word):
    word2 = word[::-1]
    return word==word2
    """
    returns whether `word` is spelled the same forwards and backwards
    """
string = "hello there"
print(is_palindrome(string))
string = "racecar"
print(is_palindrome(string))



def only_odds(numlist):
    list =[]
    for i in numlist:
        if is_odd(i):
            list.append(i)
    return list
    """
    returns a list of numbers that are odd from numlist
    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
myList = [1,2,3,4,5,6]
print(only_odds(myList))


def count_words(text):
    text=text.lower()
    list = text.split(" ")
    thisDict = {list[0]:1}
    for i in list:
        if i in thisDict:
            thisDict[i]+=1;
        else:
            thisDict[i]=1
    return thisDict
string = "there are no words repeated here here the words"
print(count_words(string))


