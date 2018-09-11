from talon.voice import Context, Key

ctx = Context('android-messages', func=lambda app, win: 'Messages for web' in win.title)

keymap = {

    # Collides with spectacle
    'new': Key('cmd-alt-c'),
    
    'next conversation': Key('ctrl-.'),
    'previous conversation': Key('ctrl-,'),
    'delete conversation': Key('cmd-alt-r'),
    'archive conversation': Key('cmd-alt-h'),
    'open settings': Key('cmd-alt-x'),
    'attach files': Key('cmd-alt-a'),
    '(show | hide) emoji picker': Key('cmd-alt-e'),
    '(show | hide) sticker picker': Key('cmd-alt-s'),
    '(show | hide) gif picker': Key('cmd-alt-g'),
    '(show | hide) details': Key('cmd-alt-d'),

}

ctx.keymap(keymap)
