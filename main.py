from character_sheet import create_character

def main():
    character = create_character()
    print(f"\nYour journey begins, {character.name} the "
          f"{character.species} {character.career}"
    )

if __name__ == "__main__":
    main()