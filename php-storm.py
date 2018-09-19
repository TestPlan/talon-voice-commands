from talon.voice import Context, Key, Str, press

ides = [
    "com.jetbrains.PhpStorm",
]

ctx = Context('phpstorm', func=lambda app, win: any(
    i in app.bundle for i in ides))


def blade_switch():
    def blade_switch_function(m):
        Str('@switch($)')(None)
        press('return')
        for x in range(0, 3):
            Str('@case()')(None)
            press('return')
            press('return')
            Str('@break')(None)
            press('return')
            press('return')
        Str('@default')(None)
        press('return')
        press('return')
        Str('@endswitch')(None)
        press('shift-tab')
        for x in range(0, 15):
            press('up')
        press('left')

    return blade_switch_function


def blade_for_each():
    def blade_for_each_function(m):
        Str('@foreach($ as $)')(None)
        press('return')
        press('return')
        Str('@endforeach')(None)
        press('shift-tab')
        press('up')
        press('up')
        press('left')

    return blade_for_each_function


def blade_if():
    def blade_if_function(m):
        Str('@if ()')(None)
        press('return')
        press('return')
        Str('@endif')(None)
        press('shift-tab')
        press('up')
        press('up')
        press('left')

    return blade_if_function


def blade_section():
    def blade_section_function(m):
        Str('@section(\'\')')(None)
        press('return')
        press('return')
        Str('@endsection')(None)
        press('shift-tab')
        press('up')
        press('up')
        press('left')

    return blade_section_function


def blade_if_else():
    def blade_if_else_function(m):
        Str('@if ()')(None)
        press('return')
        press('return')
        press('shift-tab')
        blade_else()(None)
        press('return')
        Str('@endif')(None)
        press('shift-tab')
        for x in range(0, 4):
            press('up')
        press('left')

    return blade_if_else_function


def blade_else():
    def blade_else_function(m):
        Str('@else')(None)
        press('return')

    return blade_else_function


def blade_php():
    def blade_php_function(m):
        Str('@php  @endphp')(None)
        for x in range(0, 8):
            press('left')

    return blade_php_function


def blade_include():
    def blade_include_function(m):
        Str('@include(\'\')')(None)
        for x in range(0, 2):
            press('left')

    return blade_include_function


keymap = {

    # blade
    'blade if': blade_if(),
    'blade switch': blade_switch(),
    'blade if else': blade_if_else(),
    'blade php': blade_php(),
    'blade include': blade_include(),
    'blade else': blade_else(),
    'blade for each': blade_for_each(),
    'blade data': '{{ ',
    'blade continue': '@continue',
    'blade break': '@break',
    'blade parent': '@parent',
    'blade case': ['@case()', Key('left')],
    'blade extends': ['@extends(\'\')', Key('left'), Key('left')],
    'blade section': blade_section(),
    'blade loop': '$loop',
    'blade raw data': '{!',

    # CSS
    'with': ['width: ;', Key('left')],
    'max with': ['max-width: ;', Key('left')],
    'min with': ['min-width: ;', Key('left')],
    '(hover | however)': 'hover ',
    'ram': 'rem',

    # Foundation CSS Framework
    'ramcalc': ['rem-calc()', Key('left')],

    '(flip | phiz | fizz)': ['php', Key('tab')],
    'party': ['phps', Key('tab')],
    '(start flip | start phiz | start fizz)': '<?php ',
    '(end flip | end phiz | end fizz)': '?> ',
    # 'search': [Key('shift'), Key('shift')],
    'golf': ['fore', Key('tab')],
    'horse': ['for', Key('tab')],
    'horse markup': ['formk', Key('tab')],
    'chop': ['forek', Key('tab')],
    'eagles': ['?=', Key('tab')],
    'if': ['if', Key('tab')],
    'if markup': ['ifm', Key('tab')],
    'else if': ['elif', Key('tab')],
    'else if markup': ['elifm', Key('tab')],
    'else': ['else', Key('tab')],
    'else markup': ['elsem', Key('tab')],
    'complete': Key('cmd-shift-enter'),
    'definition': Key('alt-space'),

}

ctx.keymap(keymap)


def unload(): ctx.unload()
