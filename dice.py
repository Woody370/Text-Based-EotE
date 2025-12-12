import random

BOOST_DIE = [
    {},
    {},
    {"success": 1},
    {"success": 1, "advantage": 1},
    {"advantage": 2},
    {"advantage": 1}
]

ABILITY_DIE = [
    {},
    {"success": 1},
    {"success": 1},
    {"success": 2},
    {"advantage": 1},
    {"advantage": 1},
    {"success": 1, "advantage": 1},
    {"advantage": 2}
]

PROFICIENCY_DIE = [
    {},
    {"success": 1},
    {"success": 1},
    {"success": 2},
    {"success": 2},
    {"advantage": 1},
    {"success": 1, "advantage": 1},
    {"success": 1, "advantage": 1},
    {"success": 1, "advantage": 1},
    {"advantage": 2},
    {"advantage": 2},
    {"triumph": 1}
]

SETBACK_DIE = [
    {},
    {},
    {"failure": 1},
    {"failure": 1, "threat": 1},
    {"threat": 2},
    {"threat": 1}
]

DIFFICULTY_DIE = [
    {},
    {"failure": 1},
    {"failure": 1},
    {"failure": 2},
    {"threat": 1},
    {"threat": 1},
    {"failure": 1, "threat": 1},
    {"threat": 2}
]

CHALLENGE_DIE = [
    {},
    {"failure": 1},
    {"failure": 1},
    {"failure": 2},
    {"failure": 2},
    {"threat": 1},
    {"failure": 1, "threat": 1},
    {"failure": 1, "threat": 1},
    {"failure": 1, "threat": 1},
    {"threat": 2},
    {"threat": 2},
    {"despair": 1}
]

def roll_dice(ability=0, proficiency=0, boost=0, difficulty=0, challenge=0, setback=0):
    results = {
        "success": 0,
        "failure": 0,
        "advantage": 0,
        "threat": 0,
        "triumph": 0,
        "despair": 0
    }

    for _ in range(ability):
        face = random.choice(ABILITY_DIE)
        for symbol, count in face.items():
            results[symbol] += count
    
    for _ in range(proficiency):
        face = random.choice(PROFICIENCY_DIE)
        for symbol, count in face.items():
            results[symbol] += count
            if symbol == "triumph":
                results["success"] += count

    for _ in range(boost):
        face = random.choice(BOOST_DIE)
        for symbol, count in face.items():
            results[symbol] += count
    
    for _ in range(difficulty):
        face = random.choice(DIFFICULTY_DIE)
        for symbol, count in face.items():
            results[symbol] += count
    
    for _ in range(challenge):
        face = random.choice(CHALLENGE_DIE)
        for symbol, count in face.items():
            results[symbol] += count
            if symbol == "despair":
                results["failure"] =+ count

    for _ in range(setback):
        face = random.choice(SETBACK_DIE)
        for symbol, count in face.items():
            results[symbol] += count

    return results

def calculate_net_results(results):
    net_success = (results["success"] + results["triumph"] - 
                   results["failure"] - results["despair"]
    )
    net_advantage = results["advantage"] - results["threat"]

    return {
        "net_success": net_success,
        "net_advantage": net_advantage,
        "triumph": results["triumph"],
        "despair": results["despair"]
    }