from PrintHelper import PrintHelper
from Monster import Monster
from Program import menu
import json

# Entry point of the program
def main():
    # Load default Monsters to Json object and convert Json object to list[monster]
    file = open("DefaultMonsters.json", "r")
    unprocessedMonsters = json.load(file)
    file.close()
    monsters = UnpackMonsters(unprocessedMonsters)

    # Print Helper setup and menu call
    ph = PrintHelper()
    menu(ph, monsters)

    # Pack the monsters back into a Json object and write it to file
    # Since menu() modifies the monster list, I don't have to reassign it.
    monsterJson = PackMonsters(monsters)
    file = open("OutputMonsters.json", "w")
    json.dump(monsterJson, file, indent = 4)
    file.close

# Takes a list[Monster] and converts it into a Json list
def PackMonsters(monsters: list[Monster]) -> list[dict]:
    monsterJson: list[dict] = []
    for monster in monsters:
        monsterJson.append({"name": monster.name, "elements": monster.elements, "universe": monster.universe, "attributes": monster.attributes})
    return monsterJson

# Takes a Json list and converts it into a list[Monster]
def UnpackMonsters(monsterJson: list[dict]) -> list[Monster]:
    monsters: list[Monster] = []
    for dict in monsterJson:
        monsters.append(Monster(dict["name"], dict["elements"], dict["universe"], dict["attributes"]))
    return monsters

main()