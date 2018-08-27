from talon.voice import Context, Key

ctx = Context('trello', bundle='com.atlassian.trello')

keymap = {
    '(quick add | add)': Key('ctrl-alt-space'),
    'boards': Key('b'),
    'search': Key('/'),
    'archive': Key('c'),
    'due date': Key('d'),
    'edit': Key('e'),
    'cancel': Key('esc'),
    'save': Key('cmd-enter'),
    'open card': Key('enter'),
    'create open': Key('shift-enter'),
    'filter': Key('f'),
    'toggle label': Key(';'),
    '(add | remove) members': Key('m'),
    'new card': Key('n'),
    'move card left': Key(','),
    'move card right': Key('.'),
    'my cards': Key('q'),
    '(watch | unwatch) card': Key('s'),
    '(assign | unassign) me': Key('space'),
    'edit title': Key('t'),
    'vote': Key('v'),
    '[| toggle] board menu': Key('w'),
    'clear filters': Key('x'),
    'shortcuts': Key('?'),
    'member': Key('@'),
    'tag label': Key('#'),
    'position': Key('^'),
    
    # TODO Add label color numbers (extended)
    'label': Key('l'),
}

ctx.keymap(keymap)