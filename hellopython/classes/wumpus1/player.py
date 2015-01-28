import shlex


class Player(object):

    def __init__(self, location):
        self.location = location
        self.location.here.append(self)
        self.playing = True
        self.inventory = []

    actions = ['quit', 'inv', 'get', 'drop']

    def get_input(self):
        return raw_input(">")

    def process_input(self, input):
        parts = shlex.split(input)
        if len(parts) == 0:
            return []
        if len(parts) == 1:
            parts.append("")
        verb = parts[0]
        noun = " ".join(parts[1:])

        handler = self.find_handler(verb, noun)
        if handler is None:
            return [input +
                    "? I don't know how to do that!"]
        return handler(self, noun)

    def find_handler(self, verb, noun):
        # try and find the object
        if noun != "":
            object = [x for x in self.location.here + self.inventory
                      if x is not self and
                      x.name == noun and
                      verb in x.actions]
            if len(object) > 0:
                return getattr(object[0], verb)

        if verb.lower() in self.actions:
            return getattr(self, verb)
        elif verb.lower() in self.location.actions:
            return getattr(self.location, verb)

    def quit(self, player, noun):
        self.playing = False
        return ['bye bye!']

    def get(self, player, noun):
        return [noun + "? I can't see that here."]

    def drop(self, player, noun):
        return [noun + "? I don't have that."]

    def inv(self, player, noun):
        result = ["You have:"]
        if self.inventory:
            result += [x.name for x in self.inventory]
        else:
            result += ["nothing!"]
        return result
    


if __name__ == '__main__':
    import cave
    caves = cave.create_caves()

    cave1 = caves[0]

    import item
    sword = item.Item("sword", "A pointy sword.", cave1)
    coin = item.Item("coin", "A shiny gold coin."
                     "Your first piece of treasure!", cave1)
    
    player = Player(cave1)

    print '\n'.join(player.location.look(player, ''))

    while player.playing:
        input = player.get_input()
        result = player.process_input(input)
        print "\n".join(result)
