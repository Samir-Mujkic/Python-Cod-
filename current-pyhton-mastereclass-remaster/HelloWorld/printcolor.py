import colorama



RED = '\u001b[31m'
Black = '\u001b[30m'
RESET = '\u001b[0m'


def colour_print(text: str, effect: str) -> None:
    """
    Print "text" using ansi sequance to change colour
    :param text: the text to print.
    :param effect: the effect we want. one of the constatns defines at the starg
    this moudele

    """

    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colorama.init()



