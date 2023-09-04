import pyglet


def run_pyglet_shenanigans():
    display = pyglet.canvas.get_display()
    screens = display.get_screens()
    windows = []

    for screen in screens:
        windows.append(pyglet.window.Window(fullscreen=True, screen=screen))

    for window in windows:
        @window.event
        def on_key_press(symbol, modifiers):
            if symbol == pyglet.window.key.ESCAPE:
                pyglet.app.exit()

    pyglet.app.run()


def main():
    run_pyglet_shenanigans()


if __name__ == "__main__":
    main()
