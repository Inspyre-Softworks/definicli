import tkinter

# -END

from inspy_logger import InspyLogger
import PySimpleGUI as gui

from definicli.gui import ElementVisibleError


desc_col = [
    [
        gui.Text(
            "Please provide an API key we can use to authenticate with the dictionary service, below."
        )
    ],
]

desc_frame = [gui.Column(desc_col)]


btn_col_1 = [[
    gui.Button('Quit', key='QUIT_BTN', enable_events=True, size=(8, 2))
]]

btn_col_2 = [[gui.Button('Submit', key='SUBMIT_BTN', enable_events=True)]]

btn_col_3 = [[gui.Button('Test Key', key='TEST_KEY_BTN', enable_events=True)]]

btn_frame = [
    [
        gui.Column(btn_col_1),
        gui.Column(btn_col_2, visible=False, key='BTN_COL_2'),
        gui.Column(btn_col_3, visible=False, key='BTN_COL_3')
        ]
    ]

layout = [
    [
        gui.Text("API Key: ", size=(20,1)),
        gui.InputText('', size=(20,1), key='API_KEY_INPUT', enable_events=True)
        ],
    [
        gui.Frame('', layout=btn_frame)
        ]
]

show_submit_btn = False
submit_btn_visible = False

def show_button(btn):
    """
    Switches the 'visible' state of the frame containing 'btn' to True and then draw changes if needed.

    Parameters:

        btn (str): 
            The name of the button you'd like to make visible. Can pick from;
        
                - 'submit'
                - 'test_key'

    Raises:

        ValueError: 
            Raised when the value for 'btn' does not match one of the allowed values. (See above for help on the 'btn' parameter)
        
        definicli.gui.ElementVisibleError: 
            Raised when the specified button is already visible but a call was made to make it visible again. 

    """
    elm_key = None

    if submit_btn_visible:
        raise ElementVisibleError()

    if btn.lower() == 'submit':
        elm_key = 'BTN_COL_2'
    elif btn.lower() == 'test_key':
        elm_key = 'BTN_COL_3'
    
    if not elm_key:
        raise ValueError()
    else:
        if show_submit_btn:
            show_submit_btn = False


win = gui.Window("Test", layout=layout)

while True:
    event, values = win.read(timeout=100)

    if event is None:
        win.close()
        break

    if event == 'QUIT_BTN':
        win.close()
        break

    if event == 'API_KEY_INPUT':
        if not show_submit_btn:
            if len(values['API_KEY_INPUT']) >= 15:
                show_submit_btn = True
        
        else:
            if len(values['API_KEY_INPUT']) <= 14:
                show_submit_btn = False




                win['BTN_COL_2'].Update(visible=True)
        if values['API_KEY_INPUT'] == '':
            
        else:
            win['BTN_COL_2'].Update(visible=True)
