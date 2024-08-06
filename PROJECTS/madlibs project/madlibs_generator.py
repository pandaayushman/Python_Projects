with open('mystory.txt','r') as file:
    story = file.read()
listofwords = []
start = "["
end = "]"
var = 0
for i, character in enumerate(story):
    if character == start :
        var = i+1
    if character == end and var != 0:
        word = story[var : i]
        listofwords.append(word)


key_pair = {}

for words  in set(listofwords):
    input_word = input("Enter a suitable word for " + words+" : ")
    key_pair[words]= input_word

for words in listofwords:
    story = story.replace(words,key_pair[words])
print(story)
