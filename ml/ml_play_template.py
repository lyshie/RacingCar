class MLPlay:
    def __init__(self, player):
        self.player = player
        if self.player == "player1":
            self.player_no = 0
        elif self.player == "player2":
            self.player_no = 1
        elif self.player == "player3":
            self.player_no = 2
        elif self.player == "player4":
            self.player_no = 3
<<<<<<< HEAD
        self.other_cars_position = []
        self.coins_pos = []
        print("Initial ml script")
=======
        self.car_vel = 0
        self.car_pos = ()
        self.coin_num = 0
        pass
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

    def update(self, scene_info: dict):
        """
        Generate the command according to the received scene information
        """
<<<<<<< HEAD
        if scene_info["status"] == "RUNNING":
            self.car_pos = scene_info["player_" + str(self.player_no) + "_pos"]
=======
        self.car_pos = scene_info[self.player]
        for car in scene_info["cars_info"]:
            if car["id"]==self.player_no:
                self.car_vel = car["velocity"]
                self.coin_num = car["coin_num"]
>>>>>>> fa34c7aa43c18c14874846de3b044d39d00db5f2

        self.other_cars_position = scene_info["cars_pos"]
        if scene_info.__contains__("coin"):
            self.coin_pos = scene_info["coin"]

        return ["SPEED"]

    def reset(self):
        """
        Reset the status
        """
        print("reset ml script")
        pass
