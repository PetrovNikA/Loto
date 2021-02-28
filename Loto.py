import random

ballsleft = 90
balls = random.sample(range(90), 90)
game_set = random.sample(range(90), 30)
p1_set = random.sample(game_set, 15)
p2_set = [e for e in game_set if not e in p1_set]
p1_field = [p1_set[:5], p1_set[5:10], p1_set[10:]]
p2_field = [p2_set[:5], p2_set[5:10], p2_set[10:]]
for p1line in p1_field:
    p1line.sort()
    p1line.insert(random.randint(0, 4), ' ')
    p1line.insert(random.randint(0, 5), ' ')
    p1line.insert(random.randint(0, 6), ' ')
    p1line.insert(random.randint(0, 7), ' ')
for p2line in p2_field:
    p2line.sort()
    p2line.insert(random.randint(0, 4), ' ')
    p2line.insert(random.randint(0, 5), ' ')
    p2line.insert(random.randint(0, 6), ' ')
    p2line.insert(random.randint(0, 7), ' ')


def field(p):
    if p == 0:
        print('{:-^26}'.format(' Ваша карточка '))
        for line1 in p1_field:
            for n1 in line1:
                print('{0:>2}'.format(n1), end=' ')
            print()
        print('{:-^26}\n'.format('-'))
    if p == 1:
        print('{:-^26}'.format(' Карточка компьютера '))
        for line2 in p2_field:
            for n2 in line2:
                print('{0:>2}'.format(n2), end=' ')
            print()
        print('{:-^26}\n'.format('-'))


field(0)
field(1)
