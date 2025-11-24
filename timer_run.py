import FreeSimpleGUI as sg
from math import floor

def counter_func(total_seconds):
    minutes = (floor(total_seconds / 60))
    sec = total_seconds - (minutes * 60)
    if len(str((round(sec)))) < 2:
        sec = "0" + str(round(sec))
    else:
        sec=round(sec)
    #print(f" [[   {minutes}:{sec}]]")
    return str(minutes), str(sec)


def parse_inputtext(input_text:str):
    split_text=None
    minute = "00"
    sec = "00"
    separators = (":", ".", " ",)

    if len(input_text) > 2:
        for x in separators:
            if x in input_text:
                split_text=input_text.split(x)

    if len(input_text) <= 2:
        minute = input_text
    elif split_text and len(split_text) == 2:
            minute=split_text[0]
            sec = split_text[1]

    return minute, sec


def pause_toggle(window, paused=False, running=True, pauseblink_invis=False): # paused is a bool, represents existing state, not desired state. Returns the new paused state.

    if running:
        running = False
        pause_blink(window, pauseblink_invis=False, new_text="[Paused]") # pauseblink invis here is always true, to force it to toggle visibility off regardless of actual state, hopefully feels more responsive without the 1 sec wait..
        paused=True
        pauseblink_invis=False

    else:
        running = True
        pause_blink(window, pauseblink_invis=True, new_text="Pause")
        paused=False
        pauseblink_invis=False # not invis because it's running

    return pauseblink_invis, paused, running

def pause_blink(window, pauseblink_invis, new_text=None):
    if pauseblink_invis:
        new_colour = numbers_colour
        pauseblink_invis=False
    else:
        new_colour = paused_numbers
        pauseblink_invis=True
    window['minutes'].update(text_color=new_colour)
    window['seconds'].update(text_color=new_colour)
    if new_text and new_text is not None:
        window['-PAUSE-'].update(new_text)
    return pauseblink_invis

bg_brown="#332b26"
bg_blue = "#36554E"#"darkblue"
numbers_colour="yellow"
paused_numbers = bg_blue

my_new_theme = {'BACKGROUND': bg_brown,
                'TEXT': "#ffd768",
                'INPUT': "#45523F",
                'TEXT_INPUT': "#f5db74",
                'SCROLL': "#003e9b",
                'BUTTON': ('black', "#F8DC5E"),
                'PROGRESS': ('#01826B', '#D0D0D0'),
                'BORDER': 3,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0}

# Add your dictionary to the PySimpleGUI themes
sg.theme_add_new('MyNewTheme', my_new_theme)

# Switch your theme to use the newly added one. You can add spaces to make it more readable
sg.theme('My New Theme')

#def name(name):
#    dots = 26-len(name)-2
#    return sg.Text(name + ' ' + '•'*dots, size=(26,1), justification='r',pad=(0,0), font='Courier 10')

def counter_text(key_str="minutes", txt_col=numbers_colour):
    counting_font='segoe 40 bold'


    return sg.Text(text='00', key=key_str, size=(3,1), background_color=bg_blue, relief="sunken", border_width=6, justification="center", font=counting_font, text_color=txt_col, pad=(20,8))

def make_button(width:float=10, height:float=10, key_str:str="Pause"):
        key_upper = key_str.upper()
        key_formatting = str("-" + key_upper + '-')
        return sg.Button(key_str, key=key_formatting, size=(width,height), font=("courier", "10", "bold"))

def make_spacer(width:float=0, height:float=0):
    return sg.Canvas(size=(width, height), background_color="purple")

def add_dots(dot_size=10):

    dot_instance = sg.Text('•', font=(f"courier {dot_size} bold"), auto_size_text=True, pad=0, justification="centre")
    return dot_instance

def make_vert_dots(size1=10, size2=10, size3=10):
    vert_dots_layout = [[add_dots(size1)], [add_dots(size2)], [add_dots(size3)]]
    return vert_dots_layout

def make_horz_dots(size1=10, size2=10, size3=10):
    horz_dots_layout = [[add_dots(size1), add_dots(size2), add_dots(size3)]]
    return horz_dots_layout

def mid_gap():
    mid_dots = [[add_dots(10)], [add_dots(10)]]
    return mid_dots

def make_window():
    #sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.

    numbers = [[counter_text("minutes"),
                sg.Column(layout=mid_gap()),
                counter_text("seconds"),
                  ]]

