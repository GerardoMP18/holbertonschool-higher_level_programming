#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        _length = len(sentence)
        _first = sentence[0]
    else:
        sentence[0] = None
        return (0, _first)
    return _length, _first
