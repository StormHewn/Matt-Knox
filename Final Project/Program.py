# The "core" of the program. This file has everything except the JSON handling, the indentation handling, and the Monster class.
from PrintHelper import PrintHelper
from Monster import Monster

# Main menu, entrance point to the "Game Loop"
# Variables are passed by reference, so the original will reflect the changes I make here.ope
def menu(ph: PrintHelper, monsters: list[Monster]):
    option = ""
    ph.LevelStart("Monster Maker!")
    while option != "Q":
        ph.LevelPrint()
        ph.LevelPrint("A: Add Monster")
        ph.LevelPrint("E: View/Edit Monsters")
        ph.LevelPrint("S: Search for Monsters")
        ph.LevelPrint("Q: Save and Quit")
        option = ph.LevelInput("Please choose one of the options above: ").upper()[0]
        ph.LevelPrint()

        match option:
            case "A":
                monsters.append(NewMonster(ph))
            case "E":
                EditMonster(ph, monsters)
                pass
            case "S":
                SearchMonster(ph, monsters)
                pass
            case _:
                pass

    ph.LevelEnd("Thank you for using Monster Maker! You can find your final monster list at OutputMonsters.json")

# Returns a Monster object with the input values
def NewMonster(ph: PrintHelper) -> Monster:
    ph.LevelStart("Add Monster")
    name = ph.LevelInput("What is the monster's name?: ")

    elements: list[str] = []
    input = ph.LevelInput("What are the monster's elements? (Comma-separated): ")
    elements = [s.strip().title() for s in input.split(",")]

    universe = ph.LevelInput("What universe does the monster belong to?: ")

    attributes: list[str] = []
    input = ph.LevelInput("What are the monster's other attributes? (Comma-separated): ")
    attributes = [s.strip() for s in input.split(",")]

    ph.LevelEnd(f"Added monster '{name}'")
    return Monster(name, elements, universe, attributes)

# Allows editing of the monsters' fields
def EditMonster(ph: PrintHelper, monsters: list[Monster]):
    ph.LevelStart("Edit Monsters")
    monsterIndex = ""
    while True:
        ph.LevelPrint("Q: Return to menu")
        index = 0
        for monster in monsters:
            ph.LevelPrint(f"{index}: {monster.name}")
            index += 1

        input = ph.LevelInput("Which monster would you like to view/edit? (Enter the monster's number): ").upper()
        ph.LevelPrint()
        try:
            monsterIndex = int(input)
        except ValueError:
            if input == "Q": break
            else: continue
        if monsterIndex >= len(monsters): continue
        selectedMonster = monsters[int(monsterIndex)]

        elements = ", ".join(selectedMonster.elements)
        attributes = ", ".join(selectedMonster.attributes)

        ph.LevelStart(f"Editing Monster '{selectedMonster.name}'")
        ph.LevelPrint(f"N: Name: {selectedMonster.name}")
        ph.LevelPrint(f"E: Elements: {elements}")
        ph.LevelPrint(f"U: Universe: {selectedMonster.universe}")
        ph.LevelPrint(f"A: Attributes: {attributes}")
        ph.LevelPrint(f"D: Delete monster")
        ph.LevelPrint(f"Q: Quit")
        option = ph.LevelInput("Please choose one of the options above: ").upper()[0]
        match option:
            case "N":
                selectedMonster.name = ph.LevelInput("New name: ")
            case "E":
                input = ph.LevelInput("New elements (Comma-separated): ")
                selectedMonster.elements = [s.strip() for s in input.split(",")]
            case "U":
                selectedMonster.universe = ph.LevelInput("New universe: ")
            case "A":
                input = ph.LevelInput("New attributes (Comma-separated): ")
                selectedMonster.attributes = [s.strip() for s in input.split(",")]
            case "D":
                del monsters[monsterIndex]
            case "Q": 
                ph.LevelEnd()
                break
        ph.LevelEnd()

    ph.LevelEnd()

# Searches the list of monsters for those with the input value and prints the found monsters' indecies
def SearchMonster(ph: PrintHelper, monsters: list[Monster]) -> None:
    while True:
        ph.LevelStart("Search for monsters")
        ph.LevelPrint(f"E: Elements")
        ph.LevelPrint(f"U: Universe")
        ph.LevelPrint(f"A: Attributes")
        ph.LevelPrint(f"Q: Quit")
        fieldCode = ph.LevelInput("Which field will you filter by?: ").upper()[0]
        if fieldCode == "Q": 
            ph.LevelEnd()
            break
        if fieldCode not in "EUA": continue

        searchTerm = ph.LevelInput("What is the search term?: ")
        ph.LevelPrint()

        fieldName = ""
        searchTermFound = False
        match fieldCode:
            case "E":
                fieldName = "element"
                index = 0
                ph.LevelStart(f"The monsters who have the '{searchTerm}' element are:")
                for monster in monsters:
                    if searchTerm.upper() in [x.upper() for x in monster.elements]:
                        searchTermFound = True
                        ph.LevelPrint(f"{index}: {monster.name}")
                    index += 1
                ph.LevelEnd()
            case "U":
                fieldName = "universe"
                index = 0
                ph.LevelStart(f"The monsters in the '{searchTerm}' universe are:")
                for monster in monsters:
                    if monster.universe.upper() == searchTerm.upper():
                        searchTermFound = True
                        ph.LevelPrint(f"{index}: {monster.name}")
                    index += 1
                ph.LevelEnd()
            case "A":
                fieldName = "attribute"
                index = 0
                ph.LevelStart(f"The monsters who have the '{searchTerm}' attribute are:")
                for monster in monsters:
                    if searchTerm.upper() in [x.upper() for x in monster.attributes]:
                        searchTermFound = True
                        ph.LevelPrint(f"{index}: {monster.name}")
                    index += 1
                ph.LevelEnd()
            case _: continue
        if searchTermFound == False:
            ph.LevelPrint(f"No monster with {fieldName} '{searchTerm.capitalize()}' found!")
        ph.LevelInput("Press Enter to continue")
        ph.LevelEnd()