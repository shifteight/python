def count_fragments(fragment, dna):
    count = 0
    last_match = dna.find(fragment, 0)
    while last_match != -1:
        count += 1
        last_match = dna.find(fragment, last_match + 1)

    return count

print(count_fragments('gtg', 'gttacgtggatg'))
print(count_fragments('gtt', 'gttacgtggatg'))
