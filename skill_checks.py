from dice import roll_dice, calculate_net_results

def extract_char(skill_name):
    start = skill_name.rfind("(")
    end = skill_name.rfind(")")

    if start != -1 and end != -1:
        return skill_name[start + 1:end]
    return None

def get_char_for_skill(character, skill_name):
    abbrev = extract_char(skill_name)

    char_map = {
        "Br": character.brawn,
        "Ag": character.agility,
        "Int": character.intellect,
        "Cun": character.cunning,
        "Will": character.willpower,
        "Pr": character.presence
    }

    return char_map.get(abbrev, 0)

def build_dice_pool(characteristic, skill_rank):
    ability_dice = characteristic
    proficiency_dice = 0

    for _ in range(skill_rank):
        if ability_dice > 0:
            ability_dice -= 1
            proficiency_dice += 1
        else:
            ability_dice += 1
    
    return ability_dice, proficiency_dice

def make_skill_check(character, skill_name, difficulty=1, challenge=0, setback=0, boost=0):
    skill_rank = character.skills.get(skill_name, 0)

    characteristic_value = get_char_for_skill(character, skill_name)

    ability_dice, proficieny_dice = build_dice_pool(characteristic_value, skill_rank)

    results = roll_dice(
        ability=ability_dice,
        proficiency=proficieny_dice,
        difficulty=difficulty,
        challenge=challenge,
        setback=setback,
        boost=boost
    )

    net = calculate_net_results(results)

    return net