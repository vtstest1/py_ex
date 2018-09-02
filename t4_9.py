#!/usr/local/bin/python3
def get_odds():
    for i in range(1,10,2):
            yield(i)
step=0
for i in get_odds():
    if step==2:
        print (i)
    step+=1
