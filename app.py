import eel
from middleware import *

if __name__ == '__main__':
    eel.init('front')

    eel.start('index.html', mode="chrome", size=(760, 760))


