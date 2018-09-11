from talon.voice import Key, Context, Str, press


ctx = Context('Finder', bundle='com.apple.finder')


def go_to_path(path):
    def path_function(m):
        press('cmd-shift-g')
        Str(path)(None)
        press('return')
    return path_function


ctx.keymap({
    '(dupe | duplicate)': Key('cmd-d'),
    'trash it': Key('cmd-backspace'),

    # jump to location
    'all [my] files': Key('shift-cmd-f'),
    '[my] computer': Key('shift-cmd-c'),
    'documents': Key('shift-cmd-o'),
    'desktop': Key('shift-cmd-d'),
    'library': Key('shift-cmd-l'),
    'network': Key('shift-cmd-k'),
    'utilities': Key('shift-cmd-u'),
    'downloads': Key('alt-cmd-l'),
    'applications': Key('shift-cmd-a'),
    'home': Key('shift-cmd-h'),
    'iCloud': Key('shift-cmd-i'),
    'airdrop': Key('shift-cmd-r'),
    'talon': go_to_path('~/.talon/user'),
    'code': go_to_path('~/code'),
    'pictures': go_to_path('~/Pictures'),
    'music': go_to_path('~/Music'),
    'movies': go_to_path('~/Movies'),
    'dropbox': go_to_path('~/Dropbox'),
    'books': go_to_path('~/Books'),
    'local sites': go_to_path('~/Local Sites'),
    'next level': go_to_path('~/Documents/Client Work/Next Level'),

    # views
    'icon': Key('cmd-1'),
    'list': Key('cmd-2'),
    'column': Key('cmd-3'),
    'cover': Key('cmd-4'),

    # sorting / arranging files
    '[(sort | arrange)] by none': Key('ctrl-cmd-0'),
    '[(sort | arrange)] by name': Key('ctrl-cmd-1'),
    '[(sort | arrange)] by kind': Key('ctrl-cmd-2'),
    '[(sort | arrange)] by date last opened': Key('ctrl-cmd-3'),
    '[(sort | arrange)] by date added': Key('ctrl-cmd-4'),
    '[(sort | arrange)] by date modified': Key('ctrl-cmd-5'),
    '[(sort | arrange)] by size': Key('ctrl-cmd-6'),
    '[(sort | arrange)] by tags': Key('ctrl-cmd-7'),

    # navigation
    'parent folder': Key('cmd-up'),
    'new window': Key('cmd-n'),
    'new folder': Key('cmd-shift-n'),
    'new tab': Key('cmd-t'),
    'collapse': Key('cmd-left'),
    'expand': Key('cmd-right'),
    'open': Key('cmd-down'),
    '(info | information)': Key('cmd-i'),

    # other actions
    '[toggle] preview': Key('shift-cmd-p'),
    'eject': Key('cmd-e'),
    'connect to server': Key('cmd-k'),
    '[create] alias': Key('cmd-l'),
    'close all': Key('alt-cmd-w'),
    'add to dock': Key('ctrl-shift-cmd-t'),
    'add to sidebar': Key('ctrl-cmd-t'),
    'show package contents': Key('cmd-alt-o'),
    # 'pathway': Key('cmd-alt-c'),
})
