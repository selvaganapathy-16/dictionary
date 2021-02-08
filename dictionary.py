import json
data = json.load(open("data.json"))
def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        print("enter the correct word")

word=input("enter the word")
output=translate(word)
print(output)