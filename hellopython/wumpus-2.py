from random import choice

# set up cave
cave_numbers = range(0, 20)
caves = []
for i in cave_numbers:
    caves.append([])

unvisited_caves = range(0, 20)
visited_caves = [0]
unvisited_caves.remove(0)

while unvisited_caves != []:

    # pick random visited cave
    i = choice(visited_caves)
    if len(caves[i]) >= 3:
        continue

    # link it to an unvisited one
    next_cave = choice(unvisited_caves)
    caves[i].append(next_cave)
    caves[next_cave].append(i)

    # mark cave as visited
    visited_caves.append(next_cave)
    unvisited_caves.remove(next_cave)

##    # progress report
##    for number in cave_numbers:
##        print number, ":", caves[number]
##    print '---------------'

# dig out rest of tunnels    
for i in cave_numbers:
    while len(caves[i]) < 3:
        passage_to = choice(cave_numbers)
        caves[i].append(passage_to)

##    for number in cave_numbers:
##        print number, ":", caves[number]
##    print '----------------'

wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location):
    player_location = choice(cave_numbers)

# welcome player
print "Welcome to Hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"

while True:
    # warn if Wumpus is nearby
    print "You are in cave", player_location
    print "From here, you can see caves:", caves[player_location]
    if wumpus_location in caves[player_location]:
        print "I smell a wumpus!"

    # ask player to pick cave
    print "Which cave next?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print player_input + "?"
        print "That's not a direction that I can see!"
        continue
    # move player
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
            print "Aargh! You got eaten by a wumpus!"
            break
