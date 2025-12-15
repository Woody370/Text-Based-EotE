from skill_checks import make_skill_check
from character_sheet import create_character
from utilities import *

def intro_scene(character):
    clear_screen()
    print()
    print_wrapped(
        f"{character.name} finds {character.pronouns['object']}self sitting at the counter of the Boiling Bar while visiting "
        "Flitrude: one of a thousand moons of the Outer Rim planet Iego.", 
        indent=4
        )
    print()
    print_wrapped(f"Though just in the port city of Foghaven for a simple layover, {character.pronouns['subject']} can't "
          "shake the feeling that something is wrong here. Looking around the bar, patrons of all types "
          "are present. Some are shady figures in dark corners, others more boistrous and lively at the "
          f"nearby pazaak table. One member catches {character.pronouns['possessive']} eye, but the "
          "smoke makes it difficult to see who the mysterious character is. Roll a Perception check.", 
          indent=4
          )
    get_input_with_commands("\nType 'Sheet' to view your character, or Press Enter to roll...", character)
    clear_screen()

    results, net = make_skill_check(character, "Perception (Cun)", difficulty=2, setback=1)
    display_roll_results(results, net)
    print()

    if net['net_success'] > 0:
        print_wrapped(f"Despite the smoke making it difficult to see, {character.name} peers through the haze "
                      "and meets the eyes of a grimy Weequay.",
                      indent=4
                      )
        print()
        print_wrapped(f"Something about him feels awful familiar. {character.name} racks {character.pronouns['possessive']} "
                      "brain to recall who it is. Roll a Lore check.",
                      indent=4
                      )
        get_input_with_commands("\nType 'Sheet' to view your character, or Press Enter to roll...", character)
        clear_screen()

        results, net = make_skill_check(character, "Knowledge - Lore (Int)", difficulty=3)
        display_roll_results(results, net)
        print()

        if net['net_success'] > 0:
            print_wrapped(f"{character.name} remembers seeing this Weequay at the space port on a holo. "
                          f"He is wanted for serial pickpocketing and appears to have marked {character.name} as "
                          "his next target",
                          indent=4
                          )
        else:
            print_wrapped(f"{character.name} can't quite place where {character.pronouns['subject']} has seen this "
                          "Weequay before..."
                          )
        input("\nPress Enter to continue...")
        clear_screen()
    
    
    else:
        print_wrapped(f"{character.name} squints but can't make out who it is through the haze. "
                      f"{character.name} is too focused to notice a server droid buzzing by and is plowed into. "
                      f"The tray of drinks and food flies in the air as {character.name} falls to the ground. "
                      f"When {character.pronouns['subject']} looks back up, the mysterious patron has disappeared. "
                      f"{character.name} gets the feeling that it is time to leave.",
                      indent=4
                      )
    input("\nPress Enter to continue...")
    clear_screen()





def main():
    set_window_size(100, 40)
    character = create_character()
    print(f"\nYour journey begins, {character.name} the "
          f"{character.species} {character.career}")
    input("\nPress Enter to continue...")
    intro_scene(character)





if __name__ == "__main__":
    main()