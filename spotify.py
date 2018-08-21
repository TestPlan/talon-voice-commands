from talon.voice import Context, Key

ides = {
    "com.spotify.client",
}


ctx = Context('phpstorm', func=lambda app, win: any(
    i in app.bundle for i in ides))

keymap = {
    '(play | pause)': Key('space'),
    'search': Key('cmd-l'),
    '(lower volume | quieter)': Key('cmd-down'),
    '((pump | raise) volume | louder)': Key('cmd-up'),
    '(next song | next | next track)': Key('cmd-right'),
    '(last song | last | last track)': Key('cmd-left'),
}


ctx.keymap(keymap)


def unload(): ctx.unload()