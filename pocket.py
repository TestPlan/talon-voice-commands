from talon.voice import Context, Key

ctx = Context('pocket', bundle='com.readitlater.PocketMac')

keymap = {
    # File Menu
    'save keyboard': Key('cmd-s'),
    'refresh': Key('cmd-r'),
    'close window': Key('cmd-w'),
    'print': Key('cmd-p'),

    # Edit Menu
    'tags': Key('t'),
    'save tag': Key('cmd-enter'),
    'undo': Key('cmd-z'),
    'redo': Key('shift-cmd-z'),

    # View Menu
    'next': Key('j'),
    'previous': Key('k'),
    'list home': Key('cmd-1'),
    'list favorites': Key('cmd-2'),
    'list archive': Key('cmd-3'),
    'filter all items': Key('alt-1'),
    'filter articles': Key('alt-2'),
    'filter videos': Key('alt-3'),
    'filter images': Key('alt-4'),
    '(web | article) view': Key('cmd-/'),

    # Item Menu
    'archive': Key('a'),
    'favorite': Key('f'),
    'delete': Key('backspace'),
    'copy item': Key('c'),
    'mail item': Key('shift-cmd-i'),
    'open in browser': Key('o'),
    'open in background': Key('cmd-o'),
}

ctx.keymap(keymap)
