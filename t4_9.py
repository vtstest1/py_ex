#!/usr/local/bin/python3
def get_odds():
    for i in range(1,10,2):
            yield(i)
for y,i in enumerate(get_odds()):
    if y==2:
        print (i)
        break

