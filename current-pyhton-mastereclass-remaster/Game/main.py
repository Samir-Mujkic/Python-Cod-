from enemy import Enemy, Troll, Vampyre


ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))



another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))
another_troll.take_damage(18)
print(another_troll)

brother = Troll("Urg")
print(brother)

vamp = Vampyre("Vlad")
print(vamp)
vamp.take_damage(5)
print(vamp)

while vamp.alive:
    vamp.take_damage(1)
    print(vamp)

