import json
import difflib
from difflib import get_close_matches
def resourceData():
    global dataSource
    dataSource = json.load(open("dictionary_compact.json", 'r'))


def wordSearch(word):
    resourceData()
    word = word.lower()
    if word in dataSource:
        return dataSource[word]
    elif len(get_close_matches(word,dataSource.keys()))>0:
        listOfPossibilities = get_close_matches(word,dataSource.keys(),n=1)
        choice = input("Did you mean %s instead?\nEnter Y if Yes or N if No : " %listOfPossibilities[0])
        if choice =='y' or choice =='Y':
            return dataSource[listOfPossibilities[0]]
        else:
            return "No result found. Sorry"
        return
    else:
        return "The word does not exist.Please enter another word."




a = input("Enter any word :")
b = wordSearch(a)
print("\n",b)



