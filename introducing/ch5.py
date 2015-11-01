from collections import defaultdict

food_counter = defaultdict(int)

for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

from collections import Counter

breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)

lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)

# set-like operations:
#lunch_counter - breakfast_counter
#breakfast_counter & lunch_counter
#breakfast_counter | lunch_counter

from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])
for stooge in quotes:
    print(stooge)

# stack + queue == deque
def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
