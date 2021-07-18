import pygame

from .playingMode import PlayingMode
<<<<<<< HEAD
from .coinPlayMode import CoinMode
=======
from .coinPlayMode import CoinPlayingMode
from .env import *
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

from .env import *
from .sound_controller import *

'''need some fuction same as arkanoid which without dash in the name of fuction'''

class RacingCar:
<<<<<<< HEAD
    def __init__(self, user_num: int, difficulty,sound):
        self.is_sound = sound
        self.sound_controller = SoundController(self.is_sound)
        if difficulty == "NORMAL":
            self.game_mode = PlayingMode(user_num,self.sound_controller)
            self.game_type = "NORMAL"
        elif difficulty == "COIN":
            self.game_mode = CoinMode(user_num,self.sound_controller)
            self.game_type = "COIN"

        self.user_num = user_num
=======
    def __init__(self, user_num: int, difficulty):
        if difficulty == "NORMAL":
            self.game_mode = PlayingMode(user_num)
            self.game_type = "NORMAL"
        elif difficulty == "COIN":
            self.game_mode = CoinPlayingMode(user_num)
            self.game_type = "COIN"
        pass
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

    def get_player_scene_info(self) -> dict:
        scene_info = self.get_scene_info
        return {
            "ml_1P" : scene_info,
            "ml_2P" : scene_info,
            "ml_3P" : scene_info,
            "ml_4P" : scene_info
        }

    def update(self, commands):
        self.game_mode.handle_event()
        self.game_mode.detect_collision()
        self.game_mode.update_sprite(commands)
        self.draw()
        if not self.isRunning():
            return "QUIT"

    def reset(self):
        self.__init__(self.user_num,self.game_type,self.is_sound)

    def isRunning(self):
        return self.game_mode.isRunning()

    def draw(self):
        self.game_mode.draw_bg()
        self.game_mode.drawAllSprites()
        self.game_mode.flip()

    @property
    def get_scene_info(self):
        """
        Get the scene information
        """
<<<<<<< HEAD
        cars_pos = []
        computer_cars_pos = []
        lanes_pos = []

        scene_info = {
            "frame": self.game_mode.frame,
            "status": self.game_mode.status,
            "background": [(self.game_mode.bg_x,0),(self.game_mode.rel_x,0)],
            "line":[(self.game_mode.line.rect.left,self.game_mode.line.rect.top)]}

        for car in self.game_mode.cars_info:
            cars_pos.append(car["pos"])
            if car["id"] <= 4:
                scene_info["player_"+str(car["id"])+"_pos"] = car["pos"]
            elif car["id"] > 100:
                computer_cars_pos.append(car["pos"])
        scene_info["computer_cars"] = computer_cars_pos
        scene_info["cars_pos"] = cars_pos

        for lane in self.game_mode.lanes:
            lanes_pos.append((lane.rect.left, lane.rect.top))
        scene_info["lanes"] = lanes_pos

        if self.game_type == "COIN":
            coin_pos = []
            for coin in self.game_mode.coins:
                coin_pos.append(coin.get_position())
            scene_info["coin"] = coin_pos

        scene_info["game_result"] = self.game_mode.winner
