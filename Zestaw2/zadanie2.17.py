line = 'Gniew zawsze pozostawia po sobie wiele pustego miejsca, \n' \
       'w które natychmiast, jak powódź, \n' \
       'wlewa się smutek i płynie wielką rzeką, \n' \
       'bez początku i końca.'

words = [word.lower() for word in line.split()]
words.sort()
print("Sorted alphacetic order: ")
for word in words:
    print(word)

print("\n")
line = line.split()
line = sorted(line, key=len)
print("Sorted by lenght: ")
for word in line:
    print(word)
