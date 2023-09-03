import tkinter as tk
import screeninfo


# todo
#  window.lift() on click on any of the windows to all windows
#  escape in any window closes program (all windows)



def run_window():
    window = tk.Tk()
    # window.attributes('-fullscreen', True)
    window.config(bg="black")

    window.geometry(f"500x500+2000+200")
    window.attributes("-fullscreen", True)

    # new_window = tk.Toplevel()
    # new_window.config(bg="black")

    window.attributes()
    window.mainloop()


def get_total_screen_width():
    return sum([monitor.width for monitor in screeninfo.get_monitors()])


def run_screen_info():
    # for monitor in screeninfo.get_monitors():
    #     print(monitor.width)
    pass


def main():
    # run_window()
    # run_screen_info()


if __name__ == "__main__":
    main()