=======
        coin_pos = []
        computer_cars_pos = []
        lanes_pos = []
        player_1_pos = ()
        player_2_pos = ()
        player_3_pos = ()
        player_4_pos = ()
        player_1_distance = 0
        player_2_distance = 0
        player_3_distance = 0
        player_4_distance = 0
        player_1_velocity = 0
        player_2_velocity = 0
        player_3_velocity = 0
        player_4_velocity = 0
        player_1_coin_num = 0
        player_2_coin_num = 0
        player_3_coin_num = 0
        player_4_coin_num = 0

        for car in self.game_mode.cars_info:
            if car["id"] >= 101:
                computer_cars_pos.append((car["pos"][0]-20,car["pos"][1]-40))
            elif car["id"] == 0:
                player_1_pos = (car["pos"][0]-20,car["pos"][1]-40)
                player_1_distance = car["distance"]
                player_1_coin_num = car["coin_num"]
                player_1_velocity = car["velocity"]

            elif car["id"] == 1:
                player_2_pos = (car["pos"][0]-20,car["pos"][1]-40)
                player_2_distance = car["distance"]
                player_2_coin_num = car["coin_num"]
                player_2_velocity = car["velocity"]

            elif car["id"] == 2:
                player_3_pos = (car["pos"][0]-20,car["pos"][1]-40)
                player_3_distance = car["distance"]
                player_3_coin_num = car["coin_num"]
                player_3_velocity = car["velocity"]

            elif car["id"] == 3:
                player_4_pos = (car["pos"][0]-20,car["pos"][1]-40)
                player_4_distance = car["distance"]
                player_4_coin_num = car["coin_num"]
                player_4_velocity = car["velocity"]

        for lane in self.game_mode.lanes:
            lanes_pos.append((lane.rect.left, lane.rect.top))

        if self.game_type == "NORMAL":
            scene_info = {
                "frame": self.game_mode.frame,
                "status": self.game_mode.status,
                "computer_cars": computer_cars_pos,
                "lanes": lanes_pos,
                "player1_pos": player_1_pos,
                "player2_pos": player_2_pos,
                "player3_pos": player_3_pos,
                "player4_pos": player_4_pos,
                "player_1_distance":player_1_distance,
                "player_2_distance":player_2_distance,
                "player_3_distance":player_3_distance,
                "player_4_distance":player_4_distance,
                "player_1_velocity":player_1_velocity,
                "player_2_velocity":player_2_velocity,
                "player_3_velocity":player_3_velocity,
                "player_4_velocity":player_4_velocity,
                "player_1_coin_num":player_1_coin_num,
                "player_2_coin_num":player_2_coin_num,
                "player_3_coin_num":player_3_coin_num,
                "player_4_coin_num":player_4_coin_num,
                "game_result": self.game_mode.winner}

        elif self.game_type == "COIN":
            for coin in self.game_mode.coins:
                coin_pos.append(coin.get_position())
            scene_info = {
                "frame": self.game_mode.frame,
                "status": self.game_mode.status,
                "computer_cars": computer_cars_pos,
                "lanes": lanes_pos,
                "player1_pos": player_1_pos,
                "player2_pos": player_2_pos,
                "player3_pos": player_3_pos,
                "player4_pos": player_4_pos,
                "player_1_distance": player_1_distance,
                "player_2_distance": player_2_distance,
                "player_3_distance": player_3_distance,
                "player_4_distance": player_4_distance,
                "player_1_velocity": player_1_velocity,
                "player_2_velocity": player_2_velocity,
                "player_3_velocity": player_3_velocity,
                "player_4_velocity": player_4_velocity,
                "player_1_coin_num": player_1_coin_num,
                "player_2_coin_num": player_2_coin_num,
                "player_3_coin_num": player_3_coin_num,
                "player_4_coin_num": player_4_coin_num,
                "coins":coin_pos,
                "game_result": self.game_mode.winner}

>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
        return scene_info

    def get_game_info(self):
        """
        Get the scene and object information for drawing on the web
        """
