s = input()
bad = 0
for i in range(0, len(s)):
    if i==0 and s[i]==s[i+1]:
        bad = 1
    elif i==3 and s[i]==s[i-1]:
        bad = 1
    elif i==1 and s[i] == s[i+1]:
        bad = 1

if bad == 1:
    print('Bad')
else: 
    print('Good')   