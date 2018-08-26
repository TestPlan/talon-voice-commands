from talon.voice import Context, Key, press, Str
from user.utils import parse_words_as_integer

context = Context('VSCode', bundle='com.microsoft.VSCode')

def jump_to_line(m):
    line_number = parse_words_as_integer(m._words[1:])

    if line_number == None:
        return

    # Zeroth line should go to first line
    if line_number == 0:
        line_number = 1

    # TODO: Directly interface with VSCode to accomplish the following

    # Open the jump to line input
    press('ctrl-g')

    # TODO: If requesting line that is beyond the end of the focused document, jump to last line instead

    # Enter whole line number data as if from keyboard
    Str(str(line_number))(None)

    # Confirm the navigation
    press('enter')

    # Position cursor at the beginning of meaningful text on the current line (Mac OS X)
    press('cmd-right')
    press('cmd-left')

def jump_to_next_word_instance(m):
    press('escape')    
    press('cmd-f')
    Str(' '.join([str(s) for s in m.dgndictation[0]._words]))(None)
    press('escape')

context.keymap({
    # Navigating text
    'pizza (0 | oh | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9)+': jump_to_line,

    '[toggle] terminal': Key('alt-f12'),

    # # Selecting text
    # 'select line': Key('cmd-right cmd-shift-left'),
    # 'select start': Key('cmd-shift-left'),
    # 'select end': Key('cmd-shift-right'),
    # 'select word': Key('alt-shift-right'),
    # 'select left word': Key('alt-shift-left'),
    # 'select right': Key('shift-right'),
    # 'select left': Key('shift-left'),
    'select instances': Key('cmd-shift-l'),
    
    '(top | go to top)': Key('cmd-up'),    

    # Finding text
    '(previous | last)': Key('cmd-shift-g'),
    'find next <dgndictation>': jump_to_next_word_instance,

    '(dupe | duplicate)': Key('cmd-d'),



})