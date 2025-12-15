import os
import platform
import textwrap

def set_window_size(width=100, height=40):
    if platform.system() == "Windows":
        os.system(f'mode con: cols={width} lines={height}')

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_wrapped(text, width=80, indent=0):
    indent_str = " " * indent
    wrapped = textwrap.fill(
        text, 
        width=width,
        initial_indent=indent_str,
        subsequent_indent=""
        )
    print(wrapped)

def get_limited_input(prompt, max_length=20):
    while True:
        user_input=input(prompt)
        if len(user_input) <= max_length:
            return user_input
        else:
            print(f"Please enter no more than {max_length} characters.")
    
def sanitize_input(text):
    text = text.strip()

    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 -'"
    text =''.join(char for char in text if char in allowed_chars)

    return text

def get_input_with_commands(prompt, character):
    while True:
        user_input = input(prompt).strip().lower()

        if user_input in ['sheet', 'cs', 'character', 'character sheet']:
            display_character_sheet(character)
            print()
            continue
        else:
            return user_input

def display_character_sheet(character):
    print("\n=== CHARACTER SHEET ===")
    print(f"Name: {character.name}")
    print(f"Species: {character.species}")
    print(f"Career: {character.career}")
    print(f"Soak: {character.soak}")
    print(f"Strain: {character.strain}")
    print(f"\n{character.species} Characteristics:")
    print(f"  Brawn: {character.brawn}")
    print(f"  Agility: {character.agility}")
    print(f"  Intellect: {character.intellect}")
    print(f"  Cunning: {character.cunning}")
    print(f"  Willpower: {character.willpower}")
    print(f"  Presence: {character.presence}")
    print(f"\n{character.career} Skills:")

    skills_list = list(character.skills.items())
    for skill in range(0, len(skills_list), 2):
        skill_name, rank = skills_list[skill]
        left = f"  - {skill_name}: Rank {rank}".ljust(50)

        if skill + 1 < len(skills_list):
            skill_name2, rank2 = skills_list[skill + 1]
            right = f"  - {skill_name2}: Rank {rank2}"
        else:
            right = ""
        print(left + right)

    input("\nPress Enter to return to the game...")

def display_roll_results(results,net):
    print("\n=== DICE RESULTS ===")
    print(f"Success: {results['success']}")
    print(f"Failure: {results['failure']}")
    print(f"Advantage: {results['advantage']}")
    print(f"Threat: {results['threat']}")
    print(f"Triumph: {results['triumph']}")
    print(f"Despair: {results['despair']}")
    
    print("\n=== NET RESULTS ===")
    print(f"Net Success: {net['net_success']}")
    print(f"Net Advantage: {net['net_advantage']}")