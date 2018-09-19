from talon.voice import Context, Key

ides = [
    "com.jetbrains.intellij",
    "com.jetbrains.intellij.ce",
    "com.jetbrains.AppCode",
    "com.jetbrains.CLion",
    "com.jetbrains.datagrip",
    "com.jetbrains.goland",
    "com.jetbrains.PhpStorm",
    "com.jetbrains.pycharm",
    "com.jetbrains.rider",
    "com.jetbrains.rubymine",
    "com.jetbrains.WebStorm",
    "com.google.android.studio",
]

ctx = Context('jetbrains', func=lambda app, win: any(
    i in app.bundle for i in ides))

keymap = {
    'clear': [Key('cmd-a'), Key('backspace')],
    'comment declaration': ['/**', Key('space')],
    'comment block': ['/**', Key('enter')],
    'block comment': Key('cmd-alt-/'),

    '(dupe | duplicate)': Key('cmd-d'),
    'import class': Key('alt-enter enter'),
    'quickfix': Key('alt-enter'),
    'go class': Key('cmd-o'),
    'go file': Key('cmd-shift-o'),
    '(go implement | go definition)': Key('cmd-b'),
    'preev method': Key('ctrl-up'),
    'neck method': Key('ctrl-down'),
    'refactor': Key('shift-f6'),
    'generate': Key('cmd-n'),
    'recent': Key('cmd-e'),

    'replace': Key('cmd-r'),
    'find action': Key('cmd-shift-a'),
    'settings': Key('cmd-,'),
    'grab': Key('alt-up'),
    'shrink': Key('alt-down'),
    'grab left': Key('cmd-shift-left'),
    'grab right': Key('cmd-shift-right'),
    'close': Key('cmd-w'),
    'top': Key('cmd-home'),
    'bottom': Key('cmd-end'),
    'grab up': Key('shift-cmd-pageup'),
    'grab down': Key('shift-cmd-pagedown'),
    # 'rename': Key('shift-f6'),
    'move file': Key('f6'),
    'file search': Key('shift shift'),
    'global search': Key('cmd-shift-f'),
    'go to file': Key('cmd-shift-n'),
    'format': Key('cmd-alt-l'),
    'expand': Key('cmd-+'),
    'collapse': Key('cmd--'),
    'erase line': Key('cmd-backspace'),
    'last change': Key('cmd-shift-backspace'),
    '((open | close) terminal | terminal (open | close) | toggle terminal | terminal)': Key('alt-f12'),
    'snip left': Key('cmd-shift-left delete'),
    'snip right': Key('cmd-shift-right delete'),
    'move up': Key('alt-shift-up'),
    'move down': Key('alt-shift-down'),
    'path': Key('cmd-shift-f'),
    'funk up': Key('cmd-shift-up'),
    'funk down': Key('cmd-shift-down'),
    '(breadcrumbs | crumbs)': Key('cmd-up'),

}

ctx.keymap(keymap)


def unload(): ctx.unload()
