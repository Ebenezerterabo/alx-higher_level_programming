#!/usr/bin/python3
def multiple_returns(sentence):
    #sentence is empty return None for first character
    if sentence:
        return len(sentence), sentence[0]
    else:
        return 0, None
