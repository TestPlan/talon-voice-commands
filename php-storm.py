from talon.voice import Context, Key, Str, press

ides = [
    "com.jetbrains.PhpStorm",
]

ctx = Context('phpstorm', func=lambda app, win: any(
    i in app.bundle for i in ides))


def foundation_breakpoint():
    def foundation_breakpoint_function(m):
        Str('@include breakpoint() {')(None)
        press('enter')
        press('cmd-right')
        press('up')
        for x in range(3):
            press('left')

    return foundation_breakpoint_function


def blade_switch():
    def blade_switch_function(m):
        Str('@switch ($)')(None)
        press('return')
        for x in range(3):
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
        for x in range(15):
            press('up')
        press('left')

    return blade_switch_function


def blade_for_each():
    def blade_for_each_function(m):
        Str('@foreach ($ as $)')(None)
        press('return')
        press('return')
        Str('@endforeach')(None)
        press('shift-tab')
        press('up')
        press('up')
        press('left')

    return blade_for_each_function


def blade_for():
    def blade_for_function(m):
        Str('@for ($i = 0; $i < ; $i++)')(None)
        press('return')
        press('return')
        Str('@endfor')(None)
        press('shift-tab')
        press('up')
        press('up')
        for x in range(12):
            press('right')

    return blade_for_function


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


def blade_else():
    def blade_else_function(m):
        Str('@else')(None)
        press('return')

    return blade_else_function


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
        for x in range(4):
            press('up')
        press('left')

    return blade_if_else_function


def blade_php():
    def blade_php_function(m):
        Str('@php  @endphp')(None)
        for x in range(8):
            press('left')

    return blade_php_function


def blade_include():
    def blade_include_function(m):
        Str('@include(\'\')')(None)
        for x in range(2):
            press('left')

    return blade_include_function


def php_explode():
    def php_explode_function(m):
        Str('explode(, );')(None)
        for x in range(4):
            press('left')

    return php_explode_function


def sass_mixin():
    def sass_mixin_function(m):
        Str('@mixin () {')(None)
        press('return')
        press('up')
        for x in range(7):
            press('right')

    return sass_mixin_function


def sass_if():
    def sass_if_function(m):
        Str('@if  {')(None)
        press('return')
        press('up')
        for x in range(2):
            press('right')

    return sass_if_function


def sass_else():
    def sass_else_function(m):
        Str('@else {')(None)
        press('return')
        press('up')

    return sass_else_function


def wordpress_template_part():
    def wordpress_template_part_function(m):
        Str('get_template_part(\'\');')(None)
        for x in range(3):
            press('left')

    return wordpress_template_part_function


