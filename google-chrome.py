from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer

# It is recommended to use this script in tandem with Vimium,
# a Google Chrome plugin for controlling the browser via keyboard
# https://vimium.github.io/

context = Context('GoogleChrome', bundle='com.google.Chrome')


def open_focus_devtools(m):
    press('cmd-shift-c')


def show_panel(name):
    open_focus_devtools(None)

    # Open command menu
    press('cmd-shift-p')

    Str('Show %s' % (name))(None)
    press('enter')


def next_panel(m):
    open_focus_devtools(None)
    press('cmd-]')


def last_panel(m):
    open_focus_devtools(None)
    press('cmd-[')


def focus_address_bar(m):
    press('cmd-l')


def search(m):
    press('cmd-m')
    press('cmd-shift-.')


def scroll_to_top(m):
    press('g')
    press('g')


def print_page(m):
    press('cmd-p')


# Return focus from the dev-tools to the page
def refocus_page(m):
    focus_address_bar(None)

    # Escape button
    # This leaves the focus on the page at previous tab focused point, not t_he beginning of the page
    press('escape')


def back(m):
    refocus_page(None)
    press('cmd-[')


def forward(m):
    refocus_page(None)
    press('cmd-]')


def jump_tab(m):
    tab_number = parse_words_as_integer(m._words[1:])
    if tab_number is not None and 0 < tab_number < 9:
        press('cmd-%s' % tab_number)


context.keymap({
    'address bar': focus_address_bar,
    'search': search,
    'print': print_page,
    'top': scroll_to_top,

    # shortkeys plugin
    'bottom': Key('ctrl-b'),
    'copy euro': Key('ctrl-u'),
    'google it': Key('ctrl-g'),
    'move tab left': Key('ctrl-l'),
    'move tab right': Key('ctrl-r'),



    'clear': [Key('cmd-a'), Key('backspace')],

    # youtube
    # disable vimium for youtube shortcuts to work
    '(play | pause)': Key('k'),
    'movie mode': Key('f'),
    '[toggle] theater mode': Key('t'),
    'restart video': Key('home'),
    'end video': Key('end'),
    'volume down': Key('down'),
    'volume up': Key('up'),
    '(mute | unmute)': Key('m'),
    'slow down': Key('<'),
    'speed up': Key('>'),
    '(jump | forward) ten': Key('l'),
    '(jump | forward) five': Key('right'),
    'back ten': Key('j'),
    'back five': Key('left'),

    # youtube and gmail
    '(mail | video) search': Key('/'),

    # gmail
    'compose': Key('c'),
    '(send mail | send)': Key('cmd-enter'),
    '(carbon copy | see see)': Key('cmd-shift-c'),
    '(blind carbon copy | bee see see)': Key('cmd-shift-b'),
    'misspelled word': Key('cmd-;'),

    # Not working
    'word choice': Key('cmd-m'),
        
    'remove format': Key('cmd-\\'),
    'bold': Key('cmd-b'),
    'italics': Key('cmd-i'),
    'underline': Key('cmd-u'),
    'link': Key('cmd-k'),
    'numbered list': Key('cmd-shift-7'),
    'bulleted list': Key('cmd-shift-8'),
    'quote text': Key('cmd-shift-9'),
    'inbox': Key('g i'),
    'sent': Key('g t'),
    'drafts': Key('g d'),
    'label': Key('g l'),
    'contacts': Key('g c'),
    'spam': Key('!'),
    'trash mail': Key('#'),
    'reply': Key('r'),
    'reply all': Key('a'),
    'forward mail': Key('f'),
    'expand mail': Key(';'),
    'collapse mail': Key(':'),
    'move mail': Key('v'),


    # not working
    'previous video': Key('P'),

    'next video': Key('shift-n'),
    '(toggle captions | toggle caption)': Key('c'),

    'back[ward]': back,
    'forward': forward,
    'reload': Key('cmd-r'),
    'hard reload': Key('cmd-shift-r'),
    'bookmark': Key('cmd-d'),
    'toggle bookmark [bar]': Key('cmd-shift-b'),
    'bookmark manager': Key('cmd-alt-b'),
    'downloads': Key('cmd-shift-j'),
    'add extras': Key('ctrl-enter'),
    'add extras new': Key('ctrl-shift-enter'),

    'new tab': Key('cmd-t'),
    'new window': Key('cmd-n'),
    'close window': Key('cmd-shift-w'),
    '(incognito | incog)': Key('cmd-shift-n'),
    'close tab': Key('cmd-w'),
    '(reopen | unclose) tab': Key('cmd-shift-t'),

    'next tab': Key('cmd-alt-right'),
    '(last | prevous) tab': Key('cmd-alt-left'),

    'tab (1 | 2 | 3 | 4 | 5 | 6 | 7 | 8)': jump_tab,
    '(end | rightmost) tab': Key('cmd-9'),

    'find': Key('cmd-f'),
    'next match': Key('cmd-g'),
    '(last | prevous)': Key('cmd-shift-g'),
    '(pushpin | pullpin)': Key('cmd-shift-x'),

    'clear cash': Key('cmd-shift-backspace'),

    # dev tools
    '[toggle] dev tools': Key('cmd-alt-i'),
    'command [menu]': Key('cmd-shift-p'),
    'selector': Key('cmd-shift-c'),
    'mobile': Key('cmd-shift-m'),
    '(javascript (counsel | console) | javascript (counsel | console) close)': Key('cmd-alt-j'),
    'next panel': next_panel,
    '(last | prevous) panel': last_panel,
    '[show] application [panel]': lambda m: show_panel('Application'),
    '[show] audit[s] [panel]': lambda m: show_panel('Audits'),
    '[show] console [panel]': lambda m: show_panel('Console'),
    '[show] element[s] [panel]': lambda m: show_panel('Elements'),
    '[show] memory [panel]': lambda m: show_panel('Memory'),
    '[show] network [panel]': lambda m: show_panel('Network'),
    '[show] performance [panel]': lambda m: show_panel('Performance'),
    '[show] security [panel]': lambda m: show_panel('Security'),
    '[show] source[s] [panel]': lambda m: show_panel('Sources'),

    'refocus page': refocus_page,
    '[refocus] dev tools': open_focus_devtools,

    # Clipboard
    'paste same style': Key('cmd-alt-shift-v'),



})