<<<<<<< HEAD
        game_info = {
=======


        return {
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
            "scene": {
                "size": [WIDTH, HEIGHT]
            },
            "game_object": [
<<<<<<< HEAD
                {"name": "background", "size": (2000, HEIGHT), "color": BLACK, "image": "ground0.jpg"},
                {"name": "lane", "size": lane_size, "color": WHITE},
                {"name": "coin", "size": coin_size, "color": YELLOW, "image":"logo.png"},
                {"name": "computer_car", "size": car_size, "color": LIGHT_BLUE, "image": "computer_car.png"},
                {"name": "player1_car", "size": car_size, "color": WHITE, "image": "car1.png"},
                {"name": "player2_car", "size": car_size, "color": YELLOW, "image": "car2.png"},
                {"name": "player3_car", "size": car_size, "color": BLUE, "image": "car3.png"},
                {"name": "player4_car", "size": car_size, "color": RED, "image": "car4.png"},
                {"name": "line", "size": (45,450), "color": WHITE, "image": "start.png"},
                {"name": "icon", "size": (319,80), "color": BLACK, "image": "info_km.png"},
            ],
            "images": ["car1.png", "car2.png", "car3.png", "car4.png", "computer_car.png",
                      "car1-bad.png", "car2-bad.png", "car3-bad.png", "car4-bad.png", "computer_die.png",
                      "start.png", "finish.png", "info_coin.png", "info_km.png",
                      "logo.png", "ground0.jpg"
                      ]
=======
                {"name": "lane", "size": [5, 30], "color": WHITE},
                {"name": "computer_car", "size": [40, 60], "color": (0, 191, 255)},
                {"name": "player1_car", "size": [40, 60], "color": RED},
                {"name": "player2_car", "size": [40, 60], "color": YELLOW},
                {"name": "player3_car", "size": [40, 60], "color": GREEN},
                {"name": "player4_car", "size": [40, 60], "color": BLUE},
                {"name":"coins", "size":[20,20], "color":(255, 193, 37)},
                {"name": "player1_car_icon", "size": [10, 10], "color": RED},
                {"name": "player2_car_icon", "size": [10, 10], "color": YELLOW},
                {"name": "player3_car_icon", "size": [10, 10], "color": GREEN},
                {"name": "player4_car_icon", "size": [10, 10], "color": BLUE},
            ]
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
        }

        if self.game_type == "COIN":
            game_info["game_object"][9]={"name": "icon", "size": (319,80), "color": BLACK, "image": "info_coin.png"}

        return game_info

    def _progress_dict(self, pos_left, pos_top, size = None, color = None, image = None):
        '''
        :return:Dictionary for game_progress
        '''
        object = {"pos" : [pos_left, pos_top]}
        if size != None:
            object["size"] = size
        if color != None:
            object["color"] = color
        if image != None:
            object["image"] = image

        return object

    def get_game_progress(self):
        """
        Get the position of game objects for drawing on the web
        """
<<<<<<< HEAD
        scene_info = self.get_scene_info
        game_progress = {"game_object": {
        "background" : [self._progress_dict(scene_info["background"][0][0], scene_info["background"][0][1]),
                        self._progress_dict(scene_info["background"][1][0], scene_info["background"][1][1])],
        "icon": [self._progress_dict(WIDTH-315, 5)],
        "line":[self._progress_dict(scene_info["line"][0][0], scene_info["line"][0][1])],
        },
        "game_user_information":[]}

        if self.game_mode.status == "RUNNING":
            for user in self.game_mode.users:
                user_info = {}
                user_info["distance"] = round(user.distance)
                if self.game_type == "COIN":
                    user_info["coin"] = user.coin_num
                game_progress["game_user_information"].append(user_info)

                if user.status  == False:
                    game_progress["game_object"]["player"+str(user.car_no+1) + "_car"] = [{"pos":scene_info["player_" + str(user.car_no) + "_pos"],
                                                                                           "image":"car" + str(user.car_no+1) + "-bad.png"}]
                else:
                    game_progress["game_object"]["player"+str(user.car_no+1) + "_car"] = [{"pos":scene_info["player_" + str(user.car_no) + "_pos"]}]

        lane_pos = []
        for lane in scene_info["lanes"]:
            lane_pos.append(self._progress_dict(lane[0], lane[1]))
        game_progress["game_object"]["lane"] = lane_pos

        computer_car_pos = []
        for computer in scene_info["computer_cars"]:
            computer_car_pos.append(self._progress_dict(computer[0], computer[1]))
        game_progress["game_object"]["computer_car"] = computer_car_pos

        if self.game_type == "COIN":
            coin_pos = []
            for coin in scene_info["coin"]:
                coin_pos.append(self._progress_dict(coin[0], coin[1]))
            game_progress["game_object"]["coin"] = coin_pos
        return game_progress
