import pyautogui


def get_mouse_position():
    print('Press Ctrl-C to quit.\n')
    reset_line = '\033[2K\u001b[20D'
    backspace = '\b'

    try:
        while True:
            x, y = pyautogui.position()
            position = f'X: {x:>6,d}\tY: {y:>5,d}'
            print(f'{backspace * len(position)}{position}', end='', flush=True)
            # print(f'{reset_line}{position}', end='', flush=True)

    except KeyboardInterrupt:
        print('\nDone')


if __name__ == '__main__':
    get_mouse_position()
