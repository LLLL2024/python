message = input(">")
words = message.split(' ')
emojis = {
    "$":"happy",
    "Ú":"unhappy"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