=======
        scene_info = self.get_scene_info()

        if self.game_type == "NORMAL":
            return {
                "game_object": {
                    "lane": scene_info["lanes"],
                    "computer_car": scene_info["computer_cars"],
                    "player1_car": [scene_info["player1_pos"]],
                    "player2_car": [scene_info["player2_pos"]],
                    "player3_car": [scene_info["player3_pos"]],
                    "player4_car": [scene_info["player4_pos"]],
                    "player1_car_icon": [(645,700)],
                    "player2_car_icon": [(680,700)],
                    "player3_car_icon": [(715,700)],
                    "player4_car_icon": [(750,700)],
                },
                "status": {
                     "player_1_distance": scene_info["player_1_distance"],
                     "player_1_velocity": scene_info["player_1_velocity"],
                     "player_2_distance": scene_info["player_2_distance"],
                     "player_2_velocity": scene_info["player_2_velocity"],
                     "player_3_distance": scene_info["player_3_distance"],
                     "player_3_velocity": scene_info["player_3_velocity"],
                     "player_4_distance": scene_info["player_4_distance"],
                     "player_4_velocity": scene_info["player_4_velocity"],}
            }

        elif self.game_type == "COIN":
            return {
                "game_object": {
                    "lane": scene_info["lanes"],
                    "coins":scene_info["coins"],
                    "computer_car": scene_info["computer_cars"],
                    "player1_car": [scene_info["player1_pos"]],
                    "player2_car": [scene_info["player2_pos"]],
                    "player3_car": [scene_info["player3_pos"]],
                    "player4_car": [scene_info["player4_pos"]],
                    "player1_car_icon": [(645, 700)],
                    "player2_car_icon": [(680, 700)],
                    "player3_car_icon": [(715, 700)],
                    "player4_car_icon": [(750, 700)],
                },
                "status": {
                    "player_1_distance": scene_info["player_1_distance"],
                    "player_1_velocity": scene_info["player_1_velocity"],
                    "player_1_coin": scene_info["player_1_coin_num"],
                    "player_2_distance": scene_info["player_2_distance"],
                    "player_2_velocity": scene_info["player_2_velocity"],
                    "player_2_coin": scene_info["player_2_coin_num"],
                    "player_3_distance": scene_info["player_3_distance"],
                    "player_3_velocity": scene_info["player_3_velocity"],
                    "player_3_coin": scene_info["player_3_coin_num"],
                    "player_4_distance": scene_info["player_4_distance"],
                    "player_4_velocity": scene_info["player_4_velocity"],
                    "player_4_coin": scene_info["player_4_coin_num"]}
                    }
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

    def get_game_result(self):
        """
        Get the game result for the web
        """
        scene_info = self.get_scene_info
        result = []
        ranking = []
        for user in scene_info["game_result"]:
            result.append("GAME_DRAW")
<<<<<<< HEAD
=======
            ranking.append(str(user.car_no + 1) + "P")
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

        return {
            "frame_used": scene_info["frame"],
            "result": result,
<<<<<<< HEAD
            "ranking": scene_info["game_result"]
=======
            "ranking": ranking
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2
        }

    def get_keyboard_command(self):
        """
        Get the command according to the pressed keys
        """
        key_pressed_list = pygame.key.get_pressed()
        cmd_1P = []
        cmd_2P = []

        if key_pressed_list[pygame.K_LEFT]: cmd_1P.append(BRAKE_cmd)
        if key_pressed_list[pygame.K_RIGHT]:cmd_1P.append(SPEED_cmd)
        if key_pressed_list[pygame.K_UP]:cmd_1P.append(LEFT_cmd)
        if key_pressed_list[pygame.K_DOWN]:cmd_1P.append(RIGHT_cmd)

        if key_pressed_list[pygame.K_a]: cmd_2P.append(BRAKE_cmd)
        if key_pressed_list[pygame.K_d]:cmd_2P.append(SPEED_cmd)
        if key_pressed_list[pygame.K_w]:cmd_2P.append(LEFT_cmd)
        if key_pressed_list[pygame.K_s]:cmd_2P.append(RIGHT_cmd)

        return {"ml_1P":cmd_1P,
                "ml_2P":cmd_2P}

# if __name__ == '__main__':
#     pygame.init()
#     display = pygame.display.init()
#     game = Game(4)
#
#     while game.isRunning():
#         game.update(commands)
#         game.draw()
#
#     pygame.quit()
