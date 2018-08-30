from talon.voice import Context, Key

ctx = Context('bit-bucket', func=lambda app, win: 'Bitbucket' in win.title)

keymap = {
    # All Pages

    'shortcuts': Key('?'),
    'left navigation': Key('['),
    'site search': Key('/'),

    # Most Pages (except your work and repository source)
    'omnibar': Key('.'),
    'next item': Key('capslock-j'),
    'last item': Key('capslock-k'),
    'selected': Key('capslock-o'),
    '[work] dashboard': Key('capslock-g capslock-d'),
    '[bucket] settings': Key('capslock-g capslock-a'),
    'remove focus': Key('esc'),
    'go back': Key('capslock-u'),
    'right navigation': Key(']'),

    # Repository source
    'focus': Key('capslock-f'),

    # Repository pages (except source)
    'create': Key('capslock-c capslock-r'),
    'import': Key('capslock-I capslock-r'),
    'source': Key('capslock-r capslock-s'),
    'view commits': Key('capslock-r capslock-c'),
    'view branches': Key('capslock-r capslock-b'),
    'pull requests': Key('capslock-r capslock-p'),
    'issues': Key('capslock-r capslock-i'),
    'wiki': Key('capslock-r capslock-w'),
    'show downloads': Key('capslock-r capslock-d'),
    'repo settings': Key('capslock-r capslock-a'),
    'find file': Key('capslock-f'),

    # Repository pages (except source and settings)
    'fork repository': Key('capslock-x capslock-f'),
    'create branch': Key('capslock-x capslock-b'),
    'compare': Key('capslock-x capslock-c'),
    'fork repository': Key('capslock-x capslock-f'),
    'create pull request': Key('capslock-x capslock-p'),
    'create issue': Key('capslock-x capslock-i'),

    # Pull Requests
    'submit comment': Key('ctrl+enter'),
    'inline comments': Key('capslock-t capslock-c'),
    'diff tab': Key('capslock-p capslock-d'),
    'commits tab': Key('capslock-p capslock-c'),
    'activity tab': Key('capslock-p capslock-a'),
    'show tasks': Key('shift-capslock-t'),

}

ctx.keymap(keymap)
