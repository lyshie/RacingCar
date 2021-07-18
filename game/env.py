from os import path

<<<<<<< HEAD
'''width and height'''
WIDTH = 1000
HEIGHT = 700

'''environment data'''
FPS = 30
ceiling = 600
finish_line = 20000
cars_num = 15

'''color'''
=======
WIDTH = 800
HEIGHT = 800
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
<<<<<<< HEAD
GREY = (140,140,140)
BLUE = (3,28,252)
LIGHT_BLUE = (33, 161, 241)

'''object size'''
car_size = (60, 30)
coin_size = (30,31)
lane_size = (20,3)

'''command'''
LEFT_cmd = "MOVE_LEFT"
RIGHT_cmd = "MOVE_RIGHT"
SPEED_cmd = "SPEED"
BRAKE_cmd = "BRAKE"

'''data path'''
IMAGE_DIR = path.join(path.dirname(__file__), 'image')
SOUND_DIR = path.join(path.dirname(__file__), 'sound')
BACKGROUND_IMAGE = ["ground0.jpg"]

RANKING_IMAGE = ["info_coin.png", "info_km.png"]

START_LINE_IMAGE = ["start.png", "finish.png"]
USER_IMAGE = [["car1.png","car1-bad.png"],["car2.png","car2-bad.png"],
              ["car3.png","car3-bad.png"], ["car4.png","car4-bad.png"]]
COMPUTER_CAR_IMAGE = ["computer_car.png","computer_die.png"]
USER_COLOR = [WHITE, YELLOW, BLUE, RED]


=======
BLUE = (0, 0, 255)
GREY = (190, 190, 190)
FPS = 30
lane_center = [105,245,385,525]
user_image = ["使用者車.png", "使用者車2.png", "使用者車3.png", "使用者車4.png", ["white", "chartreuse", "pink", "azure"]]
IMAGE_DIR = path.join(path.dirname(__file__),'image')
SOUND_DIR = path.join(path.dirname(__file__),'sound')
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
