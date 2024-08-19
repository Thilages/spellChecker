import string
import keyboard
from spellchecker import SpellChecker

checker = SpellChecker()

current_word = ""
correction_list = []
current_correction_index = 0

toggle = True

def key_function(event):
    global current_word
    if event.name in string.ascii_letters:
        current_word += event.name
    elif event.name == "space":  # Reset on space or punctuation
        current_word = ""
    elif event.name == "backspace" and current_word:
        current_word = current_word[:-1]

def correct_spelling(e):
    global current_word, current_correction_index, correction_list
    print("works")
    if not current_word:
        return

    # Get the list of correction candidates only once per word
    if not correction_list:
        candidates = checker.candidates(current_word)
        if candidates:
            correction_list = list(candidates)
            print(correction_list)
        else:
            return

    if correction_list:
        # Apply the current correction
        corrected_word = correction_list[current_correction_index]

        if corrected_word != current_word:
            # Remove the incorrect word
            for _ in range(len(current_word)):
                keyboard.send("backspace")

            # Type the corrected word
            keyboard.write(corrected_word)
            current_word = corrected_word  # Update current_word with the corrected word

        # Update the index for the next correction
        current_correction_index += 1
        if current_correction_index >= len(correction_list):
            current_correction_index = 0

def reset_all(e):
    global current_word, current_correction_index, correction_list
    current_word = ""
    current_correction_index = 0
    correction_list = []

def toggle_fun():
    global toggle
    toggle = not toggle
    # update_bindings()

# def update_bindings():
#     if toggle:
#
#   
#         keyboard.unhook(sample_function)
#         keyboard.unhook_key("shift")

# Ensure that the space reset and toggle hotkey are always active
keyboard.on_press_key("space", reset_all)
keyboard.add_hotkey("esc+p", toggle_fun)
keyboard.on_press(key_function)
keyboard.on_press_key("shift", correct_spelling)
# Start with the bindings active
# update_bindings()

# Wait for the specified keys to quit
keyboard.wait("esc+p+k")
