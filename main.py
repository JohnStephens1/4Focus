import pyglet

import sys
import os


APPLICATION_PATH = os.path.dirname(__file__) if getattr(sys, 'frozen', True) else os.path.dirname(sys.executable)
pyglet.resource.path = [os.path.join(APPLICATION_PATH, 'resources')]


def run_app():
    display = pyglet.canvas.get_display()
    screens = display.get_screens()
    windows = []

    for screen in screens:
        windows.append(pyglet.window.Window(fullscreen=True, screen=screen, caption='4Focus'))

    for window in windows:
        add_hotkeys(window, windows)
        window.set_icon(pyglet.resource.image('sad-cat.png'))

    pyglet.app.run()


def add_hotkeys(window, windows):
    @window.event
    def on_key_press(symbol, modifiers):
        if symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()

        if symbol == pyglet.window.key.M:
            for win in windows:
                win.minimize()

        if symbol == pyglet.window.key.SPACE:
            for win in windows:
                win.maximize()

        if symbol == pyglet.window.key.DOWN:
            window.minimize()


def main():
    run_app()


if __name__ == "__main__":
    main()