#    column_one = [[
#        sg.Column(layout=numbers, background_color="red")
#    ]]
#    column_two = [[sg.InputText(default_text="5:18", size=(16, 20), border_width=2, focus=False, enable_events=True,
#                                key='-INPUT-', tooltip="Input styles: \n     min.sec (15.10), \n     min:sec (15:10), \n     15m10s, \n     15m, \n     10s, \n     15 (defaults to minutes if not specified.)")
#                   ],
#                    [sg.VStretch()],
#                    [sg.Stretch(), make_button(width=10, height=1, key_str="Start"), sg.Stretch()],
#                    [sg.VStretch()],
#                    [sg.Stretch(), make_button(width=10, height=1, key_str="Pause"), sg.Stretch()],
#                    [sg.VStretch()],
#                    [sg.Stretch(), make_button(width=10, height=1, key_str="Exit"), sg.Stretch()],
#                    [make_spacer(height=10)]
#    ]
#        #sg.Button('Start', key='-START-', size=(30,15)), sg.Button('Pause', key='-PAUSE-', size=(20,10)), ], [sg.Button('Exit', key='-EXIT-', size=(20,10)), sg.Stretch()],

    column_one_vert = [[sg.HSeparator(color="gold")],
                       [sg.Canvas(size=(340,5))],
                       #[sg.Stretch(), make_button(width=10, height=1, key_str="Start"), sg.Stretch(), make_button(width=10, height=1, key_str="Pause"), sg.Stretch(), make_button(width=10, height=1, key_str="Exit"), sg.Stretch()],
                    [sg.Column(layout=make_vert_dots(size1=10, size2=12, size3=14), vertical_alignment="center"),
                     sg.Column(layout=numbers, justification="c", vertical_alignment="center"),
                     sg.Column(layout=make_vert_dots(size1=10, size2=12, size3=14), vertical_alignment="center")]]

    column_two_vert = [[sg.Canvas(size=(340,1), pad=2)],
                    [sg.HSeparator(color="gold")],
                    [sg.Canvas(size=(340,5))],

                    [sg.Stretch(),
                     sg.Column(layout=make_horz_dots(size1=10, size2=12, size3=14), pad=0),
                     sg.Text('•', font=("courier 14 bold"), pad=0),
                     sg.InputText(default_text="5:18", size=(16, 20), border_width=2, focus=False, enable_events=True, justification="c", font=("courier", "10", "bold"),
                        key='-INPUT-', tooltip="Input styles: \n     min.sec (15.10), \n     min:sec (15:10), \n     15m10s, \n     15m, \n     10s, \n     15 (defaults to minutes if not specified.)"),
                        sg.Text('•', font=("courier 14 bold")),
                        sg.Column(layout=make_horz_dots(size1=14, size2=12, size3=10)),
                        sg.Stretch()],
                    [sg.VStretch()],
                    [sg.Stretch(), make_button(width=10, height=1, key_str="Start"), sg.Stretch(), make_button(width=10, height=1, key_str="Pause"), sg.Stretch(), make_button(width=10, height=1, key_str="Exit"), sg.Stretch()],
                    [add_dots(), sg.Canvas(size=(165,1), pad=2), add_dots(), sg.Canvas(size=(165,1), pad=2), add_dots()]]
                    #[add_dots(), sg.Stretch(), sg.HSeparator(color="gold"), sg.Stretch(), add_dots()]#make_spacer(height=5), add_dots()]

    main_contents_vert = [
            [sg.Column(layout=column_one_vert, justification="center")], [sg.Column(layout=column_two_vert, justification="center")]
        ]

#    main_contents = [
#        [sg.Column(layout=column_one), sg.Column(layout=column_two)],
#    ]

    layout = [[sg.Frame(title="timer ••", layout=main_contents_vert, font=("courier", "10", "bold"), relief="groove", pad=((0, 0),(0,5)))]]

    # Create the Window
    minute = sec = 00
    running=False
    paused=False
    pauseblink_invis=False
    total_sec=10
    window = sg.Window('Window Title', layout, keep_on_top=True, finalize=True, alpha_channel=.95, no_titlebar=True, grab_anywhere=True, titlebar_background_color="brown", titlebar_text_color="#ffd768", titlebar_font="courier 10 bold")
    window['-INPUT-'].bind("<Return>", "_Enter")
    while True:
        event, values = window.read(timeout=1000)
        if event == "-START-" or event == "-INPUT-" + "_Enter":
            if paused:
                pauseblink_invis, paused, running = pause_toggle(window, paused, running=False) # need to toggle the pause here so it doesn't stop the start button working.
            else:
                running=True
            input_text: str = values['-INPUT-']
            if input_text:
                minute, sec = parse_inputtext(input_text)
                print(f"Minute: {minute}, sec: {sec}")
                print("Starting clock...")
                total_sec = (float(minute) * 60) + float(sec)

                window['minutes'].update(minute)
                window['seconds'].update(sec)
                window['-START-'].update("[Restart]")
                # I really want to animate it opening its eyes when the timer's about to start.
            else:
                print("Please enter a number")

        if event == sg.WIN_CLOSED or event == '-EXIT-':  # if user closes window or clicks cancel
            running=False
            break

        if total_sec < 0:
            running = False

        if event == "-PAUSE-":
            pauseblink_invis, paused, running = pause_toggle(window, paused, running, pauseblink_invis) # invis is always starting from False regardless of actual status here.

        if paused:
            pauseblink_invis = pause_blink(window, pauseblink_invis)

        if running:
            minutes, seconds = counter_func(total_sec)
            window['minutes'].update(minutes)
            window['seconds'].update(seconds)
            total_sec -= 1
            window.finalize()
            if total_sec < 0:
                running=False

    window.close()


if __name__ == '__main__':
    make_window()
