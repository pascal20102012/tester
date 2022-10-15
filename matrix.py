import random
import sys
import pygame as pg


class MatrixLetters:
    def __init__(self, app_):
        self.app = app_
        self.letters = 'QWERTYUIOPASDFGHJKLZXCVBNMO1234056789'
        self.font_size =9
        self.font = pg.font.SysFont('arial', self.font_size, bold=True)
        self.column = self.app.width // self.font_size
        self.drops = [1 for i in range(0, self.column)]

    def _draw_symbols(self):
        for i in range(0, len(self.drops)):
            char = random.choice(self.letters)
            char_render = self.font.render(char, False, (random.randint(1,255),random.randint(1,255),random.randint(1,255)))
            position = i * self.font_size, (self.drops[i] - 1) * self.font_size
            self.app.surface.blit(char_render
                                  , position)
            if self.drops[i] * self.font_size > self.app.heigth and random.uniform(0, 1) > 0.975:
                self.drops[i] = 0
            self.drops[i] += 1

    def run(self):
        self._draw_symbols()


class MatrixApp:
    def __init__(self):
        self.WINDOW = self.width, self.heigth = 1920, 1200
        pg.init()
        self.screen = pg.display.set_mode(self.WINDOW)
        self.surface = pg.Surface(self.WINDOW, pg.SRCALPHA)
        self.clock = pg.time.Clock()
        self.matrix_letters = MatrixLetters(self)

    def _draw_screen(self):
        self.surface.fill((0, 0, 0, 10))
        self.matrix_letters.run()


        self.screen.blit(self.surface, (0, 0))

    def run(self):
        while True:
            self._draw_screen()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
            pg.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    app = MatrixApp()
    app.run()
