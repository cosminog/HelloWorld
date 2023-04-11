from sys import stdin, stdout, argv

#
#   Несложная программа приветствия с параметром
#

def sanitize(s):
    result = ''.join(ch for ch in s if ch.isalpha())
    return result.capitalize() if len(result) else 'Anonymous'

def salut(name=None):
    hello = 'Hello'
    welcome = 'welcome to our Galaxy'
    mark = '!'
    if name:
        message = '{}, {}, {}{}'.format(hello, name, welcome, mark)
    else:
        message = '{}, {}{}'.format(hello, welcome, mark)
    stdout.write(message + '\n')

if __name__ == "__main__":
    salut(sanitize(argv[1]) if len(argv) > 1 else None)
