import random
import item, player, monster, cave

class Game(object):

    def __init__(self):
        self.caves = self.create_caves()
        cave1 = self.caves[0]
        sword = item.Item("sword", "A pointy sword.", cave1)
        coin = item.Item("coin", "A shiny gold coin. "
                         "Your first piece of treasure!", cave1)
        orc = monster.Monster(cave1, 'orc', 'A generic dungeon monster')
        self.player = player.Player(cave1)

    cave_names = [
         "Arched cavern",
        "Twisty passages",
        "Dripping cave",
        "Dusty crawlspace",
        "Underground lake",
        "Black pit",
        "Fallen cave",
        "Shallow pool",
        "Icy underground river",
        "Sandy hollow",
        "Old firepit",
        "Tree root cave",
        "Narrow ledge",
        "Winding steps",
        "Echoing chamber",
        "Musty cave",
        "Gloomy cave",
        "Low ceilinged cave",
        "Wumpus lair",
        "Spooky Chasm",
    ]

    def create_caves(self):
        random.shuffle(self.cave_names)
        caves = [cave.Cave(self.cave_names[0])]
        for name in self.cave_names[1:]:
            new_cave = cave.Cave(name)
            eligible_caves = [each_cave for each_cave in caves
                              if each_cave.can_tunnel_to()]
            old_cave = random.choice(eligible_caves)
            directions = [direction for direction, each_cave
                          in old_cave.tunnels.items()
                          if each_cave is None]
            direction = random.choice(directions)
            old_cave.tunnel_to(direction, new_cave)
            caves.append(new_cave)
        return caves

    def do_input(self):
        get_input_from = [thing for cave in self.caves
                          for thing in cave.here
                          if 'get_input' in dir(thing)]
        for thing in get_input_from:
            thing.events = []
            thing.input = thing.get_input()

    def do_update(self):
        things_to_update = [thing for cave in self.caves
                            for thing in cave.here
                            if 'update' in dir(thing)]
        for thing in things_to_update:
            thing.update()

    def run(self):
        while self.player.playing:
            self.do_input()
            self.do_update()


if __name__ == '__main__':
    game = Game()
    game.run()
