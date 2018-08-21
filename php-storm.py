from talon.voice import Context, Key

ides = {
    "com.jetbrains.PhpStorm",
}


ctx = Context('phpstorm', func=lambda app, win: any(
    i in app.bundle for i in ides))

keymap = {
    '(phiz | fizz)': ['php', Key('tab')],
    # 'search': [Key('shift'), Key('shift')],
    'golf': ['fore', Key('tab')],
    'chop': ['forek', Key('tab')],
    'bat': ['?=', Key('tab')],
    'if': ['if', Key('tab')],
    'complete': Key('cmd-shift-enter'),
    'definition': Key('alt-space'),
}


ctx.keymap(keymap)


def unload(): ctx.unload()