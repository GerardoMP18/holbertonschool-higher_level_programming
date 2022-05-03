#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        _length = len(sentence)
        _first = sentence[0]
    else:
        return (0, None)
    return _length, _first
