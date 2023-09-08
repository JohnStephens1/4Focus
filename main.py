import pyglet


# todo
#  add title
#  check for performance optimization

# todo
#  figure out how to reliably package program for non-python users
#  add sad cat meme as icon
#  write readme (4 everything ;-;)


def run_app():
    display = pyglet.canvas.get_display()
    screens = display.get_screens()
    windows = []

    for screen in screens:
        windows.append(pyglet.window.Window(fullscreen=True, screen=screen))

    for window in windows:
        add_hotkeys(window, windows)

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


def main():
    run_app()


if __name__ == "__main__":
    main()
