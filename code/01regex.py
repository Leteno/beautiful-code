
import sys

def main():
    if len(sys.argv) > 2:
        match(sys.argv[1], sys.argv[2])
    else:
        regex, text = input('regex: '), input('text: ')
        match(regex, text)

def match(regex, text):
    import pdb
#    pdb.set_trace()
    if regex[0] == '^':
        return matchString(regex[1:], text)

    i = 0
    while i < len(text):
        if matchString(regex, text[i:]):
            return True
        i += 1
    return False

def matchString(regex, text):
    i, j   = 0, 0
    while i < len(regex):
        i, j, ok = matchHere(regex, text, i, j)
        if not ok:
            return False
    return True

def matchHere(regex, text, i, j):
    if j == len(text):
        if regex[i] == '$':
            return i, j, True
        elif regex[i] == '*':
            return i+1, j, True
        return i, j, False
    elif regex[i] == '.' or regex[i] == text[j]:
        return i + 1, j + 1, True
    elif regex[i] == '*':
        if i == 0:
            return i, j, False
        elif regex[i-1] == '.' or regex[i-1] == text[j]:
            return i, j+1, True
        else:
            return i+1, j, True
    return i, j, False

def test():
    tests = [('.*', 'abcdefg', True), ('.*.*', 'abcdefg', True), ('a*.*', 'abcdefg', True), ('b*.*', 'abcdefg', True), ('a*b*c*', 'ab', True), ('a*b*c*', 'abc', True), ('a*b*', 'abcd', False)]
    for regex, text, wanted in tests:
        print('testing: %s, %s, %s, result: %s' % (regex, text, wanted, 'pass' if wanted == match(regex, text) else 'fail'))

if __name__ == "__main__":
    test()
