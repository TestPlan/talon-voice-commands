from talon.voice import Word, Context, Key, Rep, RepPhrase, Str, press
from talon import ctrl, clip
from talon_init import TALON_HOME, TALON_PLUGINS, TALON_USER
import string

# from user.utils import parse_word, surround, text, sentence_text, word, parse_words

alpha_alt = 'air bat cap die each fail gone harm sit jury crash look mad near owl pit quest red sun trap urge vest ' \
            'whale box yes zip'.split()

alnum = list(zip(alpha_alt, string.ascii_lowercase)) + [(str(i), str(i)) for i in range(0, 10)]
alpha = {}
alpha.update(dict(alnum))
alpha.update({'ship %s' % word: letter for word, letter in zip(alpha_alt, string.ascii_uppercase)})

# modifier key mappings
fkeys = [(f'F {i}', f'f{i}') for i in range(1, 13)]
keys = [
    'left', 'right', 'up', 'down', 'shift', 'tab', 'escape', 'enter', 'space',
    'backspace', 'delete', 'home', 'pageup', 'pagedown', 'end', 'fn',
]
keys = alnum + [(k, k) for k in keys]
keys += [
            ('tilde', '`'),
            ('comma', ','),
            ('dot', '.'),
            ('slash', '/'),
            ('(semi | semicolon)', ';'),
            ('quote', "'"),
            ('[left] square', '['),
            ('(right | are) square', ']'),
            ('backslash', '\\'),
            ('minus', '-'),
            ('equals', '='),
        ] + fkeys
alpha.update({word: Key(key) for word, key in fkeys})
alpha.update({'control %s' % k: Key('ctrl-%s' % v) for k, v in keys})
alpha.update({'control shift %s' % k: Key('ctrl-shift-%s' % v) for k, v in keys})
alpha.update({'control alt %s' % k: Key('ctrl-alt-%s' % v) for k, v in keys})
alpha.update({'command %s' % k: Key('cmd-%s' % v) for k, v in keys})
alpha.update({'command shift %s' % k: Key('cmd-shift-%s' % v) for k, v in keys})
alpha.update({'command alt shift %s' % k: Key('cmd-alt-shift-%s' % v) for k, v in keys})
alpha.update({'alt %s' % k: Key('alt-%s' % v) for k, v in keys})
alpha.update({'alt shift %s' % k: Key('alt-%s' % v) for k, v in keys})

# cleans up some Dragon output from <dgndictation>
mapping = {
    'semicolon': ';',
    'new-line': '\n',
    'new-paragraph': '\n\n',
}
# used for auto-spacing
punctuation = set('.,-!?')


def parse_word(word):
    word = str(word).lstrip('\\').split('\\', 1)[0]
    word = mapping.get(word, word)
    return word


def join_words(words, sep=' '):
    out = ''
    for i, word in enumerate(words):
        if i > 0 and word not in punctuation:
            out += sep
        out += word
    return out


def parse_words(m):
    return list(map(parse_word, m.dgndictation[0]._words))


def insert(s):
    Str(s)(None)


def text(m):
    insert(join_words(parse_words(m)).lower())


def sentence_text(m):
    text = join_words(parse_words(m)).lower()
    insert(text.capitalize())


def word(m):
    text = join_words(list(map(parse_word, m.dgnwords[0]._words)))
    insert(text.lower())


def surround(by):
    def func(i, word, last):
        if i == 0: word = by + word
        if last: word += by
        return word

    return func


def rot13(i, word, _):
    out = ''
    for c in word.lower():
        if c in string.ascii_lowercase:
            c = chr((((ord(c) - ord('a')) + 13) % 26) + ord('a'))
        out += c
    return out


# formatters = {
#     'dunder': (True, lambda i, word, _: '__%s__' % word if i == 0 else word),
#     'camel': (True, lambda i, word, _: word if i == 0 else word.capitalize()),
#     'snake': (True, lambda i, word, _: word if i == 0 else '_' + word),
#     'smash': (True, lambda i, word, _: word),
#     # spinal or kebab?
#     'truck': (True, lambda i, word, _: word if i == 0 else '-' + word),
#     # 'sentence':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
#     'title': (False, lambda i, word, _: word.capitalize()),
#     'allcaps': (False, lambda i, word, _: word.upper()),
#     'dubstring': (False, surround('"')),
#     'string': (False, surround("'")),
#     'padded': (False, surround(" ")),
#     'rot-thirteen': (False, rot13),
# }

