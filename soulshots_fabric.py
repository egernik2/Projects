# Стоимость оружия
WEAPON_PRICE = 0
# На сколько кристаллов разбивается
WEAPON_CRYSTALS = 2167
# Цена на Soul Ore
SOUL_ORE_PRICE = 270
# Сколько нужно Soul Ore на крафт
SOUL_ORE_REQ = 30
# Сколько кристаллов на крафт
CRYSTAL_REQ = 2
# Сколько сосок за крафт
SOUL_SHOTS = 952
# Сколько денег за соску
SOUL_SHOTS_PRICE = 10
# Сколько кристаллов есть
CRYSTALS_HAVE = 630

def soul_shot_cost():
    one_crystall_price = WEAPON_PRICE / WEAPON_CRYSTALS
    crystalls_per_craft_price = one_crystall_price * CRYSTAL_REQ
    soul_ore_per_craft_price = SOUL_ORE_PRICE * SOUL_ORE_REQ
    return round((crystalls_per_craft_price + soul_ore_per_craft_price) / SOUL_SHOTS, 2)

def vigoda():
    CRAFTS_HAVE = CRYSTALS_HAVE // CRYSTAL_REQ
    SOUL_ORE_NEED = CRAFTS_HAVE * SOUL_ORE_REQ
    SOUL_ORE_DENEG = SOUL_ORE_NEED * SOUL_ORE_PRICE
    SOSOK_HAVE = CRAFTS_HAVE * SOUL_SHOTS
    DENEG_VSEGO = SOSOK_HAVE * SOUL_SHOTS_PRICE
    VIGOGA = DENEG_VSEGO - SOUL_ORE_DENEG
    print(f'Crafts have: {CRAFTS_HAVE}\nDeneg need: {SOUL_ORE_DENEG}\nSosok have: {SOSOK_HAVE}\nDeneg vsego: {DENEG_VSEGO}\nVigoga: {VIGOGA}')

def main():
    #print(soul_shot_cost())
    vigoda()

if __name__ == '__main__':
    main()