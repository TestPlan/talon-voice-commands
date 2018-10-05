from talon.voice import Context, Key

ctx = Context('spectacle')

keymap = {
    'snap center': Key('alt-cmd-c'),
    '(fullscreen | full)': Key('cmd-alt-f'),
    'snapleft': Key('cmd-alt-left'),
    'snapright': Key('cmd-alt-right'),
    'snap up': Key('alt-cmd-up'),
    'snap down': Key('alt-cmd-down'),
    'snap top left': Key('ctrl-cmd-left'),
    'snap bottom left': Key('ctrl-shift-cmd-left'),
    'snap top right': Key('ctrl-cmd-right'),
    'snap bottom right': Key('ctrl-shift-cmd-right'),
    'next display': Key('ctrl-alt-cmd-right'),
    'previous display': Key('ctrl-alt-cmd-left'),
    'next third': Key('ctrl-alt-right'),
    'previous third': Key('ctrl-alt-left'),
    'make larger': Key('ctrl-alt-shift-right'),
    'make smaller': Key('ctrl-alt-shift-left'),
    'speck undo': Key('alt-cmd-z'),
    'speck redo': Key('alt-shift-cmd-z'),
}

ctx.keymap(keymap)
