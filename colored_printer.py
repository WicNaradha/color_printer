def colored_print(text, fg_color=None, bg_color=None, style=None):
    """
    Prints text with specified foreground color, background color, and style.

    Parameters:
        text (str): The text to be printed.
        fg_color (str): Foreground color (e.g., "red", "green").
        bg_color (str): Background color (e.g., "yellow", "blue").
        style (str): Text style (e.g., "bold", "underline").

    Available Colors: black, red, green, yellow, blue, magenta, cyan, white
    Available Styles: bold, underline, reset
    """
    # Define ANSI color codes
    colors = {
        "black": 30, "red": 31, "green": 32, "yellow": 33,
        "blue": 34, "magenta": 35, "cyan": 36, "white": 37,
    }
    styles = {"bold": 1, "underline": 4, "reset": 0}
    
    # Build the ANSI sequence
    codes = []
    if style in styles:
        codes.append(str(styles[style]))
    if fg_color in colors:
        codes.append(str(colors[fg_color]))
    if bg_color in colors:
        codes.append(str(colors[bg_color] + 10))  # Background colors start at 40

    # Combine codes and format the text
    ansi_sequence = "\033[" + ";".join(codes) + "m" if codes else ""
    reset_sequence = "\033[0m"
    print(f"{ansi_sequence}{text}{reset_sequence}")

# Example usage
if __name__=="__main__":
    colored_print("Hello, World!", fg_color="red", bg_color="yellow", style="bold")
    colored_print("This is underlined text!", fg_color="blue", style="underline")
    colored_print("Simple green text.", fg_color="green")
    colored_print("Default styling here!")