line = 'Gniew zawsze pozostawia po sobie wiele pustego miejsca, \n' \
       'w które natychmiast, jak powódź, \n' \
       'wlewa się smutek i płynie wielką rzeką, \n' \
       'bez początku i końca.'

words = line.split()
sum = 0
for i in words:
   sum = sum + len(i)
print(sum)