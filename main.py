from skill_checks import make_skill_check
from character_sheet import create_character

def intro_scene(character):
    print(f"\n{character.name} finds {character.pronouns['object']}self sitting at the counter of the Boiling Bar while visiting "
          "Flitrude: one of a thousand moons of the Outer Rim planet Iego."
    )
    print(f"\nThough just in the port city of Foghaven for a simple layover, {character.pronouns['object']} can't "
          "shake the feeling that something is wrong here. Looking around the bar, patrons of all types "
          "are present. Some are shady figures in dark corners, others more boistrous and lively at the "
          f"nearby pazaak table. One member catches {character.pronouns['possessive']} eye, but the "
          "smoke makes it difficult to see who the mysterious character is. Roll a Perception check!"
    )
    input("\nPress Enter to roll...")

    result = make_skill_check(character, "Perception (Cun)", difficulty=2, setback=1)

    print(f"\nNet Success: {result['net_success']}")
    print(f"Net Advantage: {result['net_advantage']}")

    if result['net_success'] > 0:
        print(f"\n{character.name} peers through the smoke and meets the eyes of a grimy Weequay. "
              "Something about him feels awful familiar... "
              "Before getting many more details, he quickly stands from his table and makes for the door."
              )
    else:
        print(f"\n{character.name} squints but can't make out who it is through the haze. "
              f"Another patron bumps into {character.pronouns['object']} and {character.pronouns['subject']} "
               "loses concentration."
               )
    
    input("\nPress Enter to continue...")

def main():
    character = create_character()
    print(f"\nYour journey begins, {character.name} the "
          f"{character.species} {character.career}")
    input("\nPress Enter to continue...")
    intro_scene(character)





if __name__ == "__main__":
    main()