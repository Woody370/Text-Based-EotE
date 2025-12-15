from species import SPECIES_DATA
from careers import CAREERS_DATA
from skills import ALL_SKILLS
from utilities import get_limited_input, sanitize_input

class Character:
    def __init__(self, name, species, career, 
                 brawn, agility, intellect,
                 cunning, willpower, presence,
                 soak, strain, skills, pronouns
    ):
        self.name = name
        self.species = species
        self.pronouns = pronouns
        self.career = career
        
        self.brawn = brawn
        self.agility = agility
        self.intellect = intellect
        self.cunning = cunning
        self.willpower = willpower
        self.presence = presence

        self.soak = soak
        self.strain = strain

        self.skills = skills

def choose_species():
    print("Choose your character's species:")
    species_list = list(SPECIES_DATA.keys())

    for index, species_name in enumerate(species_list, start=1):
        print(f"{index}. {species_name}")

    print()

    while True:
        choice_string = input("Enter the number of your choice: ")

        if not choice_string.isdigit():
                print("Please enter a valid number.")
                continue

        choice = int(choice_string)

        if 1 <= choice <= len(species_list):
            selected_species = species_list[choice - 1]
            print(f"{selected_species}")
            return selected_species
        else:
            print("That is not an option. Try again.")

def choose_pronouns():
    print("Choose your character's pronouns:")
    print("1. He/Him")
    print("2. She/Her")
    print("3. They/Them")
    print()

    while True:
        choice_string = input("Enter the number of your choice: ")

        if not choice_string.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice_string)

        if choice == 1:
            return {"subject": "he", "object": "him", "possessive": "his"}
        elif choice == 2:
            return {"subject": "she", "object": "her", "possessive": "her"}
        elif choice == 3:
            return {"subject": "they", "object": "them", "possessive": "their"}
        else:
            print("That is not an option. Try again.")

def choose_career():
    print("Choose your character's career: ")
    career_list = list(CAREERS_DATA.keys())

    for index, career_name in enumerate(career_list, start=1):
        print(f"{index}. {career_name}")
    
    print()

    while True:
        choice_string = input("Enter the number of your choice: ")
        if not choice_string.isdigit():
            print("Please enter a valid number.")
            continue
        choice = int(choice_string)

        if 1 <= choice <= len(career_list):
            selected_career = career_list[choice - 1]
            print(f"{selected_career}")
            return selected_career
        else:
            print("That is not an option. Try again.")

def create_character():
    print("=== Character Creation ===")
    print()

    while True:        
        name = get_limited_input("Enter your character's name: ", max_length=25)
        name = sanitize_input(name)
        if name: 
            break
        else:
            print("Name cannot be empty. Please enter a name.")
    print()

    pronouns = choose_pronouns()
    print()

    species = choose_species()
    species_stats = SPECIES_DATA[species]
    
    print()

    career = choose_career()
    career_skills = CAREERS_DATA[career]["skills"]

    skills = {}
    for skill_name in ALL_SKILLS:
        if skill_name in career_skills:
            skills[skill_name] = 1
        else:
            skills[skill_name] = 0

    character = Character(
        name=name,
        pronouns=pronouns,
        species=species,
        career=career,
        brawn=species_stats["brawn"],
        agility=species_stats["agility"],
        intellect=species_stats["intellect"],
        cunning=species_stats["cunning"],
        willpower=species_stats["willpower"],
        presence=species_stats["presence"],
        soak=species_stats["soak_base"] + species_stats["brawn"],
        strain=species_stats["strain_base"] + species_stats["willpower"],
        skills=skills
    )
    print("\n=== Character Summary ===")
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
    
    return character