keymap = {
    # PHP
    'echo': ['echo ;', Key('left')],
    'if': ['if', Key('tab')],
    'if markup': ['ifm', Key('tab')],
    'else if': ['elif', Key('tab')],
    'else if markup': ['elifm', Key('tab')],
    'else': ['else', Key('tab')],
    'else markup': ['elsem', Key('tab')],
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
    'array': ['array()', Key('left')],
    'explode': php_explode(),

    # WordPress
    'template part': wordpress_template_part(),

    # blade
    'blade if': blade_if(),
    'blade switch': blade_switch(),
    'blade if else': blade_if_else(),
    'blade php': blade_php(),
    'blade include': blade_include(),
    'blade else': blade_else(),
    'blade for': blade_for(),
    'blade for each': blade_for_each(),
    'blade section': blade_section(),
    'blade data': '{{ ',
    'blade continue': '@continue',
    'blade break': '@break',
    'blade parent': '@parent',
    'blade case': ['@case()', Key('left')],
    'blade extends': ['@extends(\'\')', Key('left'), Key('left')],
    'blade loop': '$loop',
    'blade index': 'index',
    'blade iteration': 'iteration',
    'blade remaining': 'remaining',
    'blade count': 'count',
    'blade first': 'first',
    'blade last': 'last',
    'blade depth': 'depth',
    'blade raw data': '{!',

    # HTML
    'href': 'href=',
    'id': 'id=',
    'class': 'class=',
    # HTML Using Emmet
    'tag section': ['section', Key('tab')],
    '[tag] paragraph': ['p', Key('tab')],
    'tag image': ['img', Key('tab')],
    'tag div': ['div', Key('tab')],
    '[tag] anchor': ['a', Key('tab')],
    'tag break': ['br', Key('tab')],
    'tag footer': ['footer', Key('tab')],
    'tag body': ['body', Key('tab')],
    'lorem': ['lorem', Key('tab')],

    # CSS
    # Properties
    '(width | with)': ['width: ;', Key('left')],
    'height': ['height: ;', Key('left')],
    'max (width | with)': ['max-width: ;', Key('left')],
    'max height': ['max-height: ;', Key('left')],
    'min (width | with)': ['min-width: ;', Key('left')],
    'align items': ['align-items: ;', Key('left')],
    'justify content': ['justify-content: ;', Key('left')],
    'display': ['display: ;', Key('left')],
    'margin': ['margin: ;', Key('left')],
    '(padding | patty)': ['padding: ;', Key('left')],
    'font family': ['font-family: ;', Key('left')],
    'font weight': ['font-weight: ;', Key('left')],
    'font size': ['font-size: ;', Key('left')],
    'line height': ['line-height: ;', Key('left')],
    'color': ['color: ;', Key('left')],
    'background color': ['background-color: ;', Key('left')],
    'background size': ['background-size: ;', Key('left')],
    'background repeat': ['background-repeat: ;', Key('left')],
    'background position': ['background-position: ;', Key('left')],
    'background image': ['background-image: ;', Key('left')],
    'flex direction': ['flex-direction: ;', Key('left')],
    'transform': ['transform: ;', Key('left')],
    'text transform': ['text-transform: ;', Key('left')],
    'position': ['position: ;', Key('left')],
    'top': ['top: ;', Key('left')],
    'zindex': ['z-index: ;', Key('left')],
    'visibility': ['visibility: ;', Key('left')],
    'bottom': ['bottom: ;', Key('left')],
    'text align': ['text-align: ;', Key('left')],
    'overflow': ['overflow: ;', Key('left')],
    'border': ['border: ;', Key('left')],
    'cursor': ['cursor: ;', Key('left')],
    'letter spacing': ['letter-spacing: ;', Key('left')],
    'border bottom': ['border-bottom: ;', Key('left')],
    'prop left': ['left: ;', Key('left')],
    'prop right': ['right: ;', Key('left')],

    # Pseudo Elements
    'after': '::after',
    'active': ':active',
    'visited': ':visited',
    'before': '::before',
    'first child': ':first-child',
    'last child': ':last-child',
    'first of type': ':first-of-type',
    'last of type': ':last-of-type',
    '(hover | however)': ':hover',
    # 'focus': ':focus',
    'checked': ':checked',
    'valid': ':valid',
    'target': ':target',
    'not': [':not()', Key('left')],
    'nth child': [':nth-child()', Key('left')],

    # Units
    '(rem | ram | rems | rams)': 'rem',
    '(em | ems)': 'em',
    '(px | pixel | pixels)': 'px',
    '(vh | viewport height)': 'vh',
    '(viewport width | viewport with)': 'vw',
    # Values
    'linear gradient': ['linear-gradient();', Key('left'), Key('left')],

    # SASS
    '[sass] (mixon | mixing | mix in)': sass_mixin(),
    'sass include': ['@include ;', Key('left')],
    'sass if': sass_if(),
    'sass else': sass_else(),

    # Foundation CSS Framework
    'ramcalc': ['rem-calc()', Key('left')],
    'breakpoint': foundation_breakpoint(),
    'complete': Key('cmd-shift-enter'),
    'definition': Key('alt-space'),
    'medium': 'medium',

    # Sage theme
    'sage production': ['yarn run build:production', Key('return')],

    # Next Level
    'Next Level': ['nextlevel', Key('return')],
}

ctx.keymap(keymap)


def unload(): ctx.unload()
