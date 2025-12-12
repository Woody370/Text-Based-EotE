# <p align="center">=== Star Wars: Edge of the Empire ===</p>  

- A very work-in-progress attempt at bringing the TTRPG to a text-based format!  

- Commits will be made to the core funtions, however I'll be uploading a Windows .exe as well  
for those who don't have WSL or VSC installed on their machines :)
<br />
  
# <p align="center"> === Character Creation ===</p>  
This will explain how character creation works **in this project.**  

## 1. Overview  

A character is defined by:  

- **Name**  
- **Species** (e.g. Human, Twi'Lek, Trandoshan, etc.)  
- **Career** (e.g. Bounty Hunter, Colonist, Smuggler, etc.)  
- **Characteristics** (e.g. Brawn, Agility, Intellect, etc.)  
- **Skills** (Career and Non-Career)  

  - Career skills are skills that your character is proficient in due to the career you choose and offer 1 free Rank (better odds when rolling) in each skill. Non-Career are all other skills. In future builds, players will be given 6 Ranks to spend in their 8 Career skills, not going above 2 Ranks in any skill at character creation.  

## 2. Species  

When you create a character, you choose a **species** from a list.  

Each species has starting **characteristics**:  
- 'Brawn'
- 'Agility'
- 'Intellect'
- 'Cunning'
- 'Willpower'
- 'Presence'  

Currently, your species assigns these starting values. However, future builds will allow a player to spend experience points to push these values higher. Higher values = better odds when rolling.  

## 3. Career  

Your **career** governs which skills your character has the ability to be proficient in from character creation. Each career offers a different selection of 8 skills, and in this version of EotE the player will be allowed to spend 6 Ranks in any of those 8 skills at character creation without going above 2 Ranks in any skill.  

The other benefit of career skills is that they cost less experience points to upgrade later. Career skills cost 5 x The Next Rank. So to go from Rank 1 to Rank 2 is 5 x 2, or 10 experience points. Non-career skills follow this same equation, however you add another 5 points after the multiplication. So Rank 1 to Rank 2 is (5x2) + 5, or 15 experience points.  

## 4. Characteristics  

As mentioned above, these are assigned via your species selection. In EotE, your **characteristics** govern your base roll for all of your career and non-career skills. For example, 2 **Brawn** provides you with two green die. Then, if you roll for a skill that is governed by Brawn - let's say **Melee** - and you have Rank 1 Melee, one of those green die is upgraded to a yellow die and your chances of success are higher.  

## 5. Skills  

Much of the **skills** has been covered above, so here is a list of all skills in the game, with the **characteristic** that governs them:  

|                                  |                |  
| -------------------------------- | -------------- |  
| Astrogation (Int)                | Athletics (Br) |  
| Charm (Pr)                       |  Coercion (Will) |  
| Computers (Int)                  | Cool (Pr) |  
| Coordination (Ag)                | Deception (Cun) |  
| Discipline (Will)                | Leadership (Pr) |  
| Mechanics (Int)                  | Medicine (Int) |  
| Negotiation (Pr)                 | Perception (Cun) |  
| Piloting - Planetary (Ag)        | Piloting - Space (Ag) |  
| Resilience (Br)                  | Skulduggery (Cun) |  
| Stealth (Ag)                     | Streetwise (Cun) |  
| Survival (Cun)                   | Vigilance (Will) |  
| Knowledge - Core Worlds (Int)    | Knowledge - Education (Int) |  
| Knowledge - Lore (Int)           | Knowledge - Outer Rim (Int) |  
| Knowledge - Underworld (Int)     | Knowledge - Xenology (Int) |  
| Brawl (Br)                       | Gunnery (Ag) |  
| Melee (Br)                       | Ranged - Light (Ag) |  
| Ranged - Heavy (Ag)              |
