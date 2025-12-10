from species import SPECIES_DATA
from careers import CAREERS_DATA

class Character:
    def __init__(self, name, species, career, 
                 brawn, agility, intellect,
                 cunning, willpower, presence
    ):
        self.name = name
        self.species = species
        self.career = career
        
        self.brawn = brawn
        self.agility = agility
        self.intellect = intellect
        self.cunning = cunning
        self.willpower = willpower
        self.presence = presence

def choose_species():
    print("Choose your character's species:")
    species_list = list(SPECIES_DATA.keys())

    for index, species_name in enumerate(species_list, start=1):
        print(f"{index}. {species_name}")

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

def choose_career():
    print("Choose your character's career: ")
    career_list = list(CAREERS_DATA.keys())

    for index, career_name in enumerate(career_list, start=1):
        print(f"{index}. {career_name}")

    while True:
        choice_string = input("Enter the number of your choice: ")
        if not choice_string.isdigit():
            print("Please tner a valid number.")
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

    name = input("Enter your character's name: ")
    
    species = choose_species()
    species_stats = SPECIES_DATA[species]
    
    career = choose_career()
    career_skills = CAREERS_DATA[career]["skills"]

    character = Character(
        name=name,
        species=species,
        career=career,
        brawn=species_stats["brawn"],
        agility=species_stats["agility"],
        intellect=species_stats["intellect"],
        cunning=species_stats["cunning"],
        willpower=species_stats["willpower"],
        presence=species_stats["presence"],
    )

    print("\n=== Character Summary ===")
    print(f"Name: {character.name}")
    print(f"Species: {character.species}")
    print(f"Career: {character.career}")
    print(f"Characteristics:")
    print(f"  Brawn: {character.brawn}")
    print(f"  Agility: {character.agility}")
    print(f"  Intellect: {character.intellect}")
    print(f"  Cunning: {character.cunning}")
    print(f"  Willpower: {character.willpower}")
    print(f"  Presence: {character.presence}")
    print(f"Career Skills:")
    for skill in career_skills:
        print (f"  - {skill}")
    return character