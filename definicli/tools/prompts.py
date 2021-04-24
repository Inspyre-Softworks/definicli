from prompt_toolkit.shortcuts import button_dialog, input_dialog


def attention(msg, title=None):
    prefix = "Attention!"
    if title:
        _title = prefix + f' - {title}'
    else:
        _title = prefix

    buttons = [("Continue", True), ("Exit", False)]

    message = f"{msg}\n\nPress continue."

    btn_dialog = button_dialog(title=_title, text=message, buttons=buttons).run()

    return btn_dialog


def get_input(msg, title=None):

    if not title:
        _title = "Please provide input."
    else:
        _title = title

    in_dialog = input_dialog(title=_title, text=msg).run()

    return in_dialog
