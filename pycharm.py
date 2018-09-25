from talon.voice import Context, Key, Str, press

ctx = Context('pycharm', func=lambda app, win: app.bundle == 'com.jetbrains.pycharm')

PYTHON = '[(pie | pi | py | python)]'

keymap = {
    # Basic Python
    f'{PYTHON} self': 'self',
    f'{PYTHON} from': 'from ',
    f'{PYTHON} raise': 'raise ',
    f'{PYTHON} import': 'import ',
    f'{PYTHON} break': 'break',
    f'{PYTHON} continue': 'continue',
    f'{PYTHON} return': 'return ',
    f'{PYTHON} jason': 'json',
    f'{PYTHON} true': 'True',
    f'{PYTHON} false': 'False',
    f'{PYTHON} none': 'None',
    f'{PYTHON} if': ['if :', Key('left')],
    f'{PYTHON} else': ['else :', Key('left')],
    f'{PYTHON} else if': ['elif :', Key('left')],
    f'{PYTHON} while': ['while :', Key('left')],
    f'{PYTHON} for loop': ['for x in :', Key('left')],
    f'{PYTHON} print': ['print()', Key('left')],
    f'{PYTHON} range': ['range()', Key('left')],
    f'{PYTHON} (def | deaf | deft)': ['def :', Key('left')],
    f'{PYTHON} in it': ['def __init__(self, ):', Key('left left')],

    # list methods
    f'{PYTHON} pop': ['pop()', Key('left')],
    f'{PYTHON} append': ['append()', Key('left')],
    f'{PYTHON} count': ['count()', Key('left')],
    f'{PYTHON} index': ['index()', Key('left')],
    f'{PYTHON} insert': ['insert()', Key('left')],
    f'{PYTHON} remove': ['remove()', Key('left')],
    f'{PYTHON} extend': ['extend()', Key('left')],
    f'{PYTHON} sort': ['sort()', Key('left')],

    # Python: relies on custom PyCharm live templates
    f'{PYTHON} class': ['pyclass', Key('tab')],
}

ctx.keymap(keymap)


def unload(): ctx.unload()

