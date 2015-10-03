from pygame.image import load as load_image


class Hero(object):
    def __init__(self, max_hp, starting_money, stamina, sprite, run):
        self.hp = self.max_hp = max_hp
        self.money = starting_money
        self.stamina = stamina
        self.image = load_image(sprite)

    @property
    def alive(self):
        return self.hp > 0

    @property
    def can_run(self):
        return self.stamina > 0