formatters = {
    'cram': (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    'pathway': (True, lambda i, word, _: word if i == 0 else '/' + word),
    'dotsway': (True, lambda i, word, _: word if i == 0 else '.' + word),
    'yellsmash': (True, lambda i, word, _: word.upper()),
    'yellsnik': (True, lambda i, word, _: word.upper() if i == 0 else '_' + word.upper()),
    'dollcram': (True, lambda i, word, _: '$' + word if i == 0 else word.capitalize()),
    'champ': (True, lambda i, word, _: word.capitalize() if i == 0 else " " + word),
    'lowcram': (True, lambda i, word, _: '@' + word if i == 0 else word.capitalize()),
    'criff': (True, lambda i, word, _: word.capitalize()),
    'criffed': (True, lambda i, word, _: word.capitalize()),
    'yeller': (False, lambda i, word, _: word.upper()),
    'dunder': (True, lambda i, word, _: '__%s__' % word if i == 0 else word),
    'camel': (True, lambda i, word, _: word if i == 0 else word.capitalize()),
    'snake': (True, lambda i, word, _: word if i == 0 else '_' + word),
    'dot': (True, lambda i, word, _: '.' + word if i == 0 else '_' + word),
    'smash': (True, lambda i, word, _: word),
    # spinal or kebab?
    'spine': (True, lambda i, word, _: word if i == 0 else '-' + word),
    # 'sentence':  (False, lambda i, word, _: word.capitalize() if i == 0 else word),
    'title': (False, lambda i, word, _: word.capitalize()),
    'tridal': (False, lambda i, word, _: word.capitalize()),
    'allcaps': (False, lambda i, word, _: word.upper()),
    'dubstring': (False, surround('"')),
    'coif': (False, surround('"')),
    'string': (False, surround("'")),
    'posh': (False, surround("'")),
    'padded': (False, surround(" ")),
    'rot-thirteen': (False, rot13),
}


def FormatText(m):
    fmt = []
    for w in m._words:
        if isinstance(w, Word):
            fmt.append(w.word)
    try:
        words = parse_words(m)
    except AttributeError:
        with clip.capture() as s:
            press('cmd-c')
        words = s.get().split(' ')
        if not words:
            return

    tmp = []
    spaces = True
    for i, word in enumerate(words):
        word = parse_word(word)
        for name in reversed(fmt):
            smash, func = formatters[name]
            word = func(i, word, i == len(words) - 1)
            spaces = spaces and not smash
        tmp.append(word)
    words = tmp

    sep = ' '
    if not spaces:
        sep = ''
    Str(sep.join(words))(None)


ctx = Context('input')
keymap = {}
keymap.update(alpha)
keymap.update({
    'say <dgndictation> [over]': text,

    'sentence <dgndictation> [over]': sentence_text,
    'comma <dgndictation> [over]': [', ', text],
    'period <dgndictation> [over]': ['. ', sentence_text],
    'more <dgndictation> [over]': [' ', text],
    'word <dgnwords>': word,

    '(%s)+ [<dgndictation>]' % (' | '.join(formatters)): FormatText,

    'tab': Key('tab'),
    '(backtab | back tab)': Key('shift-tab'),
    '(left | lef)': Key('left'),
    'right': Key('right'),
    'up': Key('up'),
    'down': Key('down'),
    'dot (calm | com)': '.comffset-key="ba538d3bb2',
    'protocol': 'http://',
    'secure protocol': 'https://',

    'puter sleep': Key('ctrl-alt-shift-cmd-s'),
    'puter down': Key('ctrl-alt-shift-cmd-d'),
    'puter restart': Key('ctrl-alt-shift-cmd-r'),
    'about this puter': Key('ctrl-alt-shift-cmd-a'),
    '(doc | dock)': Key('alt-cmd-d'),
    # 'exit talent': Key('ctrl-alt-shift-cmd-t'),

    'delete': Key('backspace'),
    'slurp': Key('right backspace'),
    'run quit': Key('cmd-q'),
    'kill': Key('ctrl-c'),
    'screenshot page': Key('alt-shift-p'),
    'screenshot manual': Key('cmd-shift-4'),

    'spotlight': Key('cmd-space'),

    # Yarn
    'run server': ['yarn start', Key('return')],

    'cut': Key('cmd-x'),
    'copy': Key('cmd-c'),
    'paste': Key('cmd-v'),
    'undo': Key('cmd-z'),
    'redo': Key('cmd-shift-z'),
    'select all': Key('cmd-a'),
    'find': Key('cmd-f'),
    'find again': Key('cmd-g'),
    'print': Key('cmd-p'),
    'hide': Key('cmd-h'),
    'hide others': Key('alt-cmd-h'),
    '(mini | minimize)': Key('cmd-m'),
    'save': Key('cmd-s'),
    'save as': Key('shift-cmd-s'),
    'open': Key('cmd-o'),
    'close': Key('cmd-w'),
    'emoji': Key('ctrl-cmd-space'),
    'new folder': Key('shift-cmd-n'),
    '(settings | preferences)': Key('cmd-,'),
    'trash': Key('cmd-delete'),
    '(show desktop | toggle desktop | hide desktop)': Key('f11'),
    'windows mode': Key('ctrl-down'),
    'reverse': Key('tab'),
    'advance': Key('`'),

    'finder': Key('cmd-alt-space'),

    # Zoom
    'zoom in': Key('cmd-+'),
    'zoom out': Key('cmd--'),

    '(comment | uncomment)': Key('cmd-/'),
    'start': Key('cmd-left'),
    'end': Key('cmd-right'),
    'page up': Key('pageup'),
    'page down': Key('pagedown'),
    'jump [right] word': Key('alt-right'),
    'jump left word': Key('alt-left'),

    # Selecting text
    'select line': Key('cmd-right cmd-shift-left'),
    'select copy': Key('cmd-right cmd-shift-left cmd-c'),
    'select cut': Key('cmd-right cmd-shift-left cmd-x'),
    'select start': Key('cmd-shift-left'),
    'select end': Key('cmd-shift-right'),
    'select right': Key('shift-right'),
    'select left': Key('shift-left'),
    'select word left': Key('left shift-right left alt-left shift-alt-right'),
    'select word [right]': Key('right shift-left right alt-right shift-alt-left'),

    'slap': [Key('cmd-right enter')],
    'enter': Key('enter'),
    '(escape | scape)': Key('esc'),
    'question [mark]': '?',
    'tilde': '~',
    '(bang | exclamation point)': '!',
    'dollar [sign]': '$',
    '(downscore | score)': '_',
    '(dubscore | double downscore | behm)': '__',
    '(dubdash | double dash | behmdash)': '--',
    '(semi | semicolon)': ';',
    'colon': ':',
    '(square | left square [bracket] | bracket)': '[', '(rsquare | are square | right square [bracket])': ']',
    '(paren | left paren)': '(', '(rparen | are paren | right paren)': ')',
    '(brace | left brace)': '{', '(rbrace | are brace | right brace)': '}',
    '(angle | left angle | less than)': '<', '(rangle | are angle | right angle | greater than)': '>',

    '(star | asterisk)': '*',
    '(pound | hash [sign] | octo | thorpe | number sign)': '#',
    'percent [sign]': '%',
    'caret': '^',
    'at sign': '@',
    '(and sign | ampersand | amper)': '&',
    'pipe': '|',

    '(dubquote | double quote)': '"',
    'quote': "'",
    'triple quote': "'''",
    '(dot | period)': '.',
    'comma': ',',
    'space': ' ',
    '[forward] slash': '/',
    'backslash': '\\',

    '(dot dot | dotdot)': '..',
    'cd': 'cd ',
    'cd talon home': 'cd {}'.format(TALON_HOME),
    'cd talon user': 'cd {}'.format(TALON_USER),
    'cd talon plugins': 'cd {}'.format(TALON_PLUGINS),

    'run make (durr | dear)': 'mkdir ',
    'run get': 'git ',
    'run get (R M | remove)': 'git rm ',
    'run get add': 'git add ',
    'run get bisect': 'git bisect ',
    'run get branch': 'git branch ',
    'run get checkout': 'git checkout ',
    'run get clone': 'git clone ',
    'run get commit': 'git commit ',
    'run get diff': 'git diff ',
    'run get fetch': 'git fetch ',
    'run get grep': 'git grep ',
    'run get in it': 'git init ',
    'run get log': 'git log ',
    'run get merge': 'git merge ',
    'run get move': 'git mv ',
    'run get pull': 'git pull ',
    'run get push': 'git push ',
    'run get rebase': 'git rebase ',
    'run get reset': 'git reset ',
    'run get show': 'git show ',
    'run get status': 'git status ',
    'run get tag': 'git tag ',
    'run (them | vim)': 'vim ',
    'run L S': 'ls\n',
    'dot pie': '.py',
    'dot Jay Es': '.js',
    'dot Sea EsEs': '.css',
    '(dot flip | dot P H P)': '.php',
    '(dot sass | dot sassy)': '.scss',
    'run make': 'make\n',
    'run jobs': 'jobs\n',

    # javascript
    'const': 'const ',
    'let': 'let ',
    'var': 'var ',

    'static': 'static ',
    'tip pent': 'int ',
    'tip char': 'char ',
    'tip byte': 'byte ',
    'tip pent 64': 'int64_t ',
    'tip you went 64': 'uint64_t ',
    'tip pent 32': 'int32_t ',
    'tip you went 32': 'uint32_t ',
    'tip pent 16': 'int16_t ',
    'tip you went 16': 'uint16_t ',
    'tip pent 8': 'int8_t ',
    'tip you went 8': 'uint8_t ',
    'tip size': 'size_t',
    'tip float': 'float ',
    'tip double': 'double ',

    'args': ['()', Key('left')],
    'brackets': ['[]', Key('left')],
    'block': [' {}', Key('left enter')],
    'empty array': '[]',
    'empty dict | braces': '{}',
    # 'brace': [' else if ()', Key('left')],

    # python
    'state switch': ['switch ()', Key('left')],
    'state case': ['case \nbreak;', Key('up')],
    'state goto': 'goto ',
    'state import': 'import ',

    'state include': '#include ',
    'state include system': ['#include <>', Key('left')],
    'state include local': ['#include ""', Key('left')],
    'state type deaf': 'typedef ',
    'state type deaf struct': ['typedef struct {\n\n};', Key('up'), '\t'],

    'word queue': 'queue',
    'word none': 'None',
    'word eye': 'eye',
    'word bson': 'bson',
    'word iter': 'iter',
    'word no': 'NULL',
    'word cmd': 'cmd',
    'word dup': 'dup',
    'word streak': ['streq()', Key('left')],
    'word printf': 'printf',
    'word (dickt | dictionary)': 'dict',
    'word shell': 'shell',
    'word to do': 'TODO',

    'word lunixbochs': 'lunixbochs',
    'word talon': 'talon',
    'word Point2d': 'Point2d',
    'word Point3d': 'Point3d',
    'title Point': 'Point',
    'word angle': 'angle',

    'dunder in it': '__init__',
    'self taught': 'self.',
    'dickt in it': ['{}', Key('left')],
    'list in it': ['[]', Key('left')],
    'string utf8': "'utf8'",
    'state past': 'pass',

    'equals': '=',
    '(double equals | dub equals)': '==',
    '(trip | triple equals)': '===',
    '(minus | dash)': '-',
    'plus': '+',
    'arrow': '->',
    '(fat arrow | fatty)': ' => ',
    '(call | parens | parenthesis)': '()',
    'indirect': '&',
    'dereference': '*',
    '(op equals | assign)': ' = ',
    'op (minus | subtract)': ' - ',
    'op (plus | add)': ' + ',
    'op (times | multiply)': ' * ',
    'op divide': ' / ',
    'op mod': ' % ',
    '[op] (minus | subtract) equals': ' -= ',
    '[op] (plus | add) equals': ' += ',
    '[op] (times | multiply) equals': ' *= ',
    '[op] divide equals': ' /= ',
    '[op] mod equals': ' %= ',

    '(op | is) greater [than]': ' > ',
    '(op | is) less [than]': ' < ',
    '(op | is) equal': ' == ',
    '(op | is) not equal': ' != ',
    '(op | is) greater [than] or equal': ' >= ',
    '(op | is) less [than] or equal': ' <= ',
    '(op (power | exponent) | to the power [of])': ' ** ',
    'op and': ' && ',
    'op or': ' || ',
    '[op] (logical | bitwise) and': ' & ',
    '[op] (logical | bitwise) or': ' | ',
    '(op | logical | bitwise) (ex | exclusive) or': ' ^ ',
    '[(op | logical | bitwise)] (left shift | shift left)': ' << ',
    '[(op | logical | bitwise)] (right shift | shift right)': ' >> ',
    '(op | logical | bitwise) and equals': ' &= ',
    '(op | logical | bitwise) or equals': ' |= ',
    '(op | logical | bitwise) (ex | exclusive) or equals': ' ^= ',
    '[(op | logical | bitwise)] (left shift | shift left) equals': ' <<= ',
    '[(op | logical | bitwise)] (right shift | shift right) equals': ' >>= ',

    'shebang bash': '#!/bin/bash -u\n',

    'new window': Key('cmd-n'),
    'next window': Key('cmd-`'),
    'last window': Key('cmd-shift-`'),
    'next app': Key('cmd-tab'),
    'last app': Key('cmd-shift-tab'),
    'next tab': Key('ctrl-tab'),
    'new tab': Key('cmd-t'),
    'last tab': Key('ctrl-shift-tab'),

    'next space': Key('cmd-alt-ctrl-right'),
    'last space': Key('cmd-alt-ctrl-left'),

    'scroll down': [Key('down')] * 30,
    'scroll down more': [Key('down')] * 60,
    'scroll up': [Key('up')] * 30,
    'scroll up more': [Key('up')] * 60,
})
ctx.keymap(keymap)
