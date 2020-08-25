'''module to take input'''

class _getChUnix:
    '''class to take input'''

    def __init__(self):
        '''init def to take input'''
        import tty
        import sys

    def __call__(self):
        '''def to call function'''
        import sys
        import tty
        import termios
        fvr = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fvr)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fvr, termios.TCSADRAIN, old_settings)
        return ch
