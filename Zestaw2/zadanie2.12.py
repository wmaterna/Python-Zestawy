import string
line = 'Gniew zawsze pozostawia po sobie wiele pustego miejsca,\n' \
       'w które natychmiast, jak powódź,\n' \
       'wlewa się smutek i płynie wielką rzeką,\n' \
       'bez początku i końca.'

result = line.split("\n")
firstLetter = ''
for letters in result:
    firstLetter = firstLetter + letters[0]
print("Word from first letters: " + firstLetter)

lastLetters = ''
for letters in result:
    if letters[len(letters)-1] in string.punctuation:
        lastLetters = lastLetters + letters[len(letters)-2]
    else:
        lastLetters = lastLetters + letters[len(letters)-1]

print("Word from last letters: " + lastLetters)