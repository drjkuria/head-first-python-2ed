#!/usr/bin/env python3

phrase = "Don't panic!" 
plist = list(phrase) 
print(phrase) 
print(plist)

for i in range(4): 
    plist.pop()
plist.pop(0)
plist.remove("'") 
plist.extend([plist.pop(), plist.pop()]) 
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist) 
print(plist) 
print(new_phrase)