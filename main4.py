#!/usr/bin/env python3

import utils, os, random, time, open_color, arcade

utils.check_version((3,7))

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprites Example"


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)
        arcade.set_background_color(open_color.white)

        self.game_list = arcade.SpriteList()

    def setup(self):
        gameiconss = ['arrowDown', 'arrowLeft', 'arrowRight', 'arrowRight', 'arrowUp', 'audioOff']

        for i in range(20):
               
                gameicons = 'arrowDown'
                x = (400)
                y = (300)
                self.game_sprite = arcade.Sprite("1x/{gameicons}.png".format(gameicons=gameicons), 0.5)
                self.game_sprite.center_x = x
                self.game_sprite.center_y = y
                self.game_list.append(self.game_sprite)

                gameicons = random.choice(gameiconss)
                x = random.randint(0,800)
                y = random.randint(0,600)
                self.game_sprite = arcade.Sprite("1x/{gameicons}.png".format(gameicons=gameicons), 0.5)
                self.game_sprite.center_x = x
                self.game_sprite.center_y = y
                self.game_list.append(self.game_sprite)



    def on_draw(self):
        arcade.start_render()
        pass


    def update(self, delta_time):
        pass


    def on_mouse_motion(self, x, y, dx, dy):
        pass

def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()