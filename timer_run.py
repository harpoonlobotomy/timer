import FreeSimpleGUI as sg
import time
from math import floor

def start_clock(minutes: str, sec:str):

    sec = (float(minutes) * 60) + float(sec)

    total_seconds = sec

    while total_seconds > 0:
        minutes = floor(total_seconds / 60)
        sec = total_seconds - (minutes * 60)
        if len(str((round(sec)))) < 2:
            sec = "0" + str(round(sec))
            print(f" [[   {minutes}:{sec}]]")
        else:
            print(f" [[   {minutes}:{round(sec)}]]")

        time.sleep(1)  # every second
        total_seconds -= 1  # take one second

def counter_func(total_seconds):
    minutes = (floor(total_seconds / 60))
    sec = total_seconds - (minutes * 60)
    if len(str((round(sec)))) < 2:
        sec = "0" + str(round(sec))
    else:
        sec=round(sec)
    print(f" [[   {minutes}:{sec}]]")

    return str(minutes), str(sec)

def clock_update(total_seconds):

    time.sleep(1)  # every second
    total_seconds -= 1  # take one second

    return total_seconds


def parse_inputtext(input_text:str):
    split_text=None
    minute = "00"
    sec = "00"
    separators = (":", ".", " ",)

    if len(input_text) > 2:
        #needs processing
        for x in separators:
            if x in input_text:
                split_text=input_text.split(x)
                print(f"Split text: {split_text}, len: {len(split_text)}, type: {type(split_text)}")

    if len(input_text) == 1:
        minute = input_text
    elif split_text and len(split_text) == 2:
            minute=split_text[0]
            sec = split_text[1]

    return minute, sec

def counter_text(key_str="minutes"):
    counting_font='Courier 40 bold'

    return sg.Text(text='00', key=key_str, size=(3,1), background_color="blue", relief="sunken", border_width=4, justification="center", font=counting_font)

def make_window():
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.

    numbers = [[counter_text("minutes"),
                counter_text("seconds"),
                  ]]

    column_one = [[
        sg.Column(layout=numbers, background_color="red")
    ]]
    column_two = [[sg.InputText(default_text="5:18", size=(16, 20), border_width=2, focus=False, enable_events=True, # focus=True, #turning this off so I can wipe the text when  you click it.
                                key='-INPUT-', tooltip="Input styles: \n     min.sec (15.10), \n     min:sec (15:10), \n     15m10s, \n     15m, \n     10s, \n     15 (defaults to minutes if not specified.)")
                   ],
                  [sg.Stretch(), sg.Button('Start', key='-START-'), sg.Button('Exit', key='-EXIT-'), sg.Stretch()],
                  ]

    main_contents = [
        [sg.Column(layout=column_one), sg.Column(layout=column_two)],
    ]

    layout = [[sg.Frame(title="clock", layout=main_contents)
               ]]

    # Create the Window
    minute = sec = 00
    window = sg.Window('Window Title', layout, keep_on_top=True, finalize=True)
    window['-INPUT-'].bind("<Return>", "_Enter")
    while True:
        event, values = window.read(timeout=1000)
        if event == "-START-" or event == "-INPUT-" + "_Enter":
            input_text: str = values['-INPUT-']
            if input_text:
                print('You entered ', input_text)
                minute, sec = parse_inputtext(input_text)
                print(f"Minute: {minute}, sec: {sec}")
                total_sec = (float(minute) * 60) + float(sec)
                print("Starting clock...")
                while True:
                    minutes, seconds = counter_func(total_sec)
                    window['minutes'].update(minutes)
                    window['seconds'].update(seconds)
                    print(f"min: {minutes}, sec: {seconds}")
                    total_sec = clock_update(total_sec)
                    window.finalize()
                    if total_sec < 0:
                        break
                # I really want to animate it opening its eyes when the timer's about to start.
            else:
                print("Please enter a number")

        if event == "Start":
            running = True

        if event == "Stop":
            running = False

        if running:
            total_seconds -= 1
            window["-TIMER-"].update(total_seconds)

        if total_seconds <= 0:
            running = False

        if event == sg.WIN_CLOSED or event == '-EXIT-':  # if user closes window or clicks cancel
            break

    window.close()


if __name__ == '__main__':
    make_window()
