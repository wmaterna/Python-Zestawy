line = 'Gniew zawsze pozostawia po sobie wiele pustego miejsca, \n' \
       'w które natychmiast, jak powódź, \n' \
       'wlewa się smutek i płynie wielką rzeką, \n' \
       'bez początku i końca.'

words = line.split()
maxWord = len(words[0])
longestWord = 'Gniew'
for i in words:
   if maxWord < len(i):
       maxWord = len(i)
       longestWord = i
print(maxWord)
print(longestWord)