from talon.voice import Context, Key

ides = [
    "com.jetbrains.PhpStorm",
]


ctx = Context('phpstorm', func=lambda app, win: any(
    i in app.bundle for i in ides))

keymap = {
    '(flip | phiz | fizz)': ['php', Key('tab')],
    'party': ['phps', Key('tab')],
    '(start flip | start phiz | start fizz)': '<?php ',
    '(end flip | end phiz | end fizz)': '?> ',
    # 'search': [Key('shift'), Key('shift')],
    'golf': ['fore', Key('tab')],
    'horse': ['for', Key('tab')],
    'horse markup': ['formk', Key('tab')],
    'chop': ['forek', Key('tab')],
    'eagles': ['?=', Key('tab')],
    'if': ['if', Key('tab')],
    'if markup': ['ifm', Key('tab')],
    'else if': ['elif', Key('tab')],
    'else if markup': ['elifm', Key('tab')],
    'else': ['else', Key('tab')],
    'else markup': ['elsem', Key('tab')],
    'complete': Key('cmd-shift-enter'),
    'definition': Key('alt-space'),
}


ctx.keymap(keymap)


def unload(): ctx.unload()