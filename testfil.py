from rpg.entities import create_skeleton, create_dragon

sk = create_skeleton()
print(sk.info())      # Skeleton (HP: 6, dmg: 1-3)
print(sk.attack())    # 1 eller 2 eller 3
sk.take_damage(2)
print(sk.is_alive())  # True (om HP > 0)

dr = create_dragon()
print(dr.info())      # Dragon (HP: 30, dmg: 4-8